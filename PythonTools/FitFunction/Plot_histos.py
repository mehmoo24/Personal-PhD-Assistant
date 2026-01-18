import ROOT
from ROOT import gROOT
from ROOT import gStyle
from ROOT import TGaxis, gPad, TLine
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F, TColor, TLegend
import os,sys
from ROOT import PlotUtils
from PlotUtils import MnvH2D
from PlotUtils import MnvH1D

ROOT.gROOT.SetBatch(True) # to prevent canvas from showing up interctively
mnv = PlotUtils.MnvPlotter()

# Set plot style
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPadGridX(1)
ROOT.gStyle.SetPadGridY(1)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetLabelSize(0.045, "XY")
ROOT.gStyle.SetTitleSize(0.050, "XY")
ROOT.gStyle.SetTitleOffset(1.15, "Y")
ROOT.gStyle.SetTitleOffset(1.05, "X")
ROOT.gStyle.SetNdivisions(505, "X")
ROOT.gStyle.SetNdivisions(505, "Y")



file_name = sys.argv[1]

fileName_output = sys.argv[2]
histo_name = sys.argv[3]
fit_name = sys.argv[4]
pzBin = sys.argv[5]
output_name = sys.argv[6]

file = ROOT.TFile.Open(file_name)

# the bkg is actually the reco distribution
effDen_CV = file.Get(histo_name)
effDen_univ0 = file.Get(histo_name)
effDen_univ1 = file.Get(histo_name)
fit = file.Get(fit_name)


c1 = ROOT.TCanvas("canvas", "Canvas", 600, 600)
c1.cd()
effDen_CV.SetLineWidth(3)
effDen_CV.SetLineColor(ROOT.kBlue+1)

effDen_univ0.SetLineWidth(3)
effDen_univ0.SetLineColor(ROOT.kRed+1)
effDen_univ1.SetLineWidth(3)
effDen_univ1.SetLineColor(ROOT.kOrange+1)

#bkg_3.SetLineWidth(3)
#bkg_3.SetLineColor(ROOT.kCyan+1)
#bkg_3.SetLineStyle(2)
#bkg_4.SetLineWidth(3)
#bkg_4.SetLineColor(ROOT.kMagenta+1)
#bkg_4.SetLineStyle(2)
#bkg_5.SetLineWidth(3)
#bkg_5.SetLineColor(ROOT.kGray+2)
#bkg_5.SetFillStyle(1001)
#bkg_5.SetFillColorAlpha(ROOT.kGray+2, 0.35)

#bkg_5.SetFillColor(ROOT.kGray+2)
#bkg_5.SetFillStyle(3004)

#bkg_5.SetFillStyle(1001)
#bkg_5.SetLineStyle(2)


effDen_CV.GetXaxis().SetLabelSize(0.035)
effDen_CV.GetYaxis().SetLabelSize(0.05)
effDen_CV.GetXaxis().SetTitle("Muon Transverse Momentum [GeV/c]")
effDen_CV.GetYaxis().SetTitle("Data MC Ratio, pzBin: "+pzBin)
effDen_CV.GetYaxis().SetTitleFont(2)
effDen_CV.GetYaxis().SetTitleOffset(1.5)
effDen_CV.GetXaxis().SetTitleFont(2)
effDen_CV.GetYaxis().SetTitleSize(0.05)
effDen_CV.GetXaxis().SetTitleSize(0.05)
effDen_CV.GetXaxis().CenterTitle()
effDen_CV.GetYaxis().CenterTitle()

effDen_CV.GetXaxis().SetTitleOffset(1.2)
effDen_CV.GetYaxis().SetTitleOffset(1.4)
effDen_CV.GetXaxis().SetLabelSize(0.04)
effDen_CV.GetYaxis().SetLabelSize(0.04)
effDen_CV.Draw()

# legend
# Add a legend
legend = ROOT.TLegend(0.25, 0.67, 0.45, 0.9)  # (x1, y1, x2, y2) in normalized coordinates
#legend.AddEntry(bkg_0, "Lownuflux param. MC", "l")

legend.AddEntry(effDen_CV, "Sigma Cut: 0", "l")
legend.AddEntry(effDen_univ0, "Sigma Cut: 1", "l")
legend.AddEntry(effDen_univ1, "Sigma Cut: 2", "l")
#legend.AddEntry(bkg_3, "Sigma Cut: 3", "l")
#legend.AddEntry(bkg_4, "Sigma Cut: 4", "l")
#legend.AddEntry(bkg_5, "Sigma Cut: 5", "f")
#legend.AddEntry(mnvtunev1_E_mc, "MnvTunev1 MC", "l")
#legend.AddEntry(mnvtunev1_E_data, "Nu+e flux", "ep")
legend.SetBorderSize(0)
legend.SetTextSize(0.03)

legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.SetFillColor(0)
legend.SetBorderSize(0)
legend.SetMargin(0.25)

#legend.Draw()

chi2 = fit.GetChisquare() 
ndf = fit.GetNDF()  

# Add a bold title above it
title = ROOT.TLatex()
title.SetTextFont(62)   # bold
title.SetTextSize(0.045)
title.SetTextAlign(21)
title.DrawLatexNDC(0.40, 0.92,"FIT: "+fit.GetTitle()+" CHI2/NDF: " + f"{chi2:.2f}" + "/" + f"{ndf:.2f}" )  # adjust x,y as needed
title.SetTextAlign(22)
#grayBox.Draw("SAME")

c1.SaveAs("Fit_"+histo_name+"_"+fileName_output +".png")

#util = PlotUtils.MacroUtil("MasterAnaDev", mc_file_list, data_file_list, "minervame1A", False)
#PlotUtils::MacroUtil util(reco_tree_name, mc_file_list, data_file_list, plist_string, wants_truth);


