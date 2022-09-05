cg_iric_read_sol_node_real_withgridid
=======================================

Reads the double-precision real-type calculation result defined at grid nodes.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_node_real_withgridid(fid, gid, step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Node_Real_WithGridId(fid, gid, step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_Node_Real_WithGridId(fid, gid, step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_node_real_withgridid
   :file: cg_iric_read_sol_node_real_withgridid_args.csv
   :header-rows: 1

