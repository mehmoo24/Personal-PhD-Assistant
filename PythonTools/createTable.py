import sys
import ROOT
import csv
import os

file_input = sys.argv[1]
title = sys.argv[2]
outfile = sys.argv[3]

file = ROOT.TFile.Open(file_input)

data_reco = file.Get("h_data_eqpqp")
mc_reco = file.Get("h_mc_eqpqp")
mc_signal = file.Get("signal_purityNum_eqpqp")

dataPOT = file.Get("DataPOT")
mcPOT = file.Get("MCPOT")

# Scale MC to data POT
mcScale = dataPOT.GetVal() / mcPOT.GetVal()
mc_reco.Scale(mcScale)
mc_signal.Scale(mcScale)

# Extract values
data_val = data_reco.Integral()
mc_reco_val = mc_reco.Integral()
mc_signal_val = mc_signal.Integral()
frac_val = mc_signal_val/mc_reco_val if mc_reco_val != 0 else 0

# Prepare output file
write_header = not os.path.exists(outfile)  # only write header first time

with open(outfile, "a", newline="") as f:
    writer = csv.writer(f)
    if write_header:
        writer.writerow(["Title", "Data Reco", "MC Reco (Data POT Norm.)", 
                         "MC Signal (Data POT Norm.)", "Fraction of Events Signal"])
    writer.writerow([title, f"{data_val:.2f}", f"{mc_reco_val:.2f}", 
                     f"{mc_signal_val:.2f}", f"{frac_val:.2f}"])
