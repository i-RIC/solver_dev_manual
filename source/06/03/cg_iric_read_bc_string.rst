cg_iric_read_bc_string
========================

文字列型の境界条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_bc_string(type, num, name, value, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_String(type, num, name, value);

形式 (Python)
---------------
.. code-block:: python

   value = cg_iRIC_Read_BC_String(type, num, name)

引数
----

.. csv-table:: cg_iric_read_bc_string の引数
   :file: cg_iric_read_bc_string_args.csv
   :header-rows: 1

