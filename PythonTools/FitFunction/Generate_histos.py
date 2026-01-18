import ROOT
from ROOT import gROOT
from ROOT import gStyle
from ROOT import TGaxis, gPad, TLine
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F, TColor, TLegend
import os,sys
from ROOT import PlotUtils
from PlotUtils import MnvH2D
from PlotUtils import MnvH1D

def oneFit(histo, pzBin):
    proj = histo.ProjectionY(f"hpt_pzBin{pzBin}", pzBin, pzBin) # the proj of a particular pz bin
    fitOrder = 0
    chi2PerNDF = 100000
    for i in range(0, 4): # going up to 7th order polynomial
        f = ROOT.TF1("f", f"pol{i}", proj.GetXaxis().GetXmin(), proj.GetXaxis().GetXmax())
        fit_res = proj.Fit(f, "RSQ")
        val = f.GetChisquare() / f.GetNDF()
        if val < chi2PerNDF:
            chi2PerNDF = f.GetChisquare() / f.GetNDF()
            fitOrder = i
    # now get the best fit and return it
    f = ROOT.TF1("f", f"pol{fitOrder}", proj.GetXaxis().GetXmin(), proj.GetXaxis().GetXmax())
    fit_res = proj.Fit(f, "RSQ")
    return f, proj

def returnFit(histo, pzBin):
    hpt = histo.ProjectionY(f"hpt_pzBin{pzBin}", 1, 13) # 1 to 13 are the indices for pt bins
    f = ROOT.TF1("f", "pol1", hpt.GetXaxis().GetXmin(), hpt.GetXaxis().GetXmax())
    fit_res = hpt.Fit(f, "RSQ")
    print("chi2/ndf:", f.GetChisquare(), "/", f.GetNDF())
    print("coeffs:", [f.GetParameter(i) for i in range(4)])
    return f, hpt

# Inputs to take in
fileName = sys.argv[1]
outputFile_name = sys.argv[2]

file = ROOT.TFile.Open(fileName)

# Histos that we need

data = file.Get("h_data_pZmu_pTmu").GetCVHistoWithStatError()
mc = file.Get("h_mc_pZmu_pTmu").GetCVHistoWithStatError()

data.Divide(data, mc) # here's the data mc ratio we're trying to fit

f1, pzBin1 = oneFit(data, 1)
f2, pzBin2 = oneFit(data, 2)
f3, pzBin3 = oneFit(data, 3)
f4, pzBin4 = oneFit(data, 4)
f5, pzBin5 = oneFit(data, 5)
f6, pzBin6 = oneFit(data, 6)
f7, pzBin7 = oneFit(data, 7)
f8, pzBin8 = oneFit(data, 8)
f9, pzBin9 = oneFit(data, 9)
f10, pzBin10 = oneFit(data, 10)
f11, pzBin11 = oneFit(data, 11)
f12, pzBin12 = oneFit(data, 12)
f13, pzBin13 = oneFit(data, 13)
f14, pzBin14 = oneFit(data, 14)
f15, pzBin15 = oneFit(data, 15)
f16, pzBin16 = oneFit(data, 16)

# open the output root file
outFile = ROOT.TFile.Open(outputFile_name+".root", "RECREATE")
data.Write("Data_MC_Ratio")
f1.Write("Fit_pzBin1")
pzBin1.Write("Slice_pzBin1")

f2.Write("Fit_pzBin2")
pzBin2.Write("Slice_pzBin2")

f3.Write("Fit_pzBin3")
pzBin3.Write("Slice_pzBin3")

f4.Write("Fit_pzBin4")
pzBin4.Write("Slice_pzBin4")

f5.Write("Fit_pzBin5")
pzBin5.Write("Slice_pzBin5")

f6.Write("Fit_pzBin6")
pzBin6.Write("Slice_pzBin6")

f7.Write("Fit_pzBin7")
pzBin7.Write("Slice_pzBin7")

f8.Write("Fit_pzBin8")
pzBin8.Write("Slice_pzBin8")

f9.Write("Fit_pzBin9")
pzBin9.Write("Slice_pzBin9")

f10.Write("Fit_pzBin10")
pzBin10.Write("Slice_pzBin10")

f11.Write("Fit_pzBin11")
pzBin11.Write("Slice_pzBin11")

f12.Write("Fit_pzBin12")
pzBin12.Write("Slice_pzBin12")

f13.Write("Fit_pzBin13")
pzBin13.Write("Slice_pzBin13")

f14.Write("Fit_pzBin14")
pzBin14.Write("Slice_pzBin14")

f15.Write("Fit_pzBin15")
pzBin15.Write("Slice_pzBin15")

f16.Write("Fit_pzBin16")
pzBin16.Write("Slice_pzBin16")


