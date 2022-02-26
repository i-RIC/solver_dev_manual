cg_iric_read_functionalwithname
=================================

-  Reads the value of a f_functional-type real variable from the CGNS

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_functionalwithname(label, name, data, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_F_functionalWithName(label, name, data);

Format (Python)
----------------
.. code-block:: python

   data = cg_iRIC_Read_F_functionalWithName(label, name)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_functionalwithname
   :file: cg_iric_read_functionalwithname_args.csv
   :header-rows: 1

