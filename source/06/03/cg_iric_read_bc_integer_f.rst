cg_iric_read_bc_integer_f
==========================

整数型の境界条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_bc_integer_f(type, num, name, value, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_Integer(type, num, name, &value);

形式 (Python)
---------------
.. code-block:: python

   value = cg_iRIC_Read_BC_Integer(type, num, name)

引数
----

.. csv-table:: cg_iric_read_bc_integer_f の引数
   :file: cg_iric_read_bc_integer_f_args.csv
   :header-rows: 1

