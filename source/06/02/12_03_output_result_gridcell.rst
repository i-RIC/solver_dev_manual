.. _iriclib_output_result_gridcell:

Value defined at grid cells
=================================

When you output value defined at grid cells, please use the functions in 
:numref:`table_iriclib_output_gridcell_functions`.

:numref:`example_output_calc_result_gridcell` shows an example of
the process to output value defined at grid cells.

.. _table_iriclib_output_gridcell_functions:

.. list-table:: Subroutines to use for outputting result defined at grid cells
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_write_sol_cell_integer
     - Outputs integer-type calculation results, having a value for each grid cell

   * - cg_iric_write_sol_real
     - Outputs double-precision real-type calculation results, having a value for each grid cell

.. code-block:: fortran
   :caption: Example source code (Value defined at grid cells)
   :name: example_output_calc_result_gridcell
   :linenos:

   program SampleProgram
     use iric
     implicit none

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     double precision, dimension(:,:), allocatable:: depth
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
     allocate(depth(isize - 1, jsize - 1), wetflag(isize - 1, jsize - 1))
     ! Read the grid into memory
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! Output the initial state information.
     time = 0
     convergence = 0.1
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)
     call cg_iric_write_sol_cell_real(fin, 'Depth', depth, ier)
     call cg_iric_write_sol_cell_integer(fin, 'Wet', wetflag, ier)
     call cg_iric_write_sol_end(fin, ier)
     do
       time = time + 10.0

       ! (Perform calculation here)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_cell_real(fin, 'Depth', depth, ier)
       call cg_iric_write_sol_cell_integer(fin, 'Wet', wetflag, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
