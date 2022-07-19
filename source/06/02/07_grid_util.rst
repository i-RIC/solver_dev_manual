格子の調査処理
======================

格子を開き、格子のセルの面積の計算、特定の座標を含むセルの探索などを行います。調査が終わったら、格子を閉じます。

このグループの関数は、CGNS ファイルに含まれている格子が構造格子の場合と非構造格子の場合どちらでも使用できます。
格子の調査処理の手順は、以下の通りになります。

1. CGNS ファイルに含まれる格子を開き、ハンドルを取得します。
2. ハンドルを引数として渡し、格子について調査の処理を実行します。
3. 使い終わったら、ハンドルを渡して格子を閉じます。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_read_grid2d_open
     - 格子を開く

   * - cg_iric_read_sol_grid2d_open
     - 計算結果の格子を開く

   * - cg_iric_read_grid2d_close
     - 格子を閉じる

   * - cg_iric_read_grid2d_cellarea
     - 格子のセルの面積を計算して返す

   * - cg_iric_read_grid2d_findcell
     - 指定した座標を含むセルのIDを返す

   * - cg_iric_read_grid2d_cellnodecount
     - 指定したセルを構成する頂点の数を返す

   * - cg_iric_read_grid2d_interpolate
     - 指定した位置での値を、格子での値を使って補間して計算するための情報を返す

   * - cg_iric_read_grid2d_interpolatewithcell
     - 指定した位置での値を、格子での値を使って補間して計算するための情報を返す

格子の調査処理の記述例を :numref:`example_grid_util`
に示します。

.. code-block:: fortran
   :caption: 格子の調査処理の記述例
   :name: example_grid_util
   :linenos:

   program TestX
     use iric
     implicit none

     integer:: i, ok
     integer:: fin, g_handle, ier
     integer:: nodecount, cellnodecount,
     double precision: area
     double precision, dimension(:), allocatable:: depth
     integer, dimension(4):: nodeid_arr
     double precision:: depth_interpolated
     double precision, dimension(4):: weights_arr
   
     ! CGNSファイルを開く
     call cg_iric_open("test.cgn", IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! 格子を開く
     call cg_iric_read_grid2d_open(fin, g_handle, ier)

     ! 格子のセルの面積を取得
     call cg_iric_read_grid2d_cellarea(g_handle, 1, area, ier)

     ! 格子の頂点の数を取得
     call cg_iric_read_grid_nodecount(fin, nodecount, ier)

     ! メモリを確保
     allocate(depth(nodecount))

     ! 計算結果 depth の値を取得
     call cg_iric_read_sol_node_real(fin, 1, 'depth', depth, ier)

     ! 座標 (10.8, 12.5) での値を補間して計算するための情報を取得
     call cg_iric_read_grid2d_interpolate(g_handle, 10.8, 12.5, ok, cellnodecount, nodeid_arr, weights_arr)

     ! 座標 (10.8, 12.5) での depth の値を、取得した情報に基づいて計算
     depth_interpolated = 0
     do i = 1, cellnodecount
       depth_interpolated = depth_interpolated + depth(nodeid_arr(i)) * weights_arr(i)
     end do

     ! 格子を閉じる
     call cg_iric_read_grid2d_close(g_handle, ier)

     deallocate(depth)
     stop
   end program TestX
