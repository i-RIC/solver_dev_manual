.. _sec_ref_cg_iRIC_Copy_Grid_WithGridId:

cg_iRIC_Copy_Grid_WithGridId
============================

CGNSファイルの間で格子をコピーする。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Copy_Grid_WithGridId(fid_from, fid_to, gid, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Copy_Grid_WithGridId(fid_from, fid_to, gid)

形式 (Python)
-----------------

.. code-block:: python

   cg_iRIC_Copy_Grid_WithGridId(fid_from, fid_to, gid)

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

