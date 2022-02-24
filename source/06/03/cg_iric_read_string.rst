cg_iric_read_string
=====================

CGNSファイルから文字列型の計算条件・格子生成条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_string(label, strvalue, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_String(label, strvalue);

形式 (Python)
---------------
.. code-block:: python

   strvalue = cg_iRIC_Read_String(label)

引数
----

.. csv-table:: cg_iric_read_string の引数
   :file: cg_iric_read_string_args.csv
   :header-rows: 1

