cg_iric_read_bc_functionalwithname
====================================

倍精度関数型の境界条件の変数の値を読み込む。変数が1つ、値が複数の関数型の境界条件の読み込みに利用する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_bc_functionalwithname(fid, type, num, name, paramname, data, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_F_functionalWithName(fid, type, num, name, paramname, data);

形式 (Python)
---------------
.. code-block:: python

   data = cg_iRIC_Read_BC_F_functionalWithName(fid, type, num, name, paramname)

引数
----

.. csv-table:: cg_iric_read_bc_functionalwithname の引数
   :file: cg_iric_read_bc_functionalwithname_args.csv
   :header-rows: 1

