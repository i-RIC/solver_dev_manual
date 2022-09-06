.. _iriclib_output_result_for_multiple_grid:

複数の計算格子での計算結果の出力
==================================

iRIClib では、複数の計算格子での計算結果の出力に対応しています。

主な使用方法の例を以下に示します。

* 2次元格子と3次元格子両方での計算結果を出力する
* 2次元の非構造格子と構造格子での計算結果を出力する

そのような場合、関数名に _withgridid が追加された名前の関数を使用します。

例えば、2次元格子と3次元格子両方での計算結果を出力したい場合、格子の出力には、
:ref:`sec_iriclibfunc_cg_iric_write_grid3d_coords_withgridid` を利用します。

:ref:`sec_iriclibfunc_cg_iric_write_grid3d_coords` と
:ref:`sec_iriclibfunc_cg_iric_write_grid3d_coords_withgridid` では、以下に示すように
引数が異なります (FORTRANの場合)。"_withgridid" が付加された関数では、引数として
gid (Grid ID) が追加されています。

.. code-block:: fortran

   call cg_iric_write_grid3d_coords(fid, nx, ny, nz, x, y, z, ier)

.. code-block:: fortran

   call cg_iric_write_grid3d_coords_withgridid(fid, nx, ny, nz, x, y, z, gid, ier)

:ref:`sec_iriclibfunc_cg_iric_write_grid3d_coords_withgridid` は、
格子を CGNS ファイルに書き込むとともに、新しい格子のIDを返します。

複数の計算格子での計算結果を出力する場合、
"_withgridid" を付加した名前の関数を使用します。

例えば、格子点で定義された実数値の計算結果を出力したい場合、
:ref:`sec_iriclibfunc_cg_iric_write_sol_node_real_withgridid` を使用します。

:ref:`sec_iriclibfunc_cg_iric_write_sol_node_real_withgridid` の引数一覧を以下に示します。

.. code-block:: fortran

   call cg_iric_write_sol_node_real_withgridid(fid, gid, label, val, ier)

2番目の引数である gid として、上記で返された格子のIDを渡します。

あらかじめ iRIC GUI で作成しておいた2次元の格子の gid は1, 
ソルバ内で作成して上記処理で CGNS ファイルに書き込んだ格子の gid は2となる点がポイントです。
適切な gid を関数に渡すことで、2次元格子と3次元格子の計算結果両方を出力することが出来ます。

:ref:`sec_iriclibfunc_cg_iric_write_sol_node_real` と同様に、格子に関する入出力用の
関数には、全て _withgridid が付加された名前の関数が存在します。
