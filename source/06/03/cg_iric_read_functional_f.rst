cg_iric_read_functional_f
=========================

CGNSファイルから倍精度実数の関数型の計算条件・格子生成条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_functional_f(label, x, y, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Functional(label, x, y);

形式 (Python)
---------------
.. code-block:: python

   x, y = cg_iRIC_Read_Functional(label)

引数
----

.. csv-table:: cg_iric_read_functional_f の引数
   :file: cg_iric_read_functional_f_args.csv
   :header-rows: 1

