.. _iriclib_output_result_particlegroup:

粒子の座標ごとに値を持つ計算結果 (複数グループ可)
===================================================

粒子の座標ごとに値を持つ計算結果を出力する場合、
:numref:`table_iriclib_output_particlegroup_functions` に示す関数を
使用します。

ここで示す関数を使うと、複数のグループの粒子を出力することができます。
各グループの出力の最初と最後で、 `cg_iric_write_sol_particlegroup_groupbegin`
と `cg_iric_write_sol_particlegroup_groupend` を呼び出してください。

出力するプログラムの例は、:numref:`example_output_calc_result_particlegroup`
を参照してください。

.. note:: :ref:`iriclib_output_result_particle` で示した関数とは異なり、
          ここで示す関数では、一度の関数呼び出しでは粒子一つ分のデータを出力します。

.. _table_iriclib_output_particlegroup_functions:

.. list-table:: 粒子ごとに値を持つ計算結果の出力に利用する関数 (複数グループ可)
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_write_sol_particlegroup_groupbegin
     - 粒子の計算結果の出力を開始する

   * - cg_iric_write_sol_particlegroup_groupend
     - 粒子の計算結果の出力を終了する

   * - cg_iric_write_sol_particlegroup_pos2d
     - 粒子の位置を出力する (2次元)

   * - cg_iric_write_sol_particlegroup_pos3d
     - 粒子の位置を出力する (3次元)

   * - cg_iric_write_sol_particlegroup_integer
     - 整数の粒子ごとに値を持つ計算結果を出力する

   * - cg_iric_write_sol_particlegroup_real
     - 倍精度実数の粒子ごとに値を持つ計算結果を出力する

.. code-block:: fortran
   :caption: サンプルプログラム (粒子の座標ごとに値を持つ計算結果 (複数グループ可))
   :name: example_output_calc_result_particlegroup
   :linenos:

   program SampleProgram
     use iric
     implicit none

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     integer:: numparticles = 10
     double precision, dimension(:), allocatable:: particle_x, particle_y, 
     double precision, dimension(:), allocatable:: velocity_x, velocity_y, temperature
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
     ! 計算結果を保持するメモリを確保。
     allocate(particle_x(numparticles), particle_y(numparticles))
     allocate(velocity_x(numparticles), velocity_y(numparticles), temperature(numparticles))

     ! 格子を読み込む
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! 初期状態の情報を出力
     time = 0
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)

     call cg_iric_write_sol_particlegroup_groupbegin(fin, 'driftwood', ier)
     do i = 1, numparticles
       ! (ここで particle_x, particle_x, velocity_x, velocity_y, temperature に適切な値を設定)
       call cg_iric_write_sol_particlegroup_pos2d(fin, particle_x(i), particle_y(i), ier)
       call cg_iric_write_sol_particlegroup_real(fin, 'VelocityX', velocity_x(i), ier)
       call cg_iric_write_sol_particlegroup_real(fin, 'VelocityY', velocity_y(i), ier)
       call cg_iric_write_sol_particlegroup_real(fin, 'Temperature', temperature(i), ier)
     end do
     call cg_iric_write_sol_particlegroup_groupend(fin, ier)
     call cg_iric_write_sol_end(fin, ier)

     do
       time = time + 10.0

       ! (ここで計算を実行)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! 計算結果を出力
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_particlegroup_groupbegin(fin, 'driftwood', ier)
       do i = 1, numparticles
         ! (ここで particle_x, particle_x, velocity_x, velocity_y, temperature に適切な値を設定)
         call cg_iric_write_sol_particlegroup_pos2d(fin, particle_x(i), particle_y(i), ier)
         call cg_iric_write_sol_particlegroup_real(fin, 'VelocityX', velocity_x(i), ier)
         call cg_iric_write_sol_particlegroup_real(fin, 'VelocityY', velocity_y(i), ier)
         call cg_iric_write_sol_particlegroup_real(fin, 'Temperature', temperature(i), ier)
       end do
       call cg_iric_write_sol_particlegroup_groupend(fin, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! CGNS ファイルのクローズ
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
