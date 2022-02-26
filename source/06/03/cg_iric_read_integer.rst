cg_iric_read_integer
======================

-  Reads the value of a integer-type variable from the CGNS file.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_integer(fid, label, intvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Integer(fid, label, &intvalue);

Format (Python)
----------------
.. code-block:: python

   intvalue = cg_iRIC_Read_Integer(fid, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_integer
   :file: cg_iric_read_integer_args.csv
   :header-rows: 1

