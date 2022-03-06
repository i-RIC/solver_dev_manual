.. _iriclib_open_cgns:

CGNS ファイルを開く
===================

CGNSファイルを開き、読み込み、書き込みができる状態にします。

書き込みを行う場合には mode として IRIC_MODE_MODIFY を指定します。

読み込み専用の場合には mode として iRIC_MODE_READ を指定します。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_open
     - CGNSファイルを開く。
