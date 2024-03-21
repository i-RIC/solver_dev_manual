.. _sec_ref_cg_iRIC_Read_Grid_TriangleElementsSize_WithGridId:

cg_iRIC_Read_Grid_TriangleElementsSize_WithGridId
=================================================

非構造格子の三角形を構成する頂点IDの配列に必要なサイズを読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid_TriangleElementsSize_WithGridId(fid, gid, tsize, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid_TriangleElementsSize_WithGridId(fid, gid, tsize)

形式 (Python)
-----------------

.. code-block:: python

   tsize = cg_iRIC_Read_Grid_TriangleElementsSize_WithGridId(fid, gid)

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

tsize
~~~~~

.. list-table:: tsize の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - tsize
   * - 入力/出力
     - 出力

   * - 説明
     - 三角形の数
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

