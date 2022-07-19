cg_iric_read_grid2d_interpolatewithcell
============================================

Returns the information to interpolate the value at the specified coordinates, with the values defined at grid nodes.

You can use this function when you already know which cell contains the coordinates.
If not please use :ref:`sec_iriclibfunc_cg_iric_read_grid2d_interpolate` instead.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid2d_interpolatewithcell(g_handle, x, y, cellid, nodeids_arr, weights_arr, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_InterpolateWithCell(g_handle, x, y, cellid, nodeids_arr, weights_arr);

Format (Python)
----------------
.. code-block:: python

   nodeids_arr, weights_arr = cg_iRIC_Read_Grid2d_InterpolateWithCell(g_handle, x, y, cellid)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid2d_interpolatewithcell
   :file: cg_iric_read_grid2d_interpolatewithcell_args.csv
   :header-rows: 1
