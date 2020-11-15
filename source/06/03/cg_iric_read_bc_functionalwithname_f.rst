cg_iric_read_bc_functionalwithname_f
====================================

-  Reads the value of a functional-type real variable from the CGNS

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_bc_functionalwithname_f(type, num, label, name, data, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_FunctionalWithName(type, num, name, paramname, data);

Format (Python)
----------------
.. code-block:: python

   data = cg_iRIC_Read_BC_FunctionalWithName(type, num, name, paramname)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_functionalwithname_f
   :file: cg_iric_read_bc_functionalwithname_f_args.csv
   :header-rows: 1

