cg_iric_read_bc_functional
============================

Reads the value of a f_functional-type double-precision real variable.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_bc_functional(fid, type, num, label, x, y, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_functional(fid, type, num, name, x, y);

Format (Python)
----------------
.. code-block:: python

   x, y = cg_iRIC_Read_BC_functional(fid, type, num, name)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_functional
   :file: cg_iric_read_bc_functional_args.csv
   :header-rows: 1

