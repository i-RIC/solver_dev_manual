.. _sec_iriclibfunc_cg_iric_read_grid_cellcount_withgridid:

cg_iric_read_grid_cellcount_withgridid
===========================================

Reads cell count of a grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid_cellcount_withgridid(fid, gid, count, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_CellCount_WithGridId(fid, gid, &count);

Format (Python)
----------------
.. code-block:: python

   count = cg_iRIC_Read_Grid_CellCount_WithGridId(fid, gid)

Arguments
---------

.. csv-table:: cg_iric_read_grid_cellcount_withgridid の引数
   :file: cg_iric_read_grid_cellcount_withgridid_args.csv
   :header-rows: 1

