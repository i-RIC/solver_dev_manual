.. _sec_ref_cg_iRIC_Read_Complex_Count:

cg_iRIC_Read_Complex_Count
==========================

複合型格子属性のグループの数を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Complex_Count(fid, groupname, num, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Complex_Count(fid, groupname, num)

形式 (Python)
-----------------

.. code-block:: python

   num = cg_iRIC_Read_Complex_Count(fid, groupname)

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

groupname
~~~~~~~~~

.. list-table:: groupname の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - groupname
   * - 入力/出力
     - 入力

   * - 説明
     - 複合型条件の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

num
~~~

.. list-table:: num の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - num
   * - 入力/出力
     - 出力

   * - 説明
     - 複合型条件のグループ番号
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int*
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

