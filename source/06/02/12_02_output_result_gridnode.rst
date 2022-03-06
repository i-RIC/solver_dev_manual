.. _iriclib_output_result_gridnode:

格子点ごとに値を持つ計算結果
============================

格子点ごとに値を持つ計算結果を出力する場合、
:numref:`table_iriclib_output_gridnode_functions` に示す関数を
使用します。

出力するプログラムの例は、:numref:`example_output_calc_result_gridnode`
を参照してください。

.. _table_iriclib_output_gridnode_functions:

.. list-table:: 格子点ごとに値を持つ計算結果の出力に利用する関数
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_write_sol_node_integer
     - 整数の格子点ごとに値を持つ計算結果を出力する

   * - cg_iric_write_sol_node_real
     - 倍精度実数の格子点ごとに値を持つ計算結果を出力する

.. code-block:: fortran
   :caption: サンプルプログラム (格子点ごとに値を持つ計算結果)
   :name: example_output_calc_result_gridnode
   :linenos:

   program SampleProgram
     use iric
     implicit none

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     double precision, dimension(:,:), allocatable:: velocity_x, velocity_y, depth
     integer, dimension(:,:), allocatable:: wetflag
     character(len=20):: condFile

     condFile = 'test.cgn'

     ! CGNS ファイルのオープン
     call cg_iric_open(condFile, IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! 格子のサイズを調べる
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
     ! 格子を読み込むためのメモリを確保
     allocate(grid_x(isize, jsize), grid_y(isize, jsize))
     ! 計算結果を保持するメモリも確保
     allocate(velocity_x(isize, jsize), velocity_y(isize, jsize), depth(isize, jsize), wetflag(isize, jsize))
     ! 格子を読み込む
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! 初期状態の情報を出力
     time = 0
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)
     call cg_iric_write_sol_real(fin, 'VelocityX', velocity_x, ier)
     call cg_iric_write_sol_real(fin, 'VelocityY', velocity_y, ier)
     call cg_iric_write_sol_real(fin, 'Depth', depth, ier)
     call cg_iric_write_sol_integer(fin, 'Wet', wetflag, ier)
     call cg_iric_write_sol_end(fin, ier)
     do
       time = time + 10.0

       ! (ここで計算を実行)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! 計算結果を出力
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_real(fin, 'VelocityX', velocity_x, ier)
       call cg_iric_write_sol_real(fin, 'VelocityY', velocity_y, ier)
       call cg_iric_write_sol_real(fin, 'Depth', depth, ier)
       call cg_iric_write_sol_integer(fin, 'Wet', wetflag, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! CGNS ファイルのクローズ
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
