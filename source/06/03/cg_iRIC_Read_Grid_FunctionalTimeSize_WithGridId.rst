.. _sec_ref_cg_iRIC_Read_Grid_FunctionalTimeSize_WithGridId:

cg_iRIC_Read_Grid_FunctionalTimeSize_WithGridId
===============================================

次元「時刻」を持つ格子の属性の次元の数を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid_FunctionalTimeSize_WithGridId(fid, gid, name, count, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid_FunctionalTimeSize_WithGridId(fid, gid, name, count)

形式 (Python)
-----------------

.. code-block:: python

   count = cg_iRIC_Read_Grid_FunctionalTimeSize_WithGridId(fid, gid, name)

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

gid
~~~

.. list-table:: gid の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - gid
   * - 入力/出力
     - 入力

   * - 説明
     - 格子ID (1から開始)
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
     - 格子属性の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

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
     - 時刻の数
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

