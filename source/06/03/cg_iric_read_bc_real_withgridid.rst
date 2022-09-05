cg_iric_read_bc_real_withgridid
=================================

Reads the value of a double-precision real-type variable defined at the boundary condition.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_bc_real_withgridid(fid, gid, type, num, label, realvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_Real_WithGridId(fid, gid, type, num, name, &value);

Format (Python)
----------------
.. code-block:: python

   value = cg_iRIC_Read_BC_Real_WithGridId(fid, gid, type, num, name)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_real_withgridid
   :file: cg_iric_read_bc_real_withgridid_args.csv
   :header-rows: 1

