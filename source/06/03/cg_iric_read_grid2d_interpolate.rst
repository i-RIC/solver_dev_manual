.. _sec_iriclibfunc_cg_iric_read_grid2d_interpolate:

cg_iric_read_grid2d_interpolate
====================================

指定した位置での値を、格子での値を使って補間して計算するための情報を返す。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid2d_interpolate(g_handle, x, y, ok, count, nodeids_arr, weights_arr, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Interpolate(g_handle, x, y, ok, count, nodeids_arr, weights_arr);

形式 (Python)
---------------
.. code-block:: python

   ok, count, nodeids_arr, weights_arr = cg_iRIC_Read_Grid2d_Interpolate(g_handle, x, y)

引数
----

.. csv-table:: cg_iric_read_grid2d_interpolate の引数
   :file: cg_iric_read_grid2d_interpolate_args.csv
   :header-rows: 1
