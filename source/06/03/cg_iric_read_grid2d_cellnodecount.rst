cg_iric_read_grid2d_cellnodecount
=====================================

指定したセルを構成する頂点の数を返す。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid2d_cellnodecount(g_handle, cell_id, count, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_CellNodeCount(g_handle, cell_id, &count);

形式 (Python)
---------------
.. code-block:: python

   count = cg_iRIC_Read_Grid2d_CellNodeCount(g_handle, cell_id)

引数
----

.. csv-table:: cg_iric_read_grid2d_cellnodecount の引数
   :file: cg_iric_read_grid2d_cellnodecount_args.csv
   :header-rows: 1
