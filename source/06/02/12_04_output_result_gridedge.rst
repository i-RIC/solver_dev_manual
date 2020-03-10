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
   * - cg_iric_write_sol_iface_integer_f
     - Outputs integer-type calculation results, having a value for each grid edge at i-direction
   * - cg_iric_write_sol_iface_real_f
     - Outputs double-precision real-type calculation results, having a value for each grid edge at i-direction
   * - cg_iric_write_sol_jface_integer_f
     - Outputs integer-type calculation results, having a value for each grid edge at j-direction
   * - cg_iric_write_sol_jface_real_f
     - Outputs double-precision real-type calculation results, having a value for each grid edge at j-direction

.. code-block:: fortran
   :caption: Example source code (Value defined at grid cells)
   :name: example_output_calc_result_gridedge
   :linenos:

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     double precision, dimension(:,:), allocatable:: fluxi, fluxj
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
     allocate(depth(isize - 1, jsize - 1), wetflag(isize - 1, jsize - 1))
     ! Read the grid into memory
     call cg_iric_getgridcoord2d_f (grid_x, grid_y, ier)

     ! Output the initial state information.
     time = 0
     convergence = 0.1
     call cg_iric_write_sol_time_f(time, ier)
     ! Output calculation results
     call cg_iric_write_sol_iface_real_f('FluxI', fluxi, ier)
     call cg_iric_write_sol_jface_real_f('FluxJ', fluxj, ier)
     do
       time = time + 10.0

       ! (Perform calculation here)

       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call iric_write_sol_start_f(condFile, ier)
       call cg_iric_write_sol_time_f(time, ier)
       call cg_iric_write_sol_iface_real_f('FluxI', fluxi, ier)
       call cg_iric_write_sol_jface_real_f('FluxJ', fluxj, ier)
       call cg_iric_flush_f(condFile, fin, ier)
       call iric_write_sol_end_f(condFile, ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram
