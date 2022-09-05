cg_iric_write_sol_cell_real_withgridid
========================================

Outputs double-precision real-type calculation results, having a value for each grid cell.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_cell_real_withgridid(fid, gid, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Cell_Real_WithGridId(fid, gid, label, val);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Sol_Cell_Real_WithGridId(fid, gid, label, val)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_cell_real_withgridid
   :file: cg_iric_write_sol_cell_real_withgridid_args.csv
   :header-rows: 1

