cg_iric_read_sol_node_integer
================================

Reads the integer-type calculation result defined at grid nodes.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_node_integer(fid, step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Node_Integer(fid, step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_Node_Integer(fid, step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_node_integer
   :file: cg_iric_read_sol_node_integer_args.csv
   :header-rows: 1
