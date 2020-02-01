.. _iriclib_output_result_particle:

粒子の座標ごとに値を持つ計算結果
===================================

粒子の座標ごとに値を持つ計算結果を出力する場合、
:numref:`table_iriclib_output_particle_functions` に示す関数を
使用します。

出力するプログラムの例は、:numref:`example_output_calc_result_particle`
を参照してください。

.. note:: ここで示す関数群は現在は非推奨です

   粒子の座標ごとに値を持つ計算結果を出力する場合は、
   :ref:`iriclib_output_result_particlegroup` に示す関数を使用する
   ことをおすすめします。そちらに示した関数を使用すれば、複数のグループの
   粒子を出力でき、グループごとに色の設定や粒子のサイズを変えて可視化することができます。

.. _table_iriclib_output_particle_functions:

.. list-table:: 粒子ごとに値を持つ計算結果の出力に利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_write_sol_particle_pos2d_f
     - 粒子の位置を出力する (2次元)
   * - cg_iric_write_sol_particle_pos3d_f
     - 粒子の位置を出力する (3次元)
   * - cg_iric_write_sol_particle_integer_f
     - 整数の粒子ごとに値を持つ計算結果を出力する
   * - cg_iric_write_sol_particle_real_f
     - 倍精度実数の粒子ごとに値を持つ計算結果を出力する

.. code-block:: fortran
   :caption: サンプルプログラム (粒子の座標ごとに値を持つ計算結果)
   :name: example_output_calc_result_particle
   :linenos:

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     integer:: numparticles = 10
     double precision, dimension(:), allocatable:: particle_x, particle_y
     double precision, dimension(:), allocatable:: velocity_x, velocity_y, temperature
     character(len=20):: condFile

     condFile = 'test.cgn'

     ! CGNS ファイルのオープン
     call cg_open_f(condFile, CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! 内部変数の初期化
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"

     ! 格子のサイズを調べる
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)
     ! 格子を読み込むためのメモリを確保
     allocate(grid_x(isize, jsize), grid_y(isize, jsize))
     ! 計算結果を保持するメモリを確保
     allocate(particle_x(numparticles), particle_y(numparticles))
     allocate(velocity_x(numparticles), velocity_y(numparticles), temperature(numparticles))

     ! 格子を読み込む
     call cg_iric_getgridcoord2d_f (grid_x, grid_y, ier)

     ! 初期状態の情報を出力
     time = 0
     call cg_iric_write_sol_time_f(time, ier)
     call cg_iric_write_sol_particle_pos2d_f(numparticles, particle_x, particle_y, ier)
     call cg_iric_write_sol_particle_real_f('VelocityX', velocity_x, ier)
     call cg_iric_write_sol_particle_real_f('VelocityY', velocity_y, ier)
     call cg_iric_write_sol_particle_real_f('Temperature', temperature, ier)
     do
       time = time + 10.0

       ! (ここで計算を実行)

       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit

       ! 計算結果を出力
       call iric_write_sol_start_f(condFile, ier)
       call cg_iric_write_sol_time_f(time, ier)
       call cg_iric_write_sol_particle_pos2d_f(numparticles, particle_x, particle_y, ier)
       call cg_iric_write_sol_particle_real_f('VelocityX', velocity_x, ier)
       call cg_iric_write_sol_particle_real_f('VelocityY', velocity_y, ier)
       call cg_iric_write_sol_particle_real_f('Temperature', temperature, ier)
       call cg_iric_flush_f(condFile, fin, ier)
       call iric_write_sol_end_f(condFile, ier)

       if (time > 1000) exit
     end do

     ! CGNS ファイルのクローズ
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram
