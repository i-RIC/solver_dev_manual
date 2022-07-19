cg_iric_read_grid2d_findcell
==============================

指定した座標を含むセルのIDを返す。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid2d_findcell(g_handle, x, y, cell_id, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_FindCell(g_handle, x, y, &cell_id);

形式 (Python)
---------------
.. code-block:: python

   cell_id = cg_iRIC_Read_Grid2d_FindCell(g_handle, x, y)

引数
----

.. csv-table:: cg_iric_read_grid2d_findcell の引数
   :file: cg_iric_read_grid2d_findcell_args.csv
   :header-rows: 1
