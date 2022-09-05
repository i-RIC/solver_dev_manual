cg_iric_read_sol_node_integer_withgridid
===========================================

Reads the integer-type calculation result defined at grid nodes.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_node_integer_withgridid(fid, gid, step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Node_Integer_WithGridId(fid, gid, step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_Node_Integer_WithGridId(fid, gid, step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_node_integer_withgridid
   :file: cg_iric_read_sol_node_integer_withgridid_args.csv
   :header-rows: 1
