cg_iric_write_sol_end
=========================

Inform the GUI that the solver finished outputting result.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_end(fid, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_End(fid);

Format (Python)
----------------
.. code-block:: c

   cg_iRIC_Write_Sol_End(fid)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_end
   :file: cg_iric_write_sol_end_args.csv
   :header-rows: 1
