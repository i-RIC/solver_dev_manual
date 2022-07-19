cg_iric_read_grid2d_interpolatewithcell
============================================

指定した位置での値を、格子での値を使って補間して計算するための情報を返す。

指定した位置が含まれるセルのIDがわかっている場合はこの関数を使用する。
分かっていない場合は :ref:`sec_iriclibfunc_cg_iric_read_grid2d_interpolate` を使用する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid2d_interpolatewithcell(g_handle, x, y, cellid, nodeids_arr, weights_arr, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_InterpolateWithCell(g_handle, x, y, cellid, nodeids_arr, weights_arr);

形式 (Python)
---------------
.. code-block:: python

   nodeids_arr, weights_arr = cg_iRIC_Read_Grid2d_InterpolateWithCell(g_handle, x, y, cellid)

引数
----

.. csv-table:: cg_iric_read_grid2d_interpolatewithcell の引数
   :file: cg_iric_read_grid2d_interpolatewithcell_args.csv
   :header-rows: 1
