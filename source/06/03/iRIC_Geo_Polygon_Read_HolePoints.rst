.. _sec_ref_iRIC_Geo_Polygon_Read_HolePoints:

iRIC_Geo_Polygon_Read_HolePoints
================================

ポリゴンの穴の頂点の座標を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_Polygon_Read_HolePoints(geo_handle, holeid, x_arr, y_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_Polygon_Read_HolePoints(geo_handle, holeid, x_arr, y_arr)

形式 (Python)
-----------------

.. code-block:: python

   x_arr, y_arr = iRIC_Geo_Polygon_Read_HolePoints(geo_handle, holeid)

引数と戻り値
----------------------------

geo_handle
~~~~~~~~~~

.. list-table:: geo_handle の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - geo_handle
   * - 入力/出力
     - 入力

   * - 説明
     - 地理情報のハンドル
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

holeid
~~~~~~

.. list-table:: holeid の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - holeid
   * - 入力/出力
     - 入力

   * - 説明
     - ポリゴンの穴のID (1から開始)
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

