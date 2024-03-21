.. _sec_ref_cg_iRIC_Read_Geo_Filename:

cg_iRIC_Read_Geo_Filename
=========================

地理情報のファイル名と種類を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Geo_Filename(fid, name, geoid, strvalue, type, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Geo_Filename(fid, name, geoid, strvalue, type)

形式 (Python)
-----------------

.. code-block:: python

   strvalue, type = cg_iRIC_Read_Geo_Filename(fid, name, geoid)

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

name
~~~~

.. list-table:: name の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - name
   * - 入力/出力
     - 入力

   * - 説明
     - 地理情報の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

geoid
~~~~~

.. list-table:: geoid の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - geoid
   * - 入力/出力
     - 入力

   * - 説明
     - 地理情報データの番号 (1から開始)
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
     - ファイル名
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - char*
   * - データ型 (Python)
     - str

type
~~~~

.. list-table:: type の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - type
   * - 入力/出力
     - 出力

   * - 説明
     - 地理情報の種類 (1 = ポリゴン, 2 = 横断測量データ)
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

