cg_iric_write_namedgrid2d_coords_withgridid
=============================================

名前を指定して2次元構造格子を出力する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_namedgrid2d_coords_withgridid(fid, name, nx, ny, x, y, gid, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid2d_Coords_WithGridId(fid, name, nx, ny, x, y, gid);

形式 (Python)
---------------
.. code-block:: python

   gid = cg_iRIC_Write_NamedGrid2d_Coords_WithGridId(fid, name, nx, ny, x, y)

引数
----

.. csv-table:: cg_iric_write_namedgrid2d_coords_withgridid の引数
   :file: cg_iric_write_namedgrid2d_coords_withgridid_args.csv
   :header-rows: 1

