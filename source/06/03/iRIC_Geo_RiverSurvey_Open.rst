.. _sec_ref_iRIC_Geo_RiverSurvey_Open:

iRIC_Geo_RiverSurvey_Open
=========================

横断測量データファイルを開く。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Open(filename, geo_handle, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Open(filename, geo_handle)

形式 (Python)
-----------------

.. code-block:: python

   geo_handle = iRIC_Geo_RiverSurvey_Open(filename)

引数と戻り値
----------------------------

filename
~~~~~~~~

.. list-table:: filename の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - filename
   * - 入力/出力
     - 入力

   * - 説明
     - ファイル名
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

geo_handle
~~~~~~~~~~

.. list-table:: geo_handle の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - geo_handle
   * - 入力/出力
     - 出力

   * - 説明
     - 地理情報のハンドル
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

