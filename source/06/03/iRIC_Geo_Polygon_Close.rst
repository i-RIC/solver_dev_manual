.. _sec_ref_iRIC_Geo_Polygon_Close:

iRIC_Geo_Polygon_Close
======================

ポリゴンファイルを閉じる。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_Polygon_Close(geo_handle, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_Polygon_Close(geo_handle)

形式 (Python)
-----------------

.. code-block:: python

   iRIC_Geo_Polygon_Close(geo_handle)

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

