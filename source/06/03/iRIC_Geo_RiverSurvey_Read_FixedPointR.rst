.. _sec_ref_iRIC_Geo_RiverSurvey_Read_FixedPointR:

iRIC_Geo_RiverSurvey_Read_FixedPointR
=====================================

横断線の右岸延長線のデータを読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_FixedPointR(geo_handle, csid, set, dirx, diry, index, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_FixedPointR(geo_handle, csid, set, dirx, diry, index)

形式 (Python)
-----------------

.. code-block:: python

   set, dirx, diry, index = iRIC_Geo_RiverSurvey_Read_FixedPointR(geo_handle, csid)

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

set
~~~

.. list-table:: set の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - set
   * - 入力/出力
     - 出力

   * - 説明
     - 右岸延長線が登録されていたら1, そうでなければ0
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int*
   * - データ型 (Python)
     - int

dirx
~~~~

.. list-table:: dirx の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - dirx
   * - 入力/出力
     - 出力

   * - 説明
     - 向きのX成分
   * - データ型 (FORTRAN)
     - double precision
   * - データ型 (C/C++)
     - double*
   * - データ型 (Python)
     - float

diry
~~~~

.. list-table:: diry の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - diry
   * - 入力/出力
     - 出力

   * - 説明
     - 向きのY成分
   * - データ型 (FORTRAN)
     - double precision
   * - データ型 (C/C++)
     - double*
   * - データ型 (Python)
     - float

index
~~~~~

.. list-table:: index の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - index
   * - 入力/出力
     - 出力

   * - 説明
     - 右岸延長線の開始位置の標高データの番号
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

