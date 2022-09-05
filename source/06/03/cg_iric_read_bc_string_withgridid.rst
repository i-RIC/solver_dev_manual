cg_iric_read_bc_string_withgridid
===================================

Reads the value of a string-type variable defined at the boundary condition.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_bc_string_withgridid(fid, gid, type, num, label, strvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_String_WithGridId(fid, gid, type, num, name, value);

Format (Python)
----------------
.. code-block:: python

   value = cg_iRIC_Read_BC_String_WithGridId(fid, gid, type, num, name)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_string_withgridid
   :file: cg_iric_read_bc_string_withgridid_args.csv
   :header-rows: 1

