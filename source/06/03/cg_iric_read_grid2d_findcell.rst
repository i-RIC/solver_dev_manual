cg_iric_read_grid2d_findcell
==============================

Finds and returns the ID of the cell that includes the specified coordinates.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid2d_findcell(g_handle, x, y, cell_id, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_FindCell(g_handle, x, y, &cell_id);

Format (Python)
----------------
.. code-block:: python

   cell_id = cg_iRIC_Read_Grid2d_FindCell(g_handle, x, y)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid2d_findcell
   :file: cg_iric_read_grid2d_findcell_args.csv
   :header-rows: 1
