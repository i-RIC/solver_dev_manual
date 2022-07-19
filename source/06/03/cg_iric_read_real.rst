cg_iric_read_real
===================

Reads the value of a double-precision real-type variable from the CGNS file.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_real(fid, label, realvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Real(fid, label, &realvalue);

Format (Python)
----------------
.. code-block:: python

   realvalue = cg_iRIC_Read_Real(fid, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_real
   :file: cg_iric_read_real_args.csv
   :header-rows: 1

