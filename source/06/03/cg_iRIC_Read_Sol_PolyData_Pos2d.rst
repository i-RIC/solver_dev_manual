.. _sec_ref_cg_iRIC_Read_Sol_PolyData_Pos2d:

cg_iRIC_Read_Sol_PolyData_Pos2d
===============================

ポリゴンもしくは折れ線で定義された計算結果の頂点の座標を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Sol_PolyData_Pos2d(fid, step, groupname, x_arr, y_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Sol_PolyData_Pos2d(fid, step, groupname, x_arr, y_arr)

形式 (Python)
-----------------

.. code-block:: python

   x_arr, y_arr = cg_iRIC_Read_Sol_PolyData_Pos2d(fid, step, groupname)

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
     - ポリゴンもしくは折れ線のグループの名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

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

