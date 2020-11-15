cg_iric_read_sol_real_f
=======================

-  Reads the double-precision real-type calculation result, having a value for each grid node.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_real_f(step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Real(step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_Real(step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_real_f
   :file: cg_iric_read_sol_real_f_args.csv
   :header-rows: 1

