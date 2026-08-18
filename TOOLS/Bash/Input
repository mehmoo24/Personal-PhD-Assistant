# Inputs to send: 
#fileName_num_eff = sys.argv[1]
#fileName_num_signal = sys.argv[2]
#fileName_den_eff = sys.argv[3]
#fileName_den_signal = sys.argv[4]
#fileName_output = sys.argv[5]


PWD=/exp/minerva/data/users/mmehmood/default_anaysis_loc/LE_nuFHC/

ORIG_DATA_RECO_FILE=$PWD/MnvTunev1_nuFHC_LE/Hists_EventSelection_MnvTunev1_nuFHC_LE_sys_t99_z99_Nu_minervaCombinedPlaylists.root
ORIG_DATA_TRUTH_FILE=$PWD/MnvTunev1_nuFHC_LE/Hists_Efficiency_MnvTunev1_nuFHC_LE_sys_t99_z99_Nu_minervaCombinedPlaylists.root

LOWQ2PION_DATA_RECO_FILE=$PWD/LE_nuFHC_warp_lowQ2PionTuneOn_noMinosMatch_yesMuonCurve/Hists_EventSelection_LE_nuFHC_warp_lowQ2PionTuneOn_noMinosMatch_yesMuonCurve_sys_t99_z99_Nu_minervaCombinedPlaylists.root
LOWQ2PION_DATA_TRUTH_FILE=$PWD/LE_nuFHC_warp_lowQ2PionTuneOn_noMinosMatch_yesMuonCurve/Hists_Efficiency_LE_nuFHC_warp_lowQ2PionTuneOn_noMinosMatch_yesMuonCurve_sys_t99_z99_Nu_minervaCombinedPlaylists.root


python modifyWarps.py  "${LOWQ2PION_DATA_TRUTH_FILE}" "${LOWQ2PION_DATA_RECO_FILE}" "${ORIG_DATA_TRUTH_FILE}" "${LOWQ2PION_DATA_RECO_FILE}"  lowQ2PionTune
