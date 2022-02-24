cg_iric_initread
==================

指定したファイルを読み込み専用でiRIClibから利用するため、内部変数を初期化する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_initread(fid, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_InitRead(fid);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_InitRead(fid)

引数
----

.. csv-table:: cg_iric_initread の引数
   :file: cg_iric_initread_args.csv
   :header-rows: 1

