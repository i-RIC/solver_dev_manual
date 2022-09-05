cg_iric_write_sol_node_real_withgridid
=======================================

Outputs double-precision real-type calculation results defined at grid nodes.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_node_real_withgridid(fid, gid, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Node_Real_WithGridId(fid, gid, label, val);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Sol_Node_Real_WithGridId(fid, gid, label, val)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_node_real_withgridid
   :file: cg_iric_write_sol_node_real_withgridid_args.csv
   :header-rows: 1
