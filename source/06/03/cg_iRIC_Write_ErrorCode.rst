.. _sec_ref_cg_iRIC_Write_ErrorCode:

cg_iRIC_Write_ErrorCode
=======================

エラーコードを書き込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_ErrorCode(fid, errorcode, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_ErrorCode(fid, errorcode)

形式 (Python)
-----------------

.. code-block:: python

   cg_iRIC_Write_ErrorCode(fid, errorcode)

引数と戻り値
----------------------------

fid
~~~

.. list-table:: fid の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - fid
   * - 入力/出力
     - 入力

   * - 説明
     - ファイルID
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

errorcode
~~~~~~~~~

.. list-table:: errorcode の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - errorcode
   * - 入力/出力
     - 入力

   * - 説明
     - エラーコード
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

ier
~~~

.. list-table:: ier の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - ier
   * - 入力/出力
     - 出力

   * - 説明
     - エラーコード。0なら成功、エラーが起きるとそれ以外。
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - (定義なし)

