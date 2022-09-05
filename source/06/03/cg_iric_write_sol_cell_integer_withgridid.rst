cg_iric_write_sol_cell_integer_withgridid
===========================================

Outputs integer-type calculation results, giving a value for each grid cell.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_cell_integer_withgridid(fid, gid, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Cell_Integer_WithGridId(fid, gid, label, val);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Sol_Cell_Integer_WithGridId(fid, gid, label, val)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_cell_integer_withgridid
   :file: cg_iric_write_sol_cell_integer_withgridid_args.csv
   :header-rows: 1

