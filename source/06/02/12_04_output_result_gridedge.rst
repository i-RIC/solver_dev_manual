.. _iriclib_output_result_gridedge:

Value defined at grid edges
=================================

When you output value defined at grid edges, please use the functions in 
:numref:`table_iriclib_output_gridedge_functions`.

:numref:`example_output_calc_result_gridedge` shows an example of
the process to output value defined at grid edges.

.. _table_iriclib_output_gridedge_functions:

.. list-table:: Subroutines to use for outputting result defined at grid edges
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_write_sol_iface_integer
     - Outputs integer-type calculation results, having a value for each grid edge at i-direction

   * - cg_iric_write_sol_iface_real
     - Outputs double-precision real-type calculation results, having a value for each grid edge at i-direction

   * - cg_iric_write_sol_jface_integer
     - Outputs integer-type calculation results, having a value for each grid edge at j-direction

   * - cg_iric_write_sol_jface_real
     - Outputs double-precision real-type calculation results, having a value for each grid edge at j-direction

.. code-block:: fortran
   :caption: Example source code (Value defined at grid cells)
   :name: example_output_calc_result_gridedge
   :linenos:

   program SampleProgram
     use iric
     implicit none

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     double precision, dimension(:,:), allocatable:: fluxi, fluxj
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
     call cg_iric_write_sol_iface_real(fin, 'FluxI', fluxi, ier)
     call cg_iric_write_sol_jface_real(fin, 'FluxJ', fluxj, ier)
     call cg_iric_write_sol_end(fin, ier)
     do
       time = time + 10.0

       ! (Perform calculation here)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_iface_real(fin, 'FluxI', fluxi, ier)
       call cg_iric_write_sol_jface_real(fin, 'FluxJ', fluxj, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
