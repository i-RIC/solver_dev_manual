.. _sec_ref_cg_iRIC_Read_BC_IndicesSize:

cg_iRIC_Read_BC_IndicesSize
===========================

境界条件が設定された要素（格子点・セル・エッジ）の数を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_BC_IndicesSize(fid, type, num, size, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_BC_IndicesSize(fid, type, num, size)

形式 (Python)
-----------------

.. code-block:: python

   size = cg_iRIC_Read_BC_IndicesSize(fid, type, num)

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

type
~~~~

.. list-table:: type の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - type
   * - 入力/出力
     - 入力

   * - 説明
     - 境界条件の名前
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
     - 入力

   * - 説明
     - 境界条件の番号
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

size
~~~~

.. list-table:: size の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - size
   * - 入力/出力
     - 出力

   * - 説明
     - インデックスの値の数
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


備考
----

size に返される値は、境界条件が設定される位置によって、以下に示すように異なります。

.. list-table:: 境界条件を定義される位置と size の値の関係
   :header-rows: 1

   * - 境界条件の定義位置
     - sizeの値

   * - 格子点 (node)
     - 格子点の数

   * - セル (cell)
     - セルの数

   * - 辺 (edge)
     - 辺の数×2
