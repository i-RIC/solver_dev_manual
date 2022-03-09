cg_iric_read_bc_functional
============================

倍精度関数型の境界条件の変数の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_bc_functional(fid, type, num, name, x, y, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_functional(fid, type, num, name, x, y);

形式 (Python)
---------------
.. code-block:: python

   x, y = cg_iRIC_Read_BC_functional(fid, type, num, name)

引数
----

.. csv-table:: cg_iric_read_bc_functional の引数
   :file: cg_iric_read_bc_functional_args.csv
   :header-rows: 1

