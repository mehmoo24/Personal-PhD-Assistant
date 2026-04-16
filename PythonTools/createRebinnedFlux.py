# Used Interpolation to be able to rebin the flux
# Linear option was better to use for interpolation since "cubic" can introduce more wiggle
# interpolation is basically it will connect the dots betweeen all the data points, makes more sense to use than a fit,
# since want to hold onto all of the data and just rebin it, like doing digitizing of a figure essentially
# we multiplied by the bin width since the end result we didn't want normalized by the bin width

# could've also used the integral for filling in the bin instead of just using the value at the bin center, but it was a 
# good enough approximation to just use value of interpolation at bin center since 500 MeV bins

# for errors, did the same thing: used interpolation and then multiplied by the bin width, though for NUISANCE the errors on
# the flux file don't matter since it's just interested in the CV (ref. Dan)

import ROOT
import numpy as np
from scipy.optimize import curve_fit

from scipy.interpolate import interp1d


from ROOT import PlotUtils


frw = PlotUtils.FluxReweighter(14, True, PlotUtils.FluxReweighter.minervame1D1M1NWeightedAve, PlotUtils.FluxReweighter.gen2thin, PlotUtils.FluxReweighter.g4numiv6)

numu_mnv = frw.GetFluxReweighted(14)
numu = numu_mnv.GetCVHistoWithError()

frw_antinu = PlotUtils.FluxReweighter(-14, True, PlotUtils.FluxReweighter.minervame6A, PlotUtils.FluxReweighter.gen2thin, PlotUtils.FluxReweighter.g4numiv6)

numubar_mnv = frw_antinu.GetFluxReweighted(-14)
numubar = numubar_mnv.GetCVHistoWithError()

f_output = ROOT.TFile.Open("ME_Flux_Rebinned.root", "recreate")
numu.Write("numu_ME")
numubar.Write("numubar_ME")

# we want to break the 1d histogram into x_data and y_data
x_data = []
y_data = []
y_data_err = []

for bin in range(1,numu.GetNbinsX()+1):
        x_data.append(numu.GetBinCenter(bin))
        y_data.append(numu.GetBinContent(bin))
        y_data_err.append(numu.GetBinError(bin))

f_interp = interp1d(x_data, y_data, kind='linear', fill_value="extrapolate")
f_interp_err= interp1d(x_data, y_data_err, kind='linear', fill_value="extrapolate")


x_d = []
y_d = []
y_d_err = []
for bin in range(1, numubar.GetNbinsX()+1):
        x_d.append(numubar.GetBinCenter(bin))
        y_d.append(numubar.GetBinContent(bin))
        y_d_err.append(numubar.GetBinError(bin))
f_interp_numubar = interp1d(x_d, y_d, kind='linear', fill_value="extrapolate")
f_interp_err_numubar = interp1d(x_d, y_d_err, kind='linear', fill_value="extrapolate")

rebin_numu = ROOT.TH1D("rebin_numu", "rebin_numu", 200, 0, 100.0)
rebin_numubar = ROOT.TH1D("rebin_numubar", "rebin_numubar", 200, 0, 100.0)
for bin in range(1, rebin_numu.GetNbinsX()+1):
    width = rebin_numu.GetBinCenter(2)-rebin_numu.GetBinCenter(1)
    # for filling in the rebinned histograms:
    value = f_interp(rebin_numu.GetBinCenter(bin)) * width
    error = f_interp_err(rebin_numu.GetBinCenter(bin)) * width
    rebin_numu.SetBinContent(bin, value)
    rebin_numu.SetBinError(bin, error)
    val = f_interp_numubar(rebin_numubar.GetBinCenter(bin)) * width # don't want it to be bin-width normalized for NUISANCE
    err = f_interp_err_numubar(rebin_numubar.GetBinCenter(bin)) * width
    rebin_numubar.SetBinContent(bin, val)
    rebin_numubar.SetBinError(bin, err)

rebin_numu.Write("numu_ME_rebinned")
rebin_numubar.Write("numubar_ME_rebinned")

#fit.Write("Fit")


f_output.Close()
