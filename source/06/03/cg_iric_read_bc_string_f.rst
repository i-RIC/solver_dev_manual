cg_iric_read_bc_string_f
========================

-  Reads the value of a string-type variable from the CGNS file.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_bc_string_f(type, num, label, strvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_String(type, num, name, value);

Format (Python)
----------------
.. code-block:: python

   value = cg_iRIC_Read_BC_String(type, num, name)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_string_f
   :file: cg_iric_read_bc_string_f_args.csv
   :header-rows: 1

