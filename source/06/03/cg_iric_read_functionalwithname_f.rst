cg_iric_read_functionalwithname_f
=================================

CGNSファイルから関数型の計算条件・格子生成条件の値を読み込む。変数が1つ、値が複数の関数型の計算条件・格子生成条件の読み込みに利用する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_functionalwithname_f(label, name, data, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_FunctionalWithName(label, name, data);

形式 (Python)
---------------
.. code-block:: python

   data = cg_iRIC_Read_FunctionalWithName(label, name)

引数
----

.. csv-table:: cg_iric_read_functionalwithname_f の引数
   :file: cg_iric_read_functionalwithname_f_args.csv
   :header-rows: 1

