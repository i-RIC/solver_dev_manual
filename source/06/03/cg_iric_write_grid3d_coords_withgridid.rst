cg_iric_write_grid3d_coords_withgridid
=======================================

3次元構造格子を出力する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_grid3d_coords_withgridid(fid, nx, ny, nz, x, y, z, gid, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_Grid3d_Coords_WithGridId(fid, nx, ny, nz, x, y, z, gid);

形式 (Python)
---------------
.. code-block:: python

   gid = cg_iRIC_Write_Grid3d_Coords_WithGridId(fid, nx, ny, nz, x, y, z)

引数
----

.. csv-table:: cg_iric_write_grid3d_coords_withgridid の引数
   :file: cg_iric_write_grid3d_coords_withgridid_args.csv
   :header-rows: 1

