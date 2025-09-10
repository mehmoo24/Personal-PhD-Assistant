The original import expects a Python package path like <something>/python/PlotUtils/LoadPlotUtilsLib.py to be on 
PYTHONPATH, and the shared library libPlotUtils.so to be on LD_LIBRARY_PATH.
	1.	Find the Python shim and the shared lib (examples):

	•	.../PlotUtils/python/PlotUtils/LoadPlotUtilsLib.py
	•	.../PlotUtils/lib/libPlotUtils.so

	2.	Export paths before running:
export PYTHONPATH=/path/to/PlotUtils/python:$PYTHONPATH
export LD_LIBRARY_PATH=/path/to/PlotUtils/lib:$LD_LIBRARY_PATH
python compute_flux.py
If you’re using MINERvA’s MAT checkout, there’s usually a setup.sh/setenv.sh that sets these for you. Source that first.


                                                                                            
SOLUTION: I went into /exp/minerva/app/users/mmehmood/MAT_AL9/opt/lib/python/PlotUtils and there was a file
          vi LoadMATMINERvALib.py that Jeremy Wolcott had actually written:
"The code necessary to load the libplotutils.so library so that PlotUtils C++ objects are available"

                                                                                            
