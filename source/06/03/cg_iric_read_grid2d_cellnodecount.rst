cg_iric_read_grid2d_cellnodecount
=====================================

Returns the number of nodes in the specified cell.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid2d_cellnodecount(g_handle, cell_id, count, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_CellNodeCount(g_handle, cell_id, &count);

Format (Python)
----------------
.. code-block:: python

   count = cg_iRIC_Read_Grid2d_CellNodeCount(g_handle, cell_id)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid2d_cellnodecount
   :file: cg_iric_read_grid2d_cellnodecount_args.csv
   :header-rows: 1
