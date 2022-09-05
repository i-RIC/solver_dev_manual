.. _iriclib_output_result_for_multiple_grid:

Outputting calculation results for multiple grids
====================================================

iRIClib supports function to output calculation results for multiple grids.

Typical examples of the usage is as follows:

* Output calculation result for both two dimensional and three dimensional grids
* Output calculation result for both unstructured and structured grids

In such cases, please use the functions with "_WithGridId" suffix.

For example, when you want to output calculation results for both two dimensional and three dimensional grids,
use the function below to output three dimensional grid:

* cg_iric_grid3d_coords_withgridid

This function write the grid to CGNS file, and returns the ID of the new grid.

And, to output calculation results, use functions with "_WithGridId" suffix also.

For example, to output calculation result defined at nodes with real values, use
cg_iric_write_sol_node_real_withgridid.

Please note that gridid is 1 for two dimensional grid that is created and output 
using iRIC GUI, and 2 for three dimensional grid that is created by solver and written
with the function above. By passing the appropriate gridid, you can output 
calculation result for both grids.

For all functions that is related to grids, the version with "_WithGridId" suffix exists.
