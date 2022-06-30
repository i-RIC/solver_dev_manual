.. _how_to_dev_analysistool:

計算結果分析ソルバーの開発手順
==============================

概要
----

iRICでは、既存のCGNSファイルの計算結果を読み込み、分析（・加工）することができます。
分析結果は、新たな CGNS ファイルに書き出すことができます。
計算結果分析ソルバーの開発手順は、通常のソルバー開発手順と同様です
( :ref:`how_to_develop_solver` 参照)。

ここでは、計算結果分析ソルバーをFORTRANで開発する例を説明します。

2つのCGNSファイルを扱い、計算結果の分析をするソルバーのソースコードの例を
:numref:`solver_with_multi_cgns`
に示します。

.. code-block:: fortran
   :caption: 複数CGNSファイルを扱ったソースコード（抜粋）
   :name: solver_with_multi_cgns
   :linenos:

   ! (前略)

   ! ファイルオープン、初期化
   call cg_iric_open(cgnsfile, IRIC_MODE_MODIFY, fin1, ier)

   ! (略)

   ! 計算条件の読み込み等
   call cg_iric_read_functionalsize(fin1, 'func', param_func_size, ier)

   ! (略)

   !ファイルオープン、初期化（計算結果読み込み用）
   call cg_iric_open(param_inputfile, IRIC_MODE_READ, fin2, ier)

   ! (略)

   ! 計算結果の読み込み等
   call cg_iric_read_sol_count(fin2, solcount, ier)

   ! (略)

   ! 計算結果の分析等

   ! (略)

   ! 分析結果等の出力
   call cg_iric_write_sol_time(fin1, t, ier)

   ! (略)

   ! ファイルのクローズ
   call cg_iric_close(fin1, ier)
   call cg_iric_close(fin2, ier)

   ! (後略)

既存のCGNSの計算結果をもとに、「魚の生息しやすさ」を算出するソルバーのソースコードを
:numref:`analysis_tool_example_source`
に示します。

.. code-block:: fortran
   :caption: 既存のCGNSファイルを読み込み、分析するソルバーのソースコード
   :name: analysis_tool_example_source
   :linenos:

   program SampleProgram2
     use iric
     implicit none
   
     integer icount
     character(len=300) cgnsfile
   
     integer:: fin1, fin2, ier, istatus
   
     character(len=300) param_inputfile
     integer:: param_result
     character(len=100) param_resultother
     integer:: param_func_size
     double precision, dimension(:), allocatable:: param_func_param
     double precision, dimension(:), allocatable:: param_func_value
     character(len=100) resultname
   
     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: target_result
     double precision, dimension(:,:), allocatable:: analysis_result
     double precision:: tmp_target_result
     double precision:: tmp_analysis_result
   
     integer:: i, j, f, solid, solcount, iter
     double precision:: t
   
     icount = nargs()
     if (icount.eq.2) then
       call getarg(1, cgnsfile, istatus)
     else
       write(*,*) "Input File not specified."
       stop
     end if
   
     ! CGNS ファイルのオープン
     call cg_iric_open(cgnsfile, IRIC_MODE_MODIFY, fin1, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! 計算条件を読み込む
     call cg_iric_read_string(fin1, 'inputfile', param_inputfile, ier)
     call cg_iric_read_integer(fin1, 'result', param_result, ier)
     call cg_iric_read_string(fin1, 'resultother', param_resultother, ier)
   
     call cg_iric_read_functionalsize(fin1, 'func', param_func_size, ier)
     allocate(param_func_param(param_func_size), param_func_value(param_func_size))
     call cg_iric_read_functional(fin1, 'func', param_func_param, param_func_value, ier)
   
     if (param_result .eq. 0) resultname = 'Depth(m)'
     if (param_result .eq. 1) resultname = 'Elevation(m)'
     if (param_result .eq. 2) resultname = param_resultother
   
     ! 指定された CGNS ファイルから、格子を読み込む
     call cg_iric_open(param_inputfile, IRIC_MODE_READ, fin2, ier)
     if (ier /=0) STOP "*** Open error of CGNS file 2 ***"
     
     ! 格子を読み込む
     call cg_iric_read_grid2d_str_size(fin2, isize, jsize, ier)
     allocate(grid_x(isize, jsize), grid_y(isize, jsize))
     call cg_iric_read_grid2d_coords(fin2, grid_x, grid_y, ier)
   
     ! 読み込んだ格子を cgnsfile に出力する
     call cg_iric_write_grid2d_coords(fin1, isize, jsize, &
       grid_x, grid_y, ier)
   
     ! 計算結果を読み込んで加工するためのメモリを確保
     allocate(target_result(isize, jsize), analysis_result(isize, jsize))
   
     ! 計算結果を処理
     call cg_iric_read_sol_count(fin2, solcount, ier)
   
     do solid = 1, solcount
       ! 計算結果を読み込み
       call cg_iric_read_sol_time(fin2, solid, t, ier)
       call cg_iric_read_sol_node_real(fin2, solid, resultname, &
         target_result, ier)
   
       ! 読み込んだ計算結果をもとに、魚の生息しやすさを算出する。
       do i = 1, isize
         do j = 1, jsize
           tmp_target_result = target_result(i, j)
           do f = 1, param_func_size
             if ( &
               param_func_param(f) .le. tmp_target_result .and. &
               param_func_param(f + 1) .gt. tmp_target_result) then
               tmp_analysis_result = &
                 param_func_value(f) + &
                 (param_func_value(f + 1) - param_func_value(f)) / &
                 (param_func_param(f + 1) - param_func_param(f)) * &
                 (tmp_target_result - param_func_param(f))
             endif
           end do
           analysis_result(i, j) = tmp_analysis_result
         end do
       end do
   
       ! 処理済みの計算結果を出力
       call cg_iric_write_sol_time(fin1, t, ier)
       call cg_iric_write_sol_node_real(fin1, 'fish_existence', analysis_result, ier)
     end do
   
     ! CGNS ファイルのクローズ
     call cg_iric_close(fin1, ier)
     call cg_iric_close(fin2, ier)
     stop
   end program SampleProgram2
