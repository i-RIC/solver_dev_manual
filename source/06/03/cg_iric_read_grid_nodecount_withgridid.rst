cg_iric_read_grid_nodecount_withgridid
===========================================

Reads node count of a grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid_nodecount_withgridid(fid, gid, count, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_NodeCount_WithGridId(fid, gid, &count);

Format (Python)
----------------
.. code-block:: python

   count = cg_iRIC_Read_Grid_NodeCount_WithGridId(fid, gid)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid_nodecount_withgridid
   :file: cg_iric_read_grid_nodecount_withgridid_args.csv
   :header-rows: 1

