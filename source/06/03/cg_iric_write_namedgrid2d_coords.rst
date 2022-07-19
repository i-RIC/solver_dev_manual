cg_iric_write_namedgrid2d_coords
==================================

名前を指定して2次元構造格子を出力する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_namedgrid2d_coords(fid, name, nx, ny, x, y, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid2d_Coords(fid, name, nx, ny, x, y);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_Write_NamedGrid2d_Coords(fid, name, nx, ny, x, y)

引数
----

.. csv-table:: cg_iric_write_namedgrid2d_coords の引数
   :file: cg_iric_write_namedgrid2d_coords_args.csv
   :header-rows: 1

