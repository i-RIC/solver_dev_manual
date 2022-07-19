.. _sec_iriclibfunc_cg_iric_read_grid2d_interpolate:

cg_iric_read_grid2d_interpolate
====================================

Returns the information to interpolate the value at the specified coordinates, with the values defined at grid nodes.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid2d_interpolate(g_handle, x, y, ok, count, nodeids_arr, weights_arr, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Interpolate(g_handle, x, y, ok, count, nodeids_arr, weights_arr);

Format (Python)
----------------
.. code-block:: python

   ok, count, nodeids_arr, weights_arr = cg_iRIC_Read_Grid2d_Interpolate(g_handle, x, y)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid2d_interpolate
   :file: cg_iric_read_grid2d_interpolate_args.csv
   :header-rows: 1
