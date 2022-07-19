cg_iric_read_grid_integer_node
================================

Reads the integer attribute values defined at nodes of a grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid_integer_node(fid, label, values, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_Integer_Node(fid, label, values);

Format (Python)
----------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_Integer_Node(fid, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_grid_integer_node
   :file: cg_iric_read_grid_integer_node_args.csv
   :header-rows: 1

