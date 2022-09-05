cg_iric_write_namedgrid3d_coords_withgridid
==============================================

名前を指定して3次元構造格子を出力する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_namedgrid3d_coords_withgridid(fid, name, nx, ny, nz, x, y, z, gid, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid3d_Coords_WithGridId(fid, name, nx, ny, nz, x, y, z);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_Write_NamedGrid3d_Coords_WithGridId(fid, name, nx, ny, nz, x, y, z)

引数
----

.. csv-table:: cg_iric_write_namedgrid3d_coords_withgridid の引数
   :file: cg_iric_write_namedgrid3d_coords_withgridid_args.csv
   :header-rows: 1

