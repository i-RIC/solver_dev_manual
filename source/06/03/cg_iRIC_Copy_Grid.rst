.. _sec_ref_cg_iRIC_Copy_Grid:

cg_iRIC_Copy_Grid
=================

CGNSファイルの間で格子をコピーする。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Copy_Grid(fid_from, fid_to, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Copy_Grid(fid_from, fid_to)

形式 (Python)
-----------------

.. code-block:: python

   cg_iRIC_Copy_Grid(fid_from, fid_to)

引数と戻り値
----------------------------

fid_from
~~~~~~~~

.. list-table:: fid_from の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - fid_from
   * - 入力/出力
     - 入力

   * - 説明
     - コピー元ファイルID
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

fid_to
~~~~~~

.. list-table:: fid_to の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - fid_to
   * - 入力/出力
     - 入力

   * - 説明
     - コピー先ファイルID
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

