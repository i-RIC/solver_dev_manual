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

   * - cg_iric_write_sol_node_integer
     - Outputs integer-type calculation results, having a value for each grid node

   * - cg_iric_write_sol_node_real
     - Outputs double-precision real-type calculation results, having a value for each grid node

.. code-block:: fortran
   :caption: Example source code (Value defined at grid nodes)
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

     ! Open CGNS file
     call cg_iric_open(condFile, IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! Check the grid size
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
     ! Allocate memory for loading the grid
     allocate(grid_x(isize, jsize), grid_y(isize, jsize))
     ! Allocate memory for calculation result
     allocate(velocity_x(isize, jsize), velocity_y(isize, jsize), depth(isize, jsize), wetflag(isize, jsize))
     ! Read the grid into memory
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! Output the initial state information.
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

       ! (Perform calculation here)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_real(fin, 'VelocityX', velocity_x, ier)
       call cg_iric_write_sol_real(fin, 'VelocityY', velocity_y, ier)
       call cg_iric_write_sol_real(fin, 'Depth', depth, ier)
       call cg_iric_write_sol_integer(fin, 'Wet', wetflag, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
