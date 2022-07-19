cg_iric_read_sol_cell_real
============================

Reads the double-precision real-type calculation result defined at grid cells.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_cell_real(fid, step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Cell_Real(fid, step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_Cell_Real(fid, step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_cell_real
   :file: cg_iric_read_sol_cell_real_args.csv
   :header-rows: 1

