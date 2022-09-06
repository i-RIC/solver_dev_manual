.. _iriclib_output_result_for_multiple_grid:

Outputting calculation results for multiple grids
====================================================

iRIClib supports function to output calculation results for multiple grids.

Typical examples of the usage is as follows:

* Output calculation result for both two dimensional and three dimensional grids
* Output calculation result for both unstructured and structured grids

In such cases, please use the functions with "_withgridid" suffix.

For example, when you want to output calculation results for both two dimensional and three dimensional grids, use :ref:`sec_iriclibfunc_cg_iric_write_grid3d_coords_withgridid`
to output three dimensional grid:

The arguments of 
:ref:`sec_iriclibfunc_cg_iric_write_grid3d_coords` and 
:ref:`sec_iriclibfunc_cg_iric_write_grid3d_coords_withgridid` differs like below
(in case of FORTRAN). with the function with "_withgridid",
argument gid (that means "Grid ID") is added.

.. code-block:: fortran

   call cg_iric_write_grid3d_coords(fid, nx, ny, nz, x, y, z, ier)

.. code-block:: fortran

   call cg_iric_write_grid3d_coords_withgridid(fid, nx, ny, nz, x, y, z, gid, ier)

:ref:`sec_iriclibfunc_cg_iric_write_grid3d_coords_withgridid` 
write the grid to CGNS file, and returns the ID of the new grid.

When you want to output calculation result for multiple grids, please use 
the functions with "_withgridid".

For example, to output calculation result defined at nodes with real values, use
:ref:`sec_iriclibfunc_cg_iric_write_sol_node_real_withgridid`.

The arguments of :ref:`sec_iriclibfunc_cg_iric_write_sol_node_real_withgridid` is shown below.

.. code-block:: fortran

   call cg_iric_write_sol_node_real_withgridid(fid, gid, label, val, ier)

Pass the value of grid id as the second argument gid.

THe important point is that gid is 1 for the two dimensional grid that is created by the user
on iRIC GUI, and 2 for three dimensional grid that is created by solver and written
with the function above. By passing the appropriate gid, you can output 
calculation result for both grids.

For all functions that is related to grids, the version with "_withgridid" suffix exists, just like
:ref:`sec_iriclibfunc_cg_iric_write_sol_node_real`.
