.. _sec_ref_cg_iRIC_Read_Grid2d_Open:

cg_iRIC_Read_Grid2d_Open
========================

格子を開く。

この関数で開いた格子は、 :ref:`sec_ref_cg_iRIC_Read_Grid2d_Close` を使用して閉じる。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_Open(fid, grid_handle, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Open(fid, grid_handle)

形式 (Python)
-----------------

.. code-block:: python

   grid_handle = cg_iRIC_Read_Grid2d_Open(fid)

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

grid_handle
~~~~~~~~~~~

.. list-table:: grid_handle の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - grid_handle
   * - 入力/出力
     - 出力

   * - 説明
     - 格子のハンドル
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

