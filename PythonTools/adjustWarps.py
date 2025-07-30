# We want to rewrite the warps so that the warped / origEffNum ratio is between 0.77 and 1.23 in every bin since that is the size of the largest data/mc discrepancy for nuFHC LE

from ROOT import TFile, MnvH2D
import os

def clamp_ratio(num_hist, den_hist, min_ratio=0.77, max_ratio=1.23):
    clamped_num = num_hist.Clone(num_hist.GetName() + "_clamped")
    clamped_num.SetTitle(num_hist.GetTitle() + " (Clamped)")

    nbins_x = num_hist.GetNbinsX()
    nbins_y = num_hist.GetNbinsY()

    for x in range(1, nbins_x + 1):
        for y in range(1, nbins_y + 1):
            num_val = num_hist.GetBinContent(x, y)
            den_val = den_hist.GetBinContent(x, y)
            if den_val == 0:
                continue

            ratio = num_val / den_val
            if ratio < min_ratio:
                new_val = min_ratio * den_val
                new_err = min_ratio * den_hist.GetBinError(x, y)
                clamped_num.SetBinContent(x, y, new_val)
                clamped_num.SetBinError(x, y, new_err)
            elif ratio > max_ratio:
                new_val = max_ratio * den_val
                new_err = max_ratio * den_hist.GetBinError(x, y)
                clamped_num.SetBinContent(x, y, new_val)
                clamped_num.SetBinError(x, y, new_err)
            # else keep original value
    return clamped_num

# === CONFIGURATION ===
den_file_path = "/exp/minerva/data/users/mmehmood/default_anaysis_loc/LE_nuFHC/MnvTunev1_nuFHC_LE/Hists_Efficiency_MnvTunev1_nuFHC_LE_sys_t99_z99_Nu_minervaCombinedPlaylists.root"
den_hist_name = "h_mc_pZmu_pTmu"

numerator_files = {
    "/exp/minerva/data/users/mmehmood/default_anaysis_loc/LE_nuFHC/LE_nuFHC_warp_lowQ2PionTuneOn_noMinosMatch_yesMuonCurve/Hists_Efficiency_LE_nuFHC_warp_lowQ2PionTuneOn_noMinosMatch_yesMuonCurve_sys_t99_z99_Nu_minervaCombinedPlaylists.root": "h_mc_pZmu_pTmu",
    "/exp/minerva/data/users/mmehmood/default_anaysis_loc/LE_nuFHC/LE_nuFHC_warp_nonresOff_noMinosMatch_yesMuonCurve/Hists_Efficiency_LE_nuFHC_warp_nonresOff_noMinosMatch_yesMuonCurve_sys_t99_z99_Nu_minervaCombinedPlaylists.root": "h_mc_pZmu_pTmu",
    "/exp/minerva/data/users/mmehmood/default_anaysis_loc/LE_nuFHC/LE_nuFHC_warp_rpaOff_noMinosMatch_yesMuonCurve/Hists_Efficiency_LE_nuFHC_warp_rpaOff_noMinosMatch_yesMuonCurve_sys_t99_z99_Nu_minervaCombinedPlaylists.root": "h_mc_pZmu_pTmu",
}

# === LOAD DENOMINATOR ===
f_den = TFile.Open(den_file_path)
den_hist = f_den.Get(den_hist_name)

# === PROCESS EACH NUMERATOR ===
for num_file_path, num_hist_name in numerator_files.items():
    f_num = TFile.Open(num_file_path)
    num_hist = f_num.Get(num_hist_name)

    clamped = clamp_ratio(num_hist, den_hist)

    # Clone original for writing
    num_original = num_hist.Clone(num_hist.GetName() + "_original")
    den_clone = den_hist.Clone(den_hist.GetName() + "_copy")

    # Output file
    base = os.path.basename(num_file_path).replace(".root", "")
    out_file = TFile.Open(f"{base}_clamped_output.root", "RECREATE")
    num_original.Write()
    den_clone.Write()
    clamped.Write()
    out_file.Close()

    f_num.Close()

f_den.Close()
