cg_iric_write_namedgrid1d_coords
=====================================

名前を指定して1次元構造格子を出力する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_namedgrid1d_coords(fid, name, nx, x, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid1d_Coords(fid, name, nx, x);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_Write_NamedGrid1d_Coords(fid, name, nx, x)

引数
----

.. csv-table:: cg_iric_write_namedgrid1d_coords の引数
   :file: cg_iric_write_namedgrid1d_coords_args.csv
   :header-rows: 1

