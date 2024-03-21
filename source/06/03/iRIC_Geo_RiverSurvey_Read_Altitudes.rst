.. _sec_ref_iRIC_Geo_RiverSurvey_Read_Altitudes:

iRIC_Geo_RiverSurvey_Read_Altitudes
===================================

横断線の横断形状を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_Altitudes(geo_handle, csid, position_arr, height_arr, active_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_Altitudes(geo_handle, csid, position_arr, height_arr, active_arr)

形式 (Python)
-----------------

.. code-block:: python

   position_arr, height_arr, active_arr = iRIC_Geo_RiverSurvey_Read_Altitudes(geo_handle, csid)

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

position_arr
~~~~~~~~~~~~

.. list-table:: position_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - position_arr
   * - 入力/出力
     - 出力

   * - 説明
     - 標高データの位置 (0より小さい = 左岸側, 0 より大きい = 右岸側)
   * - データ型 (FORTRAN)
     - double precision, dimension(:)
   * - データ型 (C/C++)
     - double*
   * - データ型 (Python)
     - numpy.array

height_arr
~~~~~~~~~~

.. list-table:: height_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - height_arr
   * - 入力/出力
     - 出力

   * - 説明
     - 標高データの高さ
   * - データ型 (FORTRAN)
     - double precision, dimension(:)
   * - データ型 (C/C++)
     - double*
   * - データ型 (Python)
     - numpy.array

active_arr
~~~~~~~~~~

.. list-table:: active_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - active_arr
   * - 入力/出力
     - 出力

   * - 説明
     - 標高データの有効/無効 (1: 有効, 0: 無効)
   * - データ型 (FORTRAN)
     - integer, dimension(:)
   * - データ型 (C/C++)
     - int*
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

