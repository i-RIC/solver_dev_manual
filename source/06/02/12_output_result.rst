.. _iriclib_output_result:

計算結果の出力
==============

CGNSファイルに、計算結果を出力します。

iRIClib で出力できる計算結果は、大きく以下に分類されます。

* 1つのタイムステップで1つ値を持つ計算結果
* 格子点ごとに値を持つ計算結果
* 格子セルごとに値を持つ計算結果
* 粒子の座標ごとに値を持つ計算結果
* 粒子の座標ごとに値を持つ計算結果 (複数グループ可)
* ポリゴンもしくは折れ線ごとに値を持つ計算結果

どの種類の計算結果を出力する場合も、 :numref:`table_iriclib_output_start_and_end_functions`
と :numref:`table_iriclib_output_time_functions`
に示す関数は必ず使用します。

計算結果の分類ごとの固有の関数は、 :ref:`iriclib_output_result_baseiterative`
～ :ref:`iriclib_output_result_polydata` をそれぞれ参照してください。

.. _table_iriclib_output_start_and_end_functions:

.. list-table:: 計算結果の出力の開始前、終了後に利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - iric_check_cancel_f
     - ユーザがソルバーの実行をキャンセルしたか確認する
   * - iric_check_lock_f
     - CGNSファイルが GUI によってロックされているか確認する
   * - iric_write_sol_start_f
     - 計算結果の出力開始をGUIに通知する
   * - iric_write_sol_end_f
     - 計算結果の出力終了をGUIに通知する
   * - cg_iric_flush_f
     - 計算結果の出力をファイルに書き込む

.. _table_iriclib_output_time_functions:

.. list-table:: 時刻・ループ回数の出力に利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_write_sol_time_f
     - 時刻を出力する
   * - cg_iric_write_sol_iteration_f
     - ループ回数を出力する

.. note:: ベクトル量とスカラー量

   iRIClib では、ベクトル量の計算結果とスカラー量の計算結果は、
   同じ関数を使って出力を行います。

   ベクトル量の計算結果を出力する場合は、
   \"VelocityX\", \"VelocityY\" などの名前で各成分を出力してください。

   スカラー量の計算結果の出力で、名前の最後に \"X\", \"Y\", \"Z\" を使った場合、
   GUI で正しく読み込まれず可視化できませんのでご注意下さい。
   小文字の \"x\", \"y\", \"z\" は問題なく使用できます。

.. note:: 計算結果で使用する特別な名前

   計算結果について、iRIC では特別な名前が定義されており、
   特定の目的で使用される結果ではその名前を使用する必要があります。
   特別な計算結果の名前については :ref:`special_result_names` を参照してください。

.. note:: 格子点と格子セル

   格子に関係する計算結果は、格子点で出力する方法と、格子セルで出力する
   方法があります。

   基本的には、ソルバにおいて変数がどこで定義されているかによって、どちらの方法で
   計算結果を出力するかを選択してください。

   ただし、ベクトル量については格子点で出力してください。格子セルでベクトル量を
   出力しても、矢印、流線、パーティクルの描画はできません。

.. toctree::
   :maxdepth: 1

   12_01_output_result_baseiterative
   12_02_output_result_gridnode
   12_03_output_result_gridcell
   12_04_output_result_particle
   12_05_output_result_particlegroup
   12_06_output_result_polydata
