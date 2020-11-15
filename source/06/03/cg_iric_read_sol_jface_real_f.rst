cg_iric_read_sol_jface_real_f
================================

-  Reads the double-precision real-type calculation result, having a value for each grid edge at j-direction.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_jface_real_f(step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_JFace_Real(step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_JFace_Real(step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_jface_real_f
   :file: cg_iric_read_sol_jface_real_f_args.csv
   :header-rows: 1
