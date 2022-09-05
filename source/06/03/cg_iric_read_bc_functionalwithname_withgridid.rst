cg_iric_read_bc_functionalwithname_withgridid
===============================================

Reads the value of a f_functional-type real variable from the CGNS.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_bc_functionalwithname_withgridid(fid, gid, type, num, label, name, data, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_functionalWithName_WithGridId(fid, gid, type, num, name, paramname, data);

Format (Python)
----------------
.. code-block:: python

   data = cg_iRIC_Read_BC_functionalWithName_WithGridId(fid, gid, type, num, name, paramname)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_functionalwithname_withgridid
   :file: cg_iric_read_bc_functionalwithname_withgridid_args.csv
   :header-rows: 1

