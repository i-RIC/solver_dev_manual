.. _sec_ref_cg_iRIC_Read_Sol_BaseIterative_String:

cg_iRIC_Read_Sol_BaseIterative_String
=====================================

グローバルに定義された文字列型の計算結果を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Sol_BaseIterative_String(fid, step, name, strvalue, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Sol_BaseIterative_String(fid, step, name, strvalue)

形式 (Python)
-----------------

.. code-block:: python

   strvalue = cg_iRIC_Read_Sol_BaseIterative_String(fid, step, name)

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

step
~~~~

.. list-table:: step の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - step
   * - 入力/出力
     - 入力

   * - 説明
     - ステップ数
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

name
~~~~

.. list-table:: name の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - name
   * - 入力/出力
     - 入力

   * - 説明
     - 計算結果の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

strvalue
~~~~~~~~

.. list-table:: strvalue の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - strvalue
   * - 入力/出力
     - 出力

   * - 説明
     - 計算結果の値
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - char*
   * - データ型 (Python)
     - str

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

