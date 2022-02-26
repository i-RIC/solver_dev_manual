cg_iric_read_string
=====================

-  Reads the value of a string-type variable from the CGNS file.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_string(label, strvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_String(label, strvalue);

Format (Python)
----------------
.. code-block:: python

   strvalue = cg_iRIC_Read_String(label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_string
   :file: cg_iric_read_string_args.csv
   :header-rows: 1

