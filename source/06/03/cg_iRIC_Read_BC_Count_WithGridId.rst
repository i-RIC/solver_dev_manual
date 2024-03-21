.. _sec_ref_cg_iRIC_Read_BC_Count_WithGridId:

cg_iRIC_Read_BC_Count_WithGridId
================================

境界条件の数を読み込む。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_BC_Count_WithGridId(fid, gid, type, num, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_BC_Count_WithGridId(fid, gid, type, num)

形式 (Python)
-----------------

.. code-block:: python

   num = cg_iRIC_Read_BC_Count_WithGridId(fid, gid, type)

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

type
~~~~

.. list-table:: type の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - type
   * - 入力/出力
     - 入力

   * - 説明
     - 境界条件の名前
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

num
~~~

.. list-table:: num の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - num
   * - 入力/出力
     - 出力

   * - 説明
     - 境界条件の番号
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int*
   * - データ型 (Python)
     - int

