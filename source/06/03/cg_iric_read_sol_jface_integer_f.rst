cg_iric_read_sol_jface_integer_f
================================

-  Reads the integer-type calculation result, having a value for each grid edge at j-direction.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_jface_integer_f(step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_JFace_Integer(step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_JFace_Integer(step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_jface_integer_f
   :file: cg_iric_read_sol_jface_integer_f_args.csv
   :header-rows: 1
