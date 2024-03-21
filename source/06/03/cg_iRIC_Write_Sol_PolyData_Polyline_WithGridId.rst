.. _sec_ref_cg_iRIC_Write_Sol_PolyData_Polyline_WithGridId:

cg_iRIC_Write_Sol_PolyData_Polyline_WithGridId
==============================================

計算結果として折れ線の形状を出力する

この関数を呼び出す前に :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin`, :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin_WithGridId` を呼び出す必要がある。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_PolyData_Polyline_WithGridId(fid, gid, numPoints, x_arr, y_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_PolyData_Polyline_WithGridId(fid, gid, numPoints, x_arr, y_arr)

形式 (Python)
-----------------

.. code-block:: python

   x_arr, y_arr = cg_iRIC_Write_Sol_PolyData_Polyline_WithGridId(fid, gid, numPoints)

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

numPoints
~~~~~~~~~

.. list-table:: numPoints の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - numPoints
   * - 入力/出力
     - 入力

   * - 説明
     - ポリゴンもしくは折れ線を構成する頂点の数
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

x_arr
~~~~~

.. list-table:: x_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - x_arr
   * - 入力/出力
     - 出力

   * - 説明
     - X座標の配列
   * - データ型 (FORTRAN)
     - double precision, dimension(:)
   * - データ型 (C/C++)
     - double*
   * - データ型 (Python)
     - numpy.array

y_arr
~~~~~

.. list-table:: y_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - y_arr
   * - 入力/出力
     - 出力

   * - 説明
     - Y座標の配列
   * - データ型 (FORTRAN)
     - double precision, dimension(:)
   * - データ型 (C/C++)
     - double*
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

