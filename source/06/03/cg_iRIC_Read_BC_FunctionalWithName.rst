.. _sec_ref_cg_iRIC_Read_BC_FunctionalWithName:

cg_iRIC_Read_BC_FunctionalWithName
==================================

倍精度関数型の境界条件の変数の値を読み込む。変数が1つ、値が複数の関数型の読み込みに利用する。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_BC_FunctionalWithName(fid, type, num, name, paramname, v_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_BC_FunctionalWithName(fid, type, num, name, paramname, v_arr)

形式 (Python)
-----------------

.. code-block:: python

   v_arr = cg_iRIC_Read_BC_FunctionalWithName(fid, type, num, name, paramname)

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
     - 変数の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

paramname
~~~~~~~~~

.. list-table:: paramname の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - paramname
   * - 入力/出力
     - 入力

   * - 説明
     - 値の名前
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
     - 条件の値の配列
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

