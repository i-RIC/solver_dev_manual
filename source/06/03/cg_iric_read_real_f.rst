cg_iric_read_real_f
===================

CGNSファイルから倍精度の実数型の計算条件・格子生成条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_real_f(label, realvalue, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Real(label, &realvalue);

形式 (Python)
---------------
.. code-block:: python

   realvalue = cg_iRIC_Read_Real(label)

引数
----

.. csv-table:: cg_iric_read_real_f の引数
   :file: cg_iric_read_real_f_args.csv
   :header-rows: 1

