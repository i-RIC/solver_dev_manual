.. _sec_ref_cg_iRIC_Read_Grid2d_Interpolate:

cg_iRIC_Read_Grid2d_Interpolate
===============================

指定した位置での値を、格子での値を使って補間して計算するための情報を返す。

この関数に渡す g_handle は :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open` を使って取得する。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_Interpolate(grid_handle, x, y, ok, count, nodeids_arr, weights_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Interpolate(grid_handle, x, y, ok, count, nodeids_arr, weights_arr)

形式 (Python)
-----------------

.. code-block:: python

   ok, count, nodeids_arr, weights_arr = cg_iRIC_Read_Grid2d_Interpolate(grid_handle, x, y)

引数と戻り値
----------------------------

grid_handle
~~~~~~~~~~~

.. list-table:: grid_handle の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - grid_handle
   * - 入力/出力
     - 入力

   * - 説明
     - 格子のハンドル
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

x
~

.. list-table:: x の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - x
   * - 入力/出力
     - 入力

   * - 説明
     - X座標
   * - データ型 (FORTRAN)
     - double precision
   * - データ型 (C/C++)
     - double
   * - データ型 (Python)
     - float

y
~

.. list-table:: y の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - y
   * - 入力/出力
     - 入力

   * - 説明
     - Y座標
   * - データ型 (FORTRAN)
     - double precision
   * - データ型 (C/C++)
     - double
   * - データ型 (Python)
     - float

ok
~~

.. list-table:: ok の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - ok
   * - 入力/出力
     - 出力

   * - 説明
     - 指定した座標を含むセルが見つかった場合は1, そうでなければ0
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int*
   * - データ型 (Python)
     - int

count
~~~~~

.. list-table:: count の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - count
   * - 入力/出力
     - 出力

   * - 説明
     - 指定した座標を含むセルを構成する頂点の数
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int*
   * - データ型 (Python)
     - int

nodeids_arr
~~~~~~~~~~~

.. list-table:: nodeids_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - nodeids_arr
   * - 入力/出力
     - 出力

   * - 説明
     - セルを構成する格子点のIDの配列 (1から開始)
   * - データ型 (FORTRAN)
     - integer, dimension(:)
   * - データ型 (C/C++)
     - int*
   * - データ型 (Python)
     - numpy.array

weights_arr
~~~~~~~~~~~

.. list-table:: weights_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - weights_arr
   * - 入力/出力
     - 出力

   * - 説明
     - 三角形を構成する頂点の値から内挿する際の重み係数の配列
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

