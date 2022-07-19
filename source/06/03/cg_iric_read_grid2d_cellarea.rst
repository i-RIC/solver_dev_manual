cg_iric_read_grid2d_cellarea
==============================

格子のセルの面積を計算して返す。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid2d_cellarea(g_handle, cell_id, area, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_CellArea(g_handle, cell_id, &area);

形式 (Python)
---------------
.. code-block:: python

   area = cg_iRIC_Read_Grid2d_CellArea(g_handle, cell_id)

引数
----

.. csv-table:: cg_iric_read_grid2d_cellarea の引数
   :file: cg_iric_read_grid2d_cellarea_args.csv
   :header-rows: 1
