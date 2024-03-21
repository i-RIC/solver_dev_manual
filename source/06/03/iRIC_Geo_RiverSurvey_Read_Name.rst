.. _sec_ref_iRIC_Geo_RiverSurvey_Read_Name:

iRIC_Geo_RiverSurvey_Read_Name
==============================

横断線の名前を文字列として読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_Name(geo_handle, csid, strvalue, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_Name(geo_handle, csid, strvalue)

形式 (Python)
-----------------

.. code-block:: python

   strvalue = iRIC_Geo_RiverSurvey_Read_Name(geo_handle, csid)

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

csid
~~~~

.. list-table:: csid の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - csid
   * - 入力/出力
     - 入力

   * - 説明
     - 横断線ID (1から開始)
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

strvalue
~~~~~~~~

.. list-table:: strvalue の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - strvalue
   * - 入力/出力
     - 出力

   * - 説明
     - 断面の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - char*
   * - データ型 (Python)
     - str

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

