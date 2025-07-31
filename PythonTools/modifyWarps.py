import ROOT
from ROOT import gROOT
from ROOT import gStyle
from ROOT import TGaxis, gPad, TLine
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F, TColor, TLegend
import os,sys
from ROOT import PlotUtils
from PlotUtils import MnvH2D
from PlotUtils import MnvH1D

# Read in the warps
fileName_num_eff_file = sys.argv[1]
fileName_num_signal_file = sys.argv[2] # purity numerator
fileName_den_eff_file = sys.argv[3]
fileName_den_signal_file = sys.argv[4]
fileName_output = sys.argv[5]

# Open the files
fileName_den_signal = ROOT.TFile.Open(fileName_den_signal_file)
fileName_num_eff = ROOT.TFile.Open(fileName_num_eff_file)
fileName_den_eff = ROOT.TFile.Open(fileName_den_eff_file)
fileName_num_signal = ROOT.TFile.Open(fileName_num_signal_file)

# Get all 4 histograms
den_eff = fileName_den_eff.Get("h_mc_pZmu_pTmu").Clone()
den_eff.SetDirectory(0)
num_signal = fileName_num_signal.Get("signal_purityNum_pZmu_pTmu").Clone()
num_signal.SetDirectory(0)
den_signal = fileName_den_signal.Get("signal_purityNum_pZmu_pTmu").Clone()
den_signal.SetDirectory(0)
num_eff = fileName_num_eff.Get("h_mc_pZmu_pTmu").Clone()
num_eff.SetDirectory(0)

ratio_eff = fileName_num_eff.Get("h_mc_pZmu_pTmu").Clone()
ratio_eff.SetDirectory(0)

# open the output root file
outFile = ROOT.TFile.Open("Modified_Warp_"+fileName_output+".root", "RECREATE")
num_eff.Write("h_mc_pZmu_pTmu_num")
den_eff.Write("h_mc_pZmu_pTmu_den")
num_signal.Write("signal_purityNum_pZmu_pTmu_num")
den_signal.Write("signal_purityNum_pZmu_pTmu_den")

nbinsX = num_eff.GetNbinsX()
nbinsY = num_eff.GetNbinsY()
# Now we want to take the ratio of the numerator to the denominator:
ratio_eff.Divide(ratio_eff, den_eff)
for i in range(1, nbinsX + 1):  # Bins start from 1 in ROOT
    for j in range(1, nbinsY + 1):
        content = ratio_eff.GetBinContent(i, j)

        if content < 0.77:
            ratioVal = 0.77
        elif content > 1.23:
            ratioVal = 1.23
        else:
            ratioVal = 1.0
            
        new_content = ratioVal * den_eff.GetBinContent(i, j) # the eff den. times the lower bound b/c want to change the size of the warp to not be larger than 23% diff
        new_error = ratioVal * den_eff.GetBinError(i, j)
        globalBin = den_eff.GetBin(i, j)
        num_eff.SetBinContent(globalBin, new_content)
        num_eff.SetBinError(globalBin, new_error)
        # We want to repeat this for the warped signal (purity numerator) as well
        new_signalContent = ratioVal * den_signal.GetBinContent(i,j)
        new_signalError = ratioVal * den_signal.GetBinError(i,j)
        num_signal.SetBinContent(globalBin, new_signalContent)
        num_signal.SetBinError(globalBin, new_signalError)

num_eff.Write("h_mc_pZmu_pTmu_num_Modified")
num_signal.Write("signal_purityNum_pZmu_pTmu_num_Modified")
outFile.Close()
