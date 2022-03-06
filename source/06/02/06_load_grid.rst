.. _iriclib_load_grid:

計算格子の読み込み
=======================

CGNSファイルから、計算格子を読み込みます。iRIClib では、構造格子の読み込みの関数のみ提供します。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_read_grid2d_str_size
     - 2次元構造格子のサイズを読み込む

   * - cg_iric_read_grid2d_coords
     - 2次元構造格子を読み込む

   * - cg_iric_read_grid_nodecount
     - 2次元非構造格子の格子点の数を読み込む

   * - cg_iric_read_grid_cellcount
     - 2次元非構造格子の格子セルの数を読み込む

   * - cg_iric_read_grid_triangleelements
     - 2次元非構造格子の三角形の頂点IDのリストを読み込む

   * - cg_iric_read_grid_integer_node
     - 格子点で定義された整数の属性を読み込む

   * - cg_iric_read_grid_real_node
     - 格子点で定義された倍精度実数の属性を読み込む

   * - cg_iric_read_grid_integer_cell
     - セルで定義された整数の属性を読み込む

   * - cg_iric_read_grid_real_cell
     - セルで定義された倍精度実数の属性を読み込む

   * - cg_iric_read_complex_count
     - 複合型の属性のグループの数を読み込む

   * - cg_iric_read_complex_integer
     - 複合型の属性の整数の条件を読み込む

   * - cg_iric_read_complex_real
     - 複合型の属性の倍精度実数の条件を読み込む

   * - cg_iric_read_complex_realsingle
     - 複合型の属性の単精度実数の条件を読み込む

   * - cg_iric_read_complex_string
     - 複合型の属性の文字列の条件を読み込む

   * - cg_iric_read_complex_functionalsize
     - 複合型の属性の関数型の条件のサイズを調べる

   * - cg_iric_read_complex_functional
     - 複合型の属性の倍精度実数の関数型の条件を読み込む

   * - cg_iric_read_complex_functionalwithname
     - 複合型の属性の単精度実数の関数型の条件を読み込む

   * - cg_iric_read_complex_functional_realsingle
     - 複合型の属性の値を複数持つ倍精度実数の関数型の条件を読み込む

   * - cg_iric_read_grid_complex_node
     - 格子点で定義された複合型の属性を読み込む

   * - cg_iric_read_grid_complex_cell
     - セルで定義された複合型の属性を読み込む

   * - cg_iric_read_grid_functionaltimesize
     - 次元「時刻」(Time) を持つ格子属性の、時刻の数を調べる

   * - cg_iric_read_grid_functionaltime
     - 次元「時刻」(Time)の値を読み込む

   * - cg_iric_read_grid_functionaldimensionsize
     - 次元の数を調べる

   * - cg_iric_read_grid_functionaldimension_integer
     - 整数の次元の値を読み込む

   * - cg_iric_read_grid_functionaldimension_real
     - 倍精度実数の次元の値を読み込む

   * - cg_iric_read_grid_functional_integer_node
     - 次元「時刻」を持つ、格子点で定義された整数の属性を読み込む

   * - cg_iric_read_grid_functional_real_node
     - 次元「時刻」を持つ、格子点で定義された倍精度実数の属性を読み込む

   * - cg_iric_read_grid_functional_integer_cell
     - 次元「時刻」を持つ、セルで定義された整数の属性を読み込む

   * - cg_iric_read_grid_functional_real_cell
     - 次元「時刻」を持つ、セルで定義された倍精度実数の属性を読み込む

cg_iric_read_grid_integer_node など属性読み込み用の関数は、
2次元構造格子、3次元構造格子で共通で利用することができます。
2次元構造格子を読み込む処理の記述例を :numref:`example_load_two_dimensional_grid` に示します。

.. code-block:: fortran
   :caption: 2次元格子を読み込む処理の記述例
   :name: example_load_two_dimensional_grid
   :linenos:

   program Sample3
     use iric
     implicit none
   
     integer:: fin, ier, discharge_size, i, j
     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: elevation
     integer, dimension(:,:), allocatable:: obstacle
     integer:: rain_timeid
     integer:: rain_timesize
     double precision, dimension(:), allocatable:: rain_time
     double precision, dimension(:,:), allocatable:: rain
   
     ! CGNS ファイルのオープン
     call cg_iric_open('test.cgn', IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! 格子のサイズを調べる
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
   
     ! 格子を読み込むためのメモリを確保
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! 格子を読み込む
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)
   
     if (ier /=0) STOP "*** No grid data ***"
     ! （出力）
     print *, 'grid x,y: isize, jsize=', isize, jsize
     do i = 1, min(isize,5)
       do j = 1, min(jsize,5)
         print *, ' (',i,',',j,')=(',grid_x(i,j),',',grid_y(i,j),')'
       end do
     end do
   
     ! 格子点で定義された属性 elevation のメモリを確保
     allocate(elevation(isize, jsize))
     ! 属性を読み込む
     call cg_iric_read_grid_real_node(fin, 'Elevation', elevation, ier)
     print *, 'Elevation: isize, jsize=', isize, jsize
     do i = 1, min(isize,5)
       do j = 1, min(jsize,5)
         print *, ' (',i,',',j,')=(',elevation(i,j),')'
       end do
     end do
   
     ! セルで定義された属性 obstacle のメモリを確保。セルの属性なのでサイズは (isize-1) * (jsize-1)
     allocate(obstacle(isize-1, jsize-1))
     ! 属性を読み込む
     call cg_iric_read_grid_integer_cell(fin, 'Obstacle', obstacle, ier)
     print *, 'Obstacle: isize -1, jsize-1=', isize-1, jsize-1
     do i = 1, min(isize-1,5)
       do j = 1, min(jsize-1,5)
         print *, ' (',i,',',j,')=(',obstacle(i,j),')'
       end do
     end do
     ! Rain の時刻の数を読み込む
     call cg_iric_read_grid_functionaltimesize(fin, 'Rain', rain_timesize);
     ! Rain の時刻を読み込むメモリを確保。
     allocate(rain_time(rain_timesize))
   
     ! セルで定義された属性 rain のメモリを確保。セルの属性なのでサイズは (isize-1) * (jsize-1)
     allocate(rain(isize-1, jsize-1))
     ! Time = 1 での属性を読み込む
     rain_timeid = 1
     call cg_iric_read_grid_functional_real_cell(fin, 'Rain', rain_timeid, rain, ier)
     print *, 'Rain: isize -1, jsize-1=', isize-1, jsize-1
     do i = 1, min(isize-1,5)
       do j = 1, min(jsize-1,5)
         print *, ' (',i,',',j,')=(',rain(i,j),')'
       end do
     end do
   
     ! allocate で確保したメモリを開放
     deallocate(grid_x, grid_y, elevation, obstacle, rain_time, rain)
   
     ! CGNS ファイルのクローズ
     call cg_iric_close(fin, ier)
     stop
   end program Sample3
