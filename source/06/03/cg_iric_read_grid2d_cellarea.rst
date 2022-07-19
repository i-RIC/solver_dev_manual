cg_iric_read_grid2d_cellarea
==============================

Calculates and returns the area of a cell in the grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid2d_cellarea(g_handle, cell_id, area, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_CellArea(g_handle, cell_id, &area);

Format (Python)
----------------
.. code-block:: python

   area = cg_iRIC_Read_Grid2d_CellArea(g_handle, cell_id)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid2d_cellarea
   :file: cg_iric_read_grid2d_cellarea_args.csv
   :header-rows: 1
