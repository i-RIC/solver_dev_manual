cg_iric_read_integer
======================

CGNSファイルから整数型の計算条件・格子生成条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_integer(fid, label, intvalue, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Integer(fid, label, &intvalue);

形式 (Python)
---------------
.. code-block:: python

   intvalue = cg_iRIC_Read_Integer(fid, label)

引数
----

.. csv-table:: cg_iric_read_integer の引数
   :file: cg_iric_read_integer_args.csv
   :header-rows: 1

