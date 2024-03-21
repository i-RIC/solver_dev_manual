.. _sec_ref_cg_iRIC_Write_NamedGrid2d_Coords:

cg_iRIC_Write_NamedGrid2d_Coords
================================

2次元構造格子を出力する。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_NamedGrid2d_Coords(fid, name, isize, jsize, x_arr, y_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid2d_Coords(fid, name, isize, jsize, x_arr, y_arr)

形式 (Python)
-----------------

.. code-block:: python

   x_arr, y_arr = cg_iRIC_Write_NamedGrid2d_Coords(fid, name, isize, jsize)

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
     - 格子の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

isize
~~~~~

.. list-table:: isize の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - isize
   * - 入力/出力
     - 入力

   * - 説明
     - I方向の格子点数
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

jsize
~~~~~

.. list-table:: jsize の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - jsize
   * - 入力/出力
     - 入力

   * - 説明
     - J方向の格子点数
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

x_arr
~~~~~

.. list-table:: x_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - x_arr
   * - 入力/出力
     - 出力

   * - 説明
     - X座標の配列
   * - データ型 (FORTRAN)
     - double precision, dimension(:)
   * - データ型 (C/C++)
     - double*
   * - データ型 (Python)
     - numpy.array

y_arr
~~~~~

.. list-table:: y_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - y_arr
   * - 入力/出力
     - 出力

   * - 説明
     - Y座標の配列
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

