cg_iric_write_sol_node_real
============================

-  Outputs double-precision real-type calculation results, having a value for each grid node.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_node_real(fid, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Node_Real(fid, label, val);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Sol_Node_Real(fid, label, val)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_node_real
   :file: cg_iric_write_sol_node_real_args.csv
   :header-rows: 1
