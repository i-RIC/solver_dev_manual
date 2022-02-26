cg_iric_read_bc_real
======================

-  Reads the value of a double-precision real-type variable from the

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_bc_real(fid, type, num, label, realvalue, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_Real(fid, type, num, name, &value);

Format (Python)
----------------
.. code-block:: python

   value = cg_iRIC_Read_BC_Real(fid, type, num, name)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_real
   :file: cg_iric_read_bc_real_args.csv
   :header-rows: 1

