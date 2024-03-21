.. _sec_ref_cg_iRIC_Write_Sol_ParticleGroup_Pos2d:

cg_iRIC_Write_Sol_ParticleGroup_Pos2d
=====================================

パーティクルの位置を書き込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_ParticleGroup_Pos2d(fid, x, y, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_ParticleGroup_Pos2d(fid, x, y)

形式 (Python)
-----------------

.. code-block:: python

   cg_iRIC_Write_Sol_ParticleGroup_Pos2d(fid, x, y)

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

x
~

.. list-table:: x の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - x
   * - 入力/出力
     - 入力

   * - 説明
     - X座標
   * - データ型 (FORTRAN)
     - double precision
   * - データ型 (C/C++)
     - double
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
     - 入力

   * - 説明
     - Y座標
   * - データ型 (FORTRAN)
     - double precision
   * - データ型 (C/C++)
     - double
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

