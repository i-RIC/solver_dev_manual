cg_iric_read_sol_iteration
============================

Reads the loop iteration value.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_iteration(fid, step, iteration, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Iteration(fid, step, &iteration);

Format (Python)
----------------
.. code-block:: python

   iteration = cg_iRIC_Read_Sol_Iteration(fid, step)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_iteration
   :file: cg_iric_read_sol_iteration_args.csv
   :header-rows: 1
