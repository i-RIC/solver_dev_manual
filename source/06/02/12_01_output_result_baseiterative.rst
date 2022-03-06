.. _iriclib_output_result_baseiterative:

1つのタイムステップで1つ値を持つ計算結果
============================================

1つのタイムステップで1つ値を持つ計算結果を出力する場合、
:numref:`table_iriclib_output_baseiterative_functions` に示す関数を
使用します。

出力するプログラムの例は、:numref:`example_output_calc_result_baseiterative`
を参照してください。

.. _table_iriclib_output_baseiterative_functions:

.. list-table:: 1つのタイムステップで1つ値を持つ計算結果の出力に利用する関数
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_write_sol_baseiterative_integer
     - 整数の計算結果を出力する

   * - cg_iric_write_sol_baseiterative_real
     - 倍精度実数の計算結果を出力する

   * - cg_iric_write_sol_baseiterative_string
     - 文字列の計算結果を出力する

.. code-block:: fortran
   :caption: サンプルプログラム (1つのタイムステップで1つ値を持つ計算結果)
   :name: example_output_calc_result_baseiterative
   :linenos:

   program SampleProgram
     use iric
     implicit none

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision:: convergence
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     character(len=20):: condFile

     condFile = 'test.cgn'

     ! CGNS ファイルのオープン
     call cg_iric_open(condFile, IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! 格子のサイズを調べる
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
     ! 格子を読み込むためのメモリを確保
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! 格子を読み込む
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! 初期状態の情報を出力
     time = 0
     convergence = 0.1
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)
     call cg_iric_write_sol_baseiterative_real(fin, 'Convergence', convergence, ier)
     call cg_iric_write_sol_end(fin, ier)
     do
       time = time + 10.0

       ! (ここで計算を実行)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! 計算結果を出力
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_baseiterative_real(fin, 'Convergence', convergence, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! CGNS ファイルのクローズ
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
