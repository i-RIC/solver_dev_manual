.. _sec_iriclibfunc_cg_iric_read_sol_grid2d_open:

cg_iric_read_sol_grid2d_open
================================

Opens the grid in calculation result.
This function works only with CGNS files that contains calculation result in which
the shape of grids changes on each time steps.

The grid opened with this subroutine can be closed with :ref:`sec_iriclibfunc_cg_iric_read_grid2d_close` .

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_grid2d_open(fid, sol_id, g_handle, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Grid2d_Open(fid, sol_id, &g_handle);

Format (Python)
----------------
.. code-block:: python

   g_handle = cg_iRIC_Read_Sol_Grid2d_Open(fid, sol_id)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_sol_grid2d_open
   :file: cg_iric_read_sol_grid2d_open_args.csv
   :header-rows: 1
