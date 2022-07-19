cg_iric_read_complex_functionalwithname
=========================================

Reads f_functional attribute of complex type grid attribute with name.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_complex_functionalwithname(fid, type, num, name, paramname, data, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Complex_functionalWithName(fid, type, num, name, paramname, data);

Format (Python)
----------------
.. code-block:: python

   data = cg_iRIC_Read_Complex_functionalWithName(fid, type, num, name, paramname)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_complex_functionalwithname
   :file: cg_iric_read_complex_functionalwithname_args.csv
   :header-rows: 1

