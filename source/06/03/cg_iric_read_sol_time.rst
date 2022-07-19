cg_iric_read_sol_time
=======================

Reads the time value

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_time(fid, step, time, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Time(fid, step, &time);

Format (Python)
----------------
.. code-block:: python

   time = cg_iRIC_Read_Sol_Time(fid, step)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_time
   :file: cg_iric_read_sol_time_args.csv
   :header-rows: 1

