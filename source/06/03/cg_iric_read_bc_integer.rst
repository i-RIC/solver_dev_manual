cg_iric_read_bc_integer
=========================

-  Reads the value of a string-type variable from the CGNS file.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_integer(type, num, label, intvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_Integer(type, num, name, &value);

Format (Python)
----------------
.. code-block:: python

   value = cg_iRIC_Read_BC_Integer(type, num, name)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_integer
   :file: cg_iric_read_bc_integer_args.csv
   :header-rows: 1

