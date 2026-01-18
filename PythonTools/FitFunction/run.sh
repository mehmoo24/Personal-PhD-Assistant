python Generate_histos.py /pnfs/minerva/persistent/users/mmehmood/default_analysis_loc/nuFHC_ME_runAfterThursUpdate_replica/Hists_EventSelection_nuFHC_ME_runAfterThursUpdate_replica_sys_t99_z99_Nu_minervameCombinedPlaylists.root nuFHC_ME

python Generate_histos.py /exp/minerva/data/users/mmehmood/default_anaysis_loc/Dec18/nuFHC_LE_runAfterThursUpdate/Hists_EventSelection_nuFHC_LE_runAfterThursUpdate_sys_t99_z99_Nu_minervaCombinedPlaylists.root nuFHC_LE

python Generate_histos.py /exp/minerva/data/users/mmehmood/default_anaysis_loc/Dec18/antinuRHC_ME_runAfterThursUpdate/Hists_EventSelection_antinuRHC_ME_runAfterThursUpdate_sys_t99_z99_AntiNu_minervameCombinedPlaylists.root antinuRHC_ME

python Generate_histos.py /exp/minerva/data/users/mmehmood/default_anaysis_loc/Nov21_allstats_allsys/LE_antinuRHC_Sample2_SemiCurv/Hists_EventSelection_LE_antinuRHC_Sample2_SemiCurv_minerva5_sys_t99_z99_AntiNu.root antinuRHC_LE

for i in {1..16}; do
   python Plot_histos.py nuFHC_ME.root Fit_pzBin${i} Slice_pzBin${i} nuFHC_ME  ${i}
   python Plot_histos.py nuFHC_LE.root Fit_pzBin${i} Slice_pzBin${i} nuFHC_LE  ${i}
   python Plot_histos.py antinuRHC_ME.root Fit_pzBin${i} Slice_pzBin${i} antinuRHC_ME  ${i}
   python Plot_histos.py antinuRHC_LE.root Fit_pzBin${i} Slice_pzBin${i} antinuRHC_LE  ${i}
done
