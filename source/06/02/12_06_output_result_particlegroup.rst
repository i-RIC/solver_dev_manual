.. _iriclib_output_result_particlegroup:

Value defined at particles (groups supported)
===================================================

When you output value defined at particles, please use the functions in 
:numref:`table_iriclib_output_particlegroup_functions`.

Using the functions explained here, you can output multiple groups of particles.
To output data please call `cg_iric_write_sol_particlegroup_groupbegin` and
`cg_iric_write_sol_particlegroup_groupend`, before and after outputting data.

:numref:`example_output_calc_result_particlegroup` shows an example of
the process to output value defined at particles.

.. note:: In functions explained here, data for one particle
          is output with each function call.

.. _table_iriclib_output_particlegroup_functions:

.. list-table:: Subroutines to use for outputting result defined at particles (groups supported)
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_write_sol_particlegroup_groupbegin
     - Start outputting calculation result defined at particles.

   * - cg_iric_write_sol_particlegroup_groupend
     - Finish outputting calculation result defined at particles.

   * - cg_iric_write_sol_particlegroup_pos2d
     - Outputs particle positions (two-dimensions)

   * - cg_iric_write_sol_particlegroup_pos3d
     - Outputs particle positions (three-dimensions)

   * - cg_iric_write_sol_particlegroup_integer
     - Outputs integer-type calculation results, giving a value for each particle.

   * - cg_iric_write_sol_particlegroup_real
     - Outputs double-precision real-type calculation results, giving a value for each particle.

.. code-block:: fortran
   :caption: Example source code (Value defined at particles (groups supported))
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

     ! Open CGNS file
     call cg_iric_open(condFile, IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! Check the grid size
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
     ! Allocate memory for loading the grid
     allocate(grid_x(isize, jsize), grid_y(isize, jsize))
     ! Allocate memory for calculation result.
     allocate(particle_x(numparticles), particle_y(numparticles))
     allocate(velocity_x(numparticles), velocity_y(numparticles), temperature(numparticles))

     ! Read the grid into memory
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! Output the initial state information.
     time = 0
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)

     call cg_iric_write_sol_particlegroup_groupbegin(fin, 'driftwood', ier)
     do i = 1, numparticles
       ! (Input values to particle_x, particle_x, velocity_x, velocity_y, temperature here)
       call cg_iric_write_sol_particlegroup_pos2d(fin, particle_x(i), particle_y(i), ier)
       call cg_iric_write_sol_particlegroup_real(fin, 'VelocityX', velocity_x(i), ier)
       call cg_iric_write_sol_particlegroup_real(fin, 'VelocityY', velocity_y(i), ier)
       call cg_iric_write_sol_particlegroup_real(fin, 'Temperature', temperature(i), ier)
     end do
     call cg_iric_write_sol_particlegroup_groupend(fin, ier)
     call cg_iric_write_sol_end(fin, ier)

     do
       time = time + 10.0

       ! (Perform calculation here)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_particlegroup_groupbegin(fin, 'driftwood', ier)
       do i = 1, numparticles
         ! (Input values to particle_x, particle_x, velocity_x, velocity_y, temperature here)
         call cg_iric_write_sol_particlegroup_pos2d(fin, particle_x(i), particle_y(i), ier)
         call cg_iric_write_sol_particlegroup_real(fin, 'VelocityX', velocity_x(i), ier)
         call cg_iric_write_sol_particlegroup_real(fin, 'VelocityY', velocity_y(i), ier)
         call cg_iric_write_sol_particlegroup_real(fin, 'Temperature', temperature(i), ier)
       end do
       call cg_iric_write_sol_particlegroup_groupend(fin, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
