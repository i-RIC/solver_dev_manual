.. _iriclib_output_result_polydata:

ポリゴンもしくは折れ線ごとに値を持つ計算結果
==============================================

ポリゴンもしくは折れ線ごとに値を持つ計算結果を出力する場合、
:numref:`table_iriclib_output_polydata_functions` に示す関数を
使用します。

ポリゴンもしくは折れ線では、複数のグループを出力することができます。
各グループの出力の最初と最後で、 `cg_iric_write_sol_polydata_groupbegin`
と `cg_iric_write_sol_polydata_groupend` を呼び出してください。

出力するプログラムの例は、:numref:`example_output_calc_result_polydata`
を参照してください。

.. note:: 粒子の座標ごとに値を持つ計算結果を出力する関数では、
          一度の関数の呼び出して全ての粒子の座標や値を出力しますが、
          ポリゴンもしくは折れ線ごとに値を持つ計算結果では、一度の関数呼び出しでは
          ポリゴンもしくは折れ線一つ分のデータを出力します。

.. note:: ポリゴンもしくは折れ線ごとに値を持つ計算結果は、2次元にのみ対応しています。

.. note:: 一つのグループの中にポリゴンと折れ線を混在させることもできます。

.. note:: ポリゴンもしくは折れ線では、計算結果の値はスカラー量にのみ対応しています。

.. _table_iriclib_output_polydata_functions:

.. list-table:: ポリゴンもしくは折れ線ごとに値を持つ計算結果の出力に利用する関数
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_write_sol_polydata_groupbegin
     - ポリゴンもしくは折れ線で定義された計算結果の出力を開始する

   * - cg_iric_write_sol_polydata_groupend
     - ポリゴンもしくは折れ線で定義された計算結果の出力を終了する

   * - cg_iric_write_sol_polydata_polygon
     - 計算結果としてポリゴンの形状を出力する

   * - cg_iric_write_sol_polydata_polyline
     - 計算結果として折れ線の形状を出力する

   * - cg_iric_write_sol_polydata_integer
     - 整数のポリゴンもしくは折れ線ごとに値を持つ計算結果を出力する

   * - cg_iric_write_sol_polydata_real
     - 倍精度実数のポリゴンもしくは折れ線ごとに値を持つ計算結果を出力する

.. code-block:: fortran
   :caption: サンプルプログラム (ポリゴンもしくは折れ線ごとに値を持つ計算結果)
   :name: example_output_calc_result_polydata
   :linenos:

   program SampleProgram
     use iric
     implicit none

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     integer:: numpolygons = 10
     integer:: numpoints = 5
     double precision, dimension(:), allocatable:: polydata_x, polydata_y, 
     double precision:: temperature = 26
     integer:: i
     integer:: status = 1
     character(len=20):: condFile

     condFile = 'test.cgn'

     ! CGNS ファイルのオープン
     call cg_iric_open(condFile, IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! 格子のサイズを調べる
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
     ! 格子を読み込むためのメモリを確保
     allocate(grid_x(isize, jsize), grid_y(isize, jsize))
     ! 計算結果を保持するメモリを確保。一つのポリゴンの点数は5点
     allocate(polydata_x(numpoints), polydata_y(numpoints))

     ! 格子を読み込む
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! 初期状態の情報を出力
     time = 0
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)

     call cg_iric_write_sol_polydata_groupbegin(fin, 'fish', ier)
     do i = 1, numpolygons
       ! (ここで polydata_x, polydata_y, temperature, status に適切な値を設定)
       call cg_iric_write_sol_polydata_polygon(fin, numpoints, polydata_x, polydata_y, ier)
       call cg_iric_write_sol_polydata_real(fin, 'Temperature', temperature, ier)
       call cg_iric_write_sol_polydata_integer(fin, 'Status', status, ier)
     end do
     call cg_iric_write_sol_polydata_groupend(fin, ier)
     call cg_iric_write_sol_end(fin, ier)

     do
       time = time + 10.0

       ! (ここで計算を実行)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! 計算結果を出力
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_polydata_groupbegin(fin, 'fish', ier)
       do i = 1, numpolygons
         ! (ここで polydata_x, polydata_y, temperature, status に適切な値を設定)
         call cg_iric_write_sol_polydata_polygon(fin, numpoints, polydata_x, polydata_y, ier)
         call cg_iric_write_sol_polydata_real(fin, 'Temperature', temperature, ier)
         call cg_iric_write_sol_polydata_integer(fin, 'Status', status, ier)
       end do
       call cg_iric_write_sol_polydata_groupend(fin, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! CGNS ファイルのクローズ
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
