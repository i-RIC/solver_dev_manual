cg_iric_read_integer_f
======================

CGNSファイルから整数型の計算条件・格子生成条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_integer_f(label, intvalue, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Integer(label, &intvalue);

形式 (Python)
---------------
.. code-block:: python

   intvalue = cg_iRIC_Read_Integer(label)

引数
----

.. csv-table:: cg_iric_read_integer_f の引数
   :file: cg_iric_read_integer_f_args.csv
   :header-rows: 1

