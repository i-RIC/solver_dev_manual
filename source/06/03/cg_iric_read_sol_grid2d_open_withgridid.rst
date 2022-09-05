.. _sec_iriclibfunc_cg_iric_read_sol_grid2d_open_withgridid:

cg_iric_read_sol_grid2d_open_withgridid
===========================================

計算結果の格子を開く。時間に依存して格子の形状が変換する計算結果を含むCGNSファイルでのみ使用できる。

この関数で開いた格子は、 :ref:`sec_iriclibfunc_cg_iric_read_grid2d_close` を使用して閉じる。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_grid2d_open_withgridid(fid, gid, sol_id, g_handle, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Grid2d_Open_WithGridId(fid, gid, sol_id, &g_handle);

形式 (Python)
---------------
.. code-block:: python

   g_handle = cg_iRIC_Read_Sol_Grid2d_Open_WithGridId(fid, gid, sol_id)

引数
----

.. csv-table:: cg_iric_read_sol_grid2d_open_withgridid の引数
   :file: cg_iric_read_sol_grid2d_open_withgridid_args.csv
   :header-rows: 1
