cg_iric_read_grid_complex_node_withgridid
===========================================

Reads the complex attribute values defined for grid nodes.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid_complex_node_withgridid(fid, gid, label, values, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_Complex_Node_WithGridId(fid, gid, label, values);

Format (Python)
----------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_Complex_Node_WithGridId(fid, gid, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_grid_complex_node_withgridid
   :file: cg_iric_read_grid_complex_node_withgridid_args.csv
   :header-rows: 1

