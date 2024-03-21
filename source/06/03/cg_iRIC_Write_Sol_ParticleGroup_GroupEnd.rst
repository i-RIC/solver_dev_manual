.. _sec_ref_cg_iRIC_Write_Sol_ParticleGroup_GroupEnd:

cg_iRIC_Write_Sol_ParticleGroup_GroupEnd
========================================

パーティクルで定義された計算結果の出力を終了する。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_ParticleGroup_GroupEnd(fid, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_ParticleGroup_GroupEnd(fid)

形式 (Python)
-----------------

.. code-block:: python

   cg_iRIC_Write_Sol_ParticleGroup_GroupEnd(fid)

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

