.. _solver_dev_add_loading:

計算条件、計算格子、境界条件の読み込み処理の記述
------------------------------------------------

計算条件、計算格子、境界条件の読み込み処理を記述します。

iRIC は、 :ref:`how_to_create_solver_def_file` で作成したソルバー定義ファイルに従って、
計算条件、格子、格子属性、境界条件を計算データファイルに出力しますので、
ソルバー定義ファイルでの記述に対応するように、計算条件、計算格子、境界条件の
読み込み処理を記述します。

計算条件、計算格子の読み込み処理を追記したソースコードを
:numref:`solver_with_loading` に示します。強調して示したのが追記した部分です。

.. code-block:: fortran
   :caption: 計算データファイルを開く処理、閉じる処理を追記したソースコード
   :name: solver_with_loading
   :linenos:
   :emphasize-lines: 8-32,34-106

   program SampleProgram
     use iric
     implicit none
     integer:: fin, ier
     integer:: icount, istatus
     character(200)::condFile
     integer:: maxiterations
     double precision:: timestep
     integer:: surfacetype
     double precision:: constantsurface
     integer:: variable_surface_size
     double precision, dimension(:), allocatable:: variable_surface_time
     double precision, dimension(:), allocatable:: variable_surface_elevation

     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: elevation
     integer, dimension(:,:), allocatable:: obstacle

     integer:: inflowid
     integer:: inflow_count
     integer:: inflow_element_max
     integer:: discharge_variable_sizemax
     integer, dimension(:), allocatable:: inflow_element_count
     integer, dimension(:,:,:), allocatable:: inflow_element
     integer, dimension(:), allocatable:: discharge_type
     double precision, dimension(:), allocatable:: discharge_constant
     integer, dimension(:), allocatable:: discharge_variable_size
     double precision, dimension(:,:), allocatable:: discharge_variable_time
     double precision, dimension(:,:), allocatable:: discharge_variable_value

     write(*,*) "Sample Program"

     ! (略)

     ! 計算条件の読み込み
     call cg_iric_read_integer(fin, "maxIteretions", maxiterations, ier)
     call cg_iric_read_real(fin, "timeStep", timestep, ier)
     call cg_iric_read_integer(fin, "surfaceType", surfacetype, ier)
     call cg_iric_read_real(fin, "constantSurface", constantsurface, ier)

     call cg_iric_read_functionalsize(fin, "variableSurface", variable_surface_size, ier)
     allocate(variable_surface_time(variable_surface_size))
     allocate(variable_surface_elevation(variable_surface_size))
     call cg_iric_read_functional(fin, "variableSurface", variable_surface_time, variable_surface_elevation, ier)

     ! 格子のサイズを調べる
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)

     ! 格子を読み込むためのメモリを確保
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! 格子を読み込む
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! 格子点で定義された属性 のメモリを確保
     allocate(elevation(isize, jsize))
     allocate(obstacle(isize - 1, jsize - 1))

     ! 属性を読み込む
     call cg_iric_read_grid_real_node(fin, "Elevation", elevation, ier)
     call cg_iric_read_grid_integer_cell(fin, "Obstacle", obstacle, ier)

     ! 流入口の数に従って、境界条件を保持するメモリを確保。
     allocate(inflow_element_count(inflow_count))
     allocate(discharge_type(inflow_count), discharge_constant(inflow_count))
     allocate(discharge_variable_size(inflow_count))

     ! 流入口に指定された格子点の数と、時間依存の流入量のサイズを調べる
     inflow_element_max = 0
     do inflowid = 1, inflow_count
       ! 流入口に指定された格子点の数
       call cg_iric_read_bc_indicessize(fin, 'inflow', inflowid, inflow_element_count(inflowid))
       if (inflow_element_max < inflow_element_count(inflowid)) then
         inflow_element_max = inflow_element_count(inflowid)
       end if
       ! 流入口の時間依存の流入量のデータの数
       call cg_iric_read_bc_functionalsize(fin, 'inflow', inflowid, 'FunctionalDischarge', discharge_variable_size(inflowid), ier);
       if (discharge_variable_sizemax < discharge_variable_size(inflowid)) then
         discharge_variable_sizemax = discharge_variable_size(inflowid)
       end if
     end do

     ! 流入口に指定された格子点と、時間依存の流入量を保持するメモリを確保。
     allocate(inflow_element(inflow_count, 2, inflow_element_max))
     allocate(discharge_variable_time(inflow_count, discharge_variable_sizemax))
     allocate(discharge_variable_value(inflow_count, discharge_variable_sizemax))

     ! 境界条件の読み込み
     do inflowid = 1, inflow_count
       ! 流入口に指定された格子点
       call cg_iric_read_bc_indices(fin, 'inflow', inflowid, inflow_element(inflowid:inflowid,:,:), ier)
       ! 流入量の種類 (0 = 一定、1 = 時間依存)
       call cg_iric_read_bc_integer(fin, 'inflow', inflowid, 'Type', discharge_type(inflowid:inflowid), ier)
       ! 流入量 (一定)
       call cg_iric_read_bc_real(fin, 'inflow', inflowid, 'ConstantDischarge', discharge_constant(inflowid:inflowid), ier)
       ! 流入量 (時間依存)
       call cg_iric_read_bc_functional(fin, 'inflow', inflowid, 'FunctionalDischarge', discharge_variable_time(inflowid:inflowid,:), discharge_variable_value(inflowid:inflowid,:), ier)
     end do

     ! 計算データファイルを閉じる
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram

計算条件などを読み込む関数に渡す引数が、
:ref:`solverdef_define_calccond`, :ref:`solverdef_define_gridcond`
でソルバー定義ファイルに定義した Item 要素の name 属性と一致していることに注目してください。

なお、ソルバー定義ファイルで定義する計算条件、格子、格子属性と、それを読み込むための
iRIClib の関数の対応関係については、 :ref:`calccond_def_examples` を参照してください。

また、計算条件、計算格子、境界条件の読み込みに使う関数の詳細については、
:ref:`iriclib_load_calccond`, :ref:`iriclib_load_grid`, :ref:`iriclib_load_bc` を参照してください。
