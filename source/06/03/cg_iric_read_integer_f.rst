cg_iric_read_integer_f
======================

-  Reads the value of a integer-type variable from the CGNS file.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_integer_f(label, intvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Integer(label, &intvalue);

Format (Python)
----------------
.. code-block:: python

   intvalue = cg_iRIC_Read_Integer(label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_integer_f
   :file: cg_iric_read_integer_f_args.csv
   :header-rows: 1

