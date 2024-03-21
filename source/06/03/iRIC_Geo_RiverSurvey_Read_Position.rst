.. _sec_ref_iRIC_Geo_RiverSurvey_Read_Position:

iRIC_Geo_RiverSurvey_Read_Position
==================================

横断線の中心点の座標を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_Position(geo_handle, csid, x, y, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_Position(geo_handle, csid, x, y)

形式 (Python)
-----------------

.. code-block:: python

   x, y = iRIC_Geo_RiverSurvey_Read_Position(geo_handle, csid)

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

x
~

.. list-table:: x の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - x
   * - 入力/出力
     - 出力

   * - 説明
     - X座標
   * - データ型 (FORTRAN)
     - double precision
   * - データ型 (C/C++)
     - double*
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
     - 出力

   * - 説明
     - Y座標
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

