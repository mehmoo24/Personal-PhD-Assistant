nuFHC_pdg=14
nuFHC_lep_pdg=13
antinuRHC_pdg=-14
antinuRHC_lep_pdg=-13
run_lownu=1 # 0 is false, 1 is true

# explicit list of input files
files_nuFHC_ME=(
	"/pnfs/minerva/persistent/Models/NEUT/Medium_Energy/FHC/v5.4.1/tracker/SF_ma103/tracker/mnv.nu.flat.SF.neut.103.root"
	"/pnfs/minerva/persistent/Models/NEUT/Medium_Energy/FHC/v5.4.1/tracker/LFG_ma105/tracker/mnv.nu.flat.LFG.neut.105.root"
	"/pnfs/minerva/persistent/Models/GENIE/Medium_Energy/FHC/v3_0_6/tracker/G18_02a_02_11a/CH/flat_GENIE_G18_02a_02_11a_50M.root"
	"/pnfs/minerva/persistent/Models/GENIE/Medium_Energy/FHC/v3_0_6/tracker/G18_02b_02_11a/CH/flat_GENIE_G18_02b_02_11a_50Mcombined.root"
	"/pnfs/minerva/persistent/Models/GENIE/Medium_Energy/FHC/v3_0_6/tracker/G18_10a_02_11a/CH/flat_GENIE_G18_10a_02_11a_50M.root"
	"/pnfs/minerva/persistent/Models/GENIE/Medium_Energy/FHC/v3_0_6/tracker/G18_10b_02_11a/CH/flat_GENIE_G18_10b_02_11a_50M.root"
	"/pnfs/minerva/persistent/Models/NuWro/Medium_Energy/FHC/v2109/tracker/SF/flat_NuWro_CH_SF_50M.root"
	"/pnfs/minerva/persistent/Models/NuWro/Medium_Energy/FHC/v2109/tracker/LFG/flat_NuWro_CH_LFG_50M.root"
)

# Loop over each file
for infile in "${files_nuFHC_ME[@]}"; do
    # Strip extension for a base name
    base=$(basename "$infile" .root)

    # Define output file name (customize as you like)
    if [ "$run_lownu" -eq 1 ]; then
	    outfile="${base}_LownuFluxParam_nuFHC_ME.root"
    else
	    outfile="${base}_noLownuFluxParam_nuFHC_ME.root"
    fi
    echo "Processing $infile -> $outfile"

    # Call your Python script with input + output
    python GenerateModelPrediction.py "$nuFHC_pdg" "$nuFHC_lep_pdg" "$infile" "$outfile" $run_lownu
done

files_nuFHC_LE=(
	"/exp/minerva/data/users/drut1186/Model_Temp_Store/NEUT/Low_Energy/SF/flat_NEUT_tune_SF_maqe1.03_50M.root"
	"/exp/minerva/data/users/drut1186/Model_Temp_Store/NEUT/Low_Energy/LFG/flat_NEUT_tune_LFG_maqe1.05_50M.root"
	"/pnfs/minerva/persistent/Models/GENIE/Low_Energy/FHC/v3_0_6/tracker/G18_02a_02_11a/GENIE_LE_FHC_50M_G18_02a_02_11a.root"
	"/pnfs/minerva/persistent/Models/GENIE/Low_Energy/FHC/v3_0_6/tracker/G18_02b_02_11a/GENIE_LE_FHC_50M_G18_02b_02_11a.root"
	"/pnfs/minerva/persistent/Models/GENIE/Low_Energy/FHC/v3_0_6/tracker/G18_10a_02_11a/GENIE_LE_FHC_50M_G18_10a_02_11a.root"
	"/pnfs/minerva/persistent/Models/GENIE/Low_Energy/FHC/v3_0_6/tracker/G18_10b_02_11a/GENIE_LE_FHC_50M_G18_10b_02_11a.root"
	"/exp/minerva/data/users/drut1186/Model_Temp_Store/NuWro/Low_Energy/FHC/v2109/tracker/SF/nuwro_new_SF_LE.root"
	"/exp/minerva/data/users/drut1186/Model_Temp_Store/NuWro/Low_Energy/FHC/v2109/tracker/LFG/nuwro_new_LFG_LE.root"
)

for infile in "${files_nuFHC_LE[@]}"; do
    # Strip extension for a base name
    base=$(basename "$infile" .root)

    outfile="${base}_noLownuFluxParam_nuFHC_LE.root"
    echo "Processing $infile -> $outfile"

    # Call your Python script with input + output
    python GenerateModelPrediction.py "$nuFHC_pdg" "$nuFHC_lep_pdg" "$infile" "$outfile" 0 # 0 is for false, 1 is for true
done

files_antinuRHC_ME=(
	"/pnfs/minerva/persistent/Models/NEUT/Medium_Energy/RHC/v5.4.1/tracker/SF_ma103/tracker/flat_NEUT_tune_SF_maqe105_50M.root"
	"/pnfs/minerva/persistent/Models/NEUT/Medium_Energy/RHC/v5.4.1/tracker/LFG_ma105/tracker/flat_NEUT_tune_LFG_maqe1.05_50M.root"
	"/pnfs/minerva/persistent/Models/GENIE/Medium_Energy/RHC/v3_0_6/tracker/G18_02a_02_11a/tracker/flat_GENIE_1000k_tune_G18_02a_02_11a_50MCombined_RHC.root"
	"/pnfs/minerva/persistent/Models/GENIE/Medium_Energy/RHC/v3_0_6/tracker/G18_02b_02_11a/tracker/flat_GENIE_1000k_tune_G18_02b_02_11a_50Mcombined.root"
	"/pnfs/minerva/persistent/Models/GENIE/Medium_Energy/RHC/v3_0_6/tracker/G18_10a_02_11a/tracker/flat_GENIE_1000k_tune_G18_10a_02_11a_50Mcombined_rhc.root"
	"/pnfs/minerva/persistent/Models/GENIE/Medium_Energy/RHC/v3_0_6/tracker/G18_10b_02_11a/tracker/flat_GENIE_1000k_tune_G18_10b_02_11a_50Mcombined_rhc.root"
	"/pnfs/minerva/persistent/Models/NuWro/Medium_Energy/RHC/v2109/tracker/SF/flat_NuWro_CH_SF_50M.root"
	"/pnfs/minerva/persistent/Models/NuWro/Medium_Energy/RHC/v2109/tracker/LFG/flat_NuWro_CH_LFG_50M.root"
)

for infile in "${files_antinuRHC_ME[@]}"; do
    # Strip extension for a base name
    base=$(basename "$infile" .root)

    # Define output file name (customize as you like)
    if [ "$run_lownu" -eq 1 ]; then
            outfile="${base}_LownuFluxParam_antinuRHC_ME.root"
    else
            outfile="${base}_noLownuFluxParam_antinuRHC_ME.root"
    fi
    echo "Processing $infile -> $outfile"

    # Call your Python script with input + output
    python GenerateModelPrediction.py "$antinuRHC_pdg" "$antinuRHC_lep_pdg" "$infile" "$outfile" $run_lownu
done
