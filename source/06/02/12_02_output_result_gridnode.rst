.. _iriclib_output_result_gridnode:

Value defined at grid nodes
============================

When you output value defined at grid nodes, please use the functions in 
:numref:`table_iriclib_output_gridnode_functions`.

:numref:`example_output_calc_result_gridnode` shows an example of
the process to output value defined at grid nodes.

.. _table_iriclib_output_gridnode_functions:

.. list-table:: Subroutines to use for outputting result defined at grid nodes
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_write_sol_integer_f
     - Outputs integer-type calculation results, having a value for each grid node
   * - cg_iric_write_sol_real_f
     - Outputs double-precision real-type calculation results, having a value for each grid node

.. code-block:: fortran
   :caption: Example source code (Value defined at grid nodes)
   :name: example_output_calc_result_gridnode
   :linenos:

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     double precision, dimension(:,:), allocatable:: velocity_x, velocity_y, depth
     integer, dimension(:,:), allocatable:: wetflag
     character(len=20):: condFile

     condFile = 'test.cgn'

     ! Open CGNS file
     call cg_open_f(condFile, CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! Initialize iRIClib
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"

     ! Check the grid size
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)
     ! Allocate memory for loading the grid
     allocate(grid_x(isize, jsize), grid_y(isize, jsize))
     ! Allocate memory for calculation result
     allocate(velocity_x(isize, jsize), velocity_y(isize, jsize), depth(isize, jsize), wetflag(isize, jsize))
     ! Read the grid into memory
     call cg_iric_getgridcoord2d_f (grid_x, grid_y, ier)

     ! Output the initial state information.
     time = 0
     call cg_iric_write_sol_time_f(time, ier)
     call cg_iric_write_sol_real_f('VelocityX', velocity_x, ier)
     call cg_iric_write_sol_real_f('VelocityY', velocity_y, ier)
     call cg_iric_write_sol_real_f('Depth', depth, ier)
     call cg_iric_write_sol_integer_f('Wet', wetflag, ier)
     do
       time = time + 10.0

       ! (Perform calculation here)

       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call iric_write_sol_start_f(condFile, ier)
       call cg_iric_write_sol_time_f(time, ier)
       call cg_iric_write_sol_real_f('VelocityX', velocity_x, ier)
       call cg_iric_write_sol_real_f('VelocityY', velocity_y, ier)
       call cg_iric_write_sol_real_f('Depth', depth, ier)
       call cg_iric_write_sol_integer_f('Wet', wetflag, ier)
       call cg_iric_flush_f(condFile, fin, ier)
       call iric_write_sol_end_f(condFile, ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram
