iric_write_sol_start
======================

-  Inform the GUI that the solver started outputting result

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_start(fid, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Start(fid);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Sol_Start(fid)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_start
   :file: cg_iric_write_sol_start_args.csv
   :header-rows: 1
