cg_iric_read_functionalsize
=============================

CGNSファイルから関数型の計算条件・格子生成条件のサイズを読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_functionalsize(fid, label, size, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_functionalSize(fid, label, &size);

形式 (Python)
---------------

Python にはこの関数は存在しない

引数
----

.. csv-table:: cg_iric_read_functionalsize の引数
   :file: cg_iric_read_functionalsize_args.csv
   :header-rows: 1

