.. _sec_iriclibfunc_cg_iric_read_sol_grid2d_open_withgridid:

cg_iric_read_sol_grid2d_open_withgridid
===========================================

Opens the grid in calculation result.
This function works only with CGNS files that contains calculation result in which
the shape of grids changes on each time steps.

The grid opened with this subroutine can be closed with :ref:`sec_iriclibfunc_cg_iric_read_grid2d_close` .

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_grid2d_open_withgridid(fid, gid, sol_id, g_handle, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Grid2d_Open_WithGridId(fid, gid, sol_id, &g_handle);

Format (Python)
----------------
.. code-block:: python

   g_handle = cg_iRIC_Read_Sol_Grid2d_Open_WithGridId(fid, gid, sol_id)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_sol_grid2d_open_withgridid
   :file: cg_iric_read_sol_grid2d_open_withgridid_args.csv
   :header-rows: 1
