cg_iric_read_complex_real_withgridid
======================================

Reads the double precision attribute values of complex type grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_complex_real_withgridid(fid, gid, type, num, name, value, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Complex_Real_WithGridId(fid, gid, type, num, name, &value);

Format (Python)
----------------
.. code-block:: python

   value = cg_iRIC_Read_Complex_Real_WithGridId(fid, gid, type, num, name)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_complex_real_withgridid
   :file: cg_iric_read_complex_real_withgridid_args.csv
   :header-rows: 1

