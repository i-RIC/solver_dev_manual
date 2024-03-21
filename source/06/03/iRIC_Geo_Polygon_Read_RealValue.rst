.. _sec_ref_iRIC_Geo_Polygon_Read_RealValue:

iRIC_Geo_Polygon_Read_RealValue
===============================

ポリゴンの値を倍精度実数で読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_Polygon_Read_RealValue(geo_handle, value, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_Polygon_Read_RealValue(geo_handle, value)

形式 (Python)
-----------------

.. code-block:: python

   value = iRIC_Geo_Polygon_Read_RealValue(geo_handle)

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

value
~~~~~

.. list-table:: value の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - value
   * - 入力/出力
     - 出力

   * - 説明
     - 条件の値
   * - データ型 (FORTRAN)
     - double precision
   * - データ型 (C/C++)
     - double*
   * - データ型 (Python)
     - float

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

