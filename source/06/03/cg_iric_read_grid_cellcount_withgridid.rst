cg_iric_read_grid_cellcount_withgridid
===========================================

格子のセルの数を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid_cellcount_withgridid(fid, gid, count, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_CellCount_WithGridId(fid, gid, &count);

形式 (Python)
---------------
.. code-block:: python

   count = cg_iRIC_Read_Grid_CellCount_WithGridId(fid, gid)

引数
----

.. csv-table:: cg_iric_read_grid_cellcount_withgridid の引数
   :file: cg_iric_read_grid_cellcount_withgridid_args.csv
   :header-rows: 1

