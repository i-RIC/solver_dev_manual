cg_iric_read_sol_grid3d_coords
================================

計算結果の3次元構造格子を取得する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_grid3d_coords(fid, step, x, y, z, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Grid3d_Coords(fid, step, x, y, z);

形式 (Python)
---------------
.. code-block:: python

   x, y, z = cg_iRIC_Read_Sol_Grid3d_Coords(fid, step)

引数
----

.. csv-table:: cg_iric_read_sol_grid3d_coords の引数
   :file: cg_iric_read_sol_grid3d_coords_args.csv
   :header-rows: 1

