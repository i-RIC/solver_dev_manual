.. _sec_ref_cg_iRIC_Read_Grid_TriangleElements_WithGridId:

cg_iRIC_Read_Grid_TriangleElements_WithGridId
=============================================

非構造格子の三角形を構成する頂点IDの配列を読み込む。

id_arr に、セルの数 x 3 のサイズの配列を渡すと、 1, 2, 3 番目, 4, 5, 6 番目, ... にそれぞれ 1番目, 2番目の三角形を構成する頂点の ID が返される。

配列 id_arr を作成するために、先に cg_iRIC_Read_CellCount で三角形の数を調べる。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid_TriangleElements_WithGridId(fid, gid, id_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid_TriangleElements_WithGridId(fid, gid, id_arr)

形式 (Python)
-----------------

.. code-block:: python

   id_arr = cg_iRIC_Read_Grid_TriangleElements_WithGridId(fid, gid)

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

id_arr
~~~~~~

.. list-table:: id_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - id_arr
   * - 入力/出力
     - 出力

   * - 説明
     - 三角形を構成する頂点IDの配列 (1から開始)
   * - データ型 (FORTRAN)
     - integer, dimension(:)
   * - データ型 (C/C++)
     - int*
   * - データ型 (Python)
     - numpy.array

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

