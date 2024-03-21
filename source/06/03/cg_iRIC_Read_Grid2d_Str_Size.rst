.. _sec_ref_cg_iRIC_Read_Grid2d_Str_Size:

cg_iRIC_Read_Grid2d_Str_Size
============================

構造格子のサイズ (格子のI方向とJ方向の格子点数)を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_Str_Size(fid, isize, jsize, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Str_Size(fid, isize, jsize)

形式 (Python)
-----------------

.. code-block:: python

   isize, jsize = cg_iRIC_Read_Grid2d_Str_Size(fid)

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

isize
~~~~~

.. list-table:: isize の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - isize
   * - 入力/出力
     - 出力

   * - 説明
     - I方向の格子点数
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int*
   * - データ型 (Python)
     - int

jsize
~~~~~

.. list-table:: jsize の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - jsize
   * - 入力/出力
     - 出力

   * - 説明
     - J方向の格子点数
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

