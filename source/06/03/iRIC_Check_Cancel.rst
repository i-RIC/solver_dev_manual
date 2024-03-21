.. _sec_ref_iRIC_Check_Cancel:

iRIC_Check_Cancel
=================

ユーザがソルバの実行をキャンセルしたか確認する。

形式 (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Check_Cancel(canceled)

形式 (C/C++)
-----------------

.. code-block:: c

   canceled = iRIC_Check_Cancel()

形式 (Python)
-----------------

.. code-block:: python

   canceled = iRIC_Check_Cancel()

引数と戻り値
----------------------------

canceled
~~~~~~~~

.. list-table:: canceled の説明
   :header-rows: 1

   * - 項目
     - 値
   * - 名前
     - canceled
   * - 入力/出力
     - 出力

   * - 説明
     - キャンセルされていたら1、そうでなければ0。
   * - データ型 (FORTRAN)
     - integer
   * - データ型 (C/C++)
     - int
   * - データ型 (Python)
     - int

