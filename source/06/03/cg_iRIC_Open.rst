.. _sec_ref_cg_iRIC_Open:

cg_iRIC_Open
============

CGNS ファイルを開く。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Open(filename, mode, fid, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Open(filename, mode, fid)

形式 (Python)
-----------------

.. code-block:: python

   fid = cg_iRIC_Open(filename, mode)

引数と戻り値
----------------------------

filename
~~~~~~~~

.. list-table:: filename の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - filename
   * - 入力/出力
     - 入力

   * - 説明
     - ファイル名
   * - データ型 (FORTRAN)
     - character(*)
   * - データ型 (C/C++)
     - const char*
   * - データ型 (Python)
     - str

mode
~~~~

.. list-table:: mode の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - mode
   * - 入力/出力
     - 入力

   * - 説明
     - モード (IRIC_MODE_READ, IRIC_MODE_WRITE, IRIC_MODE_MODIFY のいずれか)
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

fid
~~~

.. list-table:: fid の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - fid
   * - 入力/出力
     - 出力

   * - 説明
     - ファイルID
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

