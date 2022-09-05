cg_iric_read_grid_real_node_withgridid
========================================

Reads the double-precision real-type attribute values defined at nodes of a grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid_real_node_withgridid(fid, gid, label, values, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_Real_Node_WithGridId(fid, gid, label, values);

Format (Python)
----------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_Real_Node_WithGridId(fid, gid, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_grid_real_node_withgridid
   :file: cg_iric_read_grid_real_node_withgridid_args.csv
   :header-rows: 1

