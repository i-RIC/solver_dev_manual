.. _sec_ref_cg_iRIC_Read_Grid_Functional_Integer_JFace_WithGridId:

cg_iRIC_Read_Grid_Functional_Integer_JFace_WithGridId
=====================================================

次元「時刻」を持つ、格子のJ方向のセル境界面 (エッジ) で定義された整数型の属性を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid_Functional_Integer_JFace_WithGridId(fid, gid, name, dimid, v_arr, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid_Functional_Integer_JFace_WithGridId(fid, gid, name, dimid, v_arr)

形式 (Python)
-----------------

.. code-block:: python

   v_arr = cg_iRIC_Read_Grid_Functional_Integer_JFace_WithGridId(fid, gid, name, dimid)

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

name
~~~~

.. list-table:: name の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - name
   * - 入力/出力
     - 入力

   * - 説明
     - 格子属性の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

dimid
~~~~~

.. list-table:: dimid の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - dimid
   * - 入力/出力
     - 入力

   * - 説明
     - 時刻のID (1 ～ 時刻の数)
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

v_arr
~~~~~

.. list-table:: v_arr の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - v_arr
   * - 入力/出力
     - 出力

   * - 説明
     - 条件の値の配列
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

