cg_iric_read_sol_integer
==========================

-  Reads the integer-type calculation result, having a value for each grid node.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_integer(fid, step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Integer(fid, step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_Integer(fid, step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_integer
   :file: cg_iric_read_sol_integer_args.csv
   :header-rows: 1
