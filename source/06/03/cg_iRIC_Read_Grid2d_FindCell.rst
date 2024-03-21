.. _sec_ref_cg_iRIC_Read_Grid2d_FindCell:

cg_iRIC_Read_Grid2d_FindCell
============================

指定した座標を含むセルのIDを返す。

この関数に渡す g_handle は :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open` を使って取得する。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_FindCell(grid_handle, x, y, cellId, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_FindCell(grid_handle, x, y, cellId)

形式 (Python)
-----------------

.. code-block:: python

   cellId = cg_iRIC_Read_Grid2d_FindCell(grid_handle, x, y)

引数と戻り値
----------------------------

grid_handle
~~~~~~~~~~~

.. list-table:: grid_handle の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - grid_handle
   * - 入力/出力
     - 入力

   * - 説明
     - 格子のハンドル
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

cellId
~~~~~~

.. list-table:: cellId の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - cellId
   * - 入力/出力
     - 出力

   * - 説明
     - セルID (1から開始)
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

