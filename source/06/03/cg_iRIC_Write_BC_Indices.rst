.. _sec_ref_cg_iRIC_Write_BC_Indices:

cg_iRIC_Write_BC_Indices
========================

境界条件が設定された要素（格子点・セル・エッジ）のインデックスのリストを書き込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_BC_Indices(fid, type, num, length, idx_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_BC_Indices(fid, type, num, length, idx_arr)

形式 (Python)
-----------------

.. code-block:: python

   idx_arr = cg_iRIC_Write_BC_Indices(fid, type, num, length)

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

length
~~~~~~

.. list-table:: length の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - length
   * - 入力/出力
     - 入力

   * - 説明
     - インデックスの数
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

idx_arr
~~~~~~~

.. list-table:: idx_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - idx_arr
   * - 入力/出力
     - 出力

   * - 説明
     - インデックスの値の配列
   * - データ型 (FORTRAN)
     - integer, dimension(:)
   * - データ型 (C/C++)
     - int*
   * - データ型 (Python)
     - numpy.array

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

idx_arr に渡す値は、境界条件の定義位置によって、
以下に示すように異なります。
格子点、セルでは、値2つで一つの要素を定義しているのに対し、
辺では値4つで1つの要素を定義している点にご注意下さい。

.. list-table::  境界条件の定義位置と idx_arr の値の関係
   :header-rows: 1

   * - 境界条件の定義位置
     - idx_arr の値
   * - 格子点 (node)
     - | (格子点1のI), (格子点1のJ)
       | ...,
       | (格子点NのI), (格子点NのJ)
   * - セル (cell)
     - | (セル1のI), (セル1のJ)
       | ...,
       | (セルNのI), (セルNのJ)
   * - 辺 (edge)
     - | (辺1の開始格子点のI), (辺1の開始格子点のJ),
       | (辺1の終了格子点のI), (辺1の終了格子点のJ),
       | ...,
       | (辺Nの開始格子点のI), (辺Nの開始格子点のJ),
       | (辺Nの終了格子点のI), (辺Nの終了格子点のJ)
