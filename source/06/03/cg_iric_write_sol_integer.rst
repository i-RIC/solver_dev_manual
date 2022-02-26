cg_iric_write_sol_integer
===========================

-  Outputs integer-type calculation results, giving a value for each grid node.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_integer(fid, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Integer(fid, label, val);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Sol_Integer(fid, label, val)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_integer
   :file: cg_iric_write_sol_integer_args.csv
   :header-rows: 1

