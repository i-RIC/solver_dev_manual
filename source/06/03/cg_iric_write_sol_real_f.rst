cg_iric_write_sol_real_f
========================

-  Outputs double-precision real-type calculation results, having a value for each grid node.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_real_f(label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Real(label, val);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Sol_Real(label, val)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_real_f
   :file: cg_iric_write_sol_real_f_args.csv
   :header-rows: 1
