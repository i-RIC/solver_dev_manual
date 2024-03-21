.. _sec_ref_cg_iRIC_Write_Sol_Cell_Real_WithGridId:

cg_iRIC_Write_Sol_Cell_Real_WithGridId
======================================

格子のセルで定義された倍精度実数型の計算結果を書き込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_Cell_Real_WithGridId(fid, gid, name, v_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_Cell_Real_WithGridId(fid, gid, name, v_arr)

形式 (Python)
-----------------

.. code-block:: python

   v_arr = cg_iRIC_Write_Sol_Cell_Real_WithGridId(fid, gid, name)

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

gid
~~~

.. list-table:: gid の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - gid
   * - 入力/出力
     - 入力

   * - 説明
     - 格子ID (1から開始)
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

v_arr
~~~~~

.. list-table:: v_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - v_arr
   * - 入力/出力
     - 出力

   * - 説明
     - 計算結果の値の配列
   * - データ型 (FORTRAN)
     - double precision, dimension(:)
   * - データ型 (C/C++)
     - double*
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

