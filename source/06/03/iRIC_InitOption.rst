.. _sec_ref_iRIC_InitOption:

iRIC_InitOption
===============

ソルバーのオプションを指定する。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_InitOption(option, ier)

形式 (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_InitOption(option)

形式 (Python)
-----------------

.. code-block:: python

   iRIC_InitOption(option)

引数と戻り値
----------------------------

option
~~~~~~

.. list-table:: option の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - option
   * - 入力/出力
     - 入力

   * - 説明
     - 指定するオプションの値
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


備考
----

.. list-table:: option に指定可能な値
  
   * - option の値
     - 内容

   * - IRIC_OPTION_CANCEL
     - iRIC_Check_Cancel を利用してキャンセルを検知できることをGUIに伝える。
