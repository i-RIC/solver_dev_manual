.. _iriclib_output_result_baseiterative:

One value for each time step
======================================

When you output one value for each time step, please use the functions in 
:numref:`table_iriclib_output_baseiterative_functions`.

:numref:`example_output_calc_result_baseiterative` shows an example of
the process to output value for each time step.

.. _table_iriclib_output_baseiterative_functions:

.. list-table:: Subroutines to use for outputting result value that have one value for each time step
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_write_sol_baseiterative_integer_f
     - Outputs integer-type calculation results
   * - cg_iric_write_sol_baseiterative_real_f
     - Outputs double-precision real-type calculation results
   * - cg_iric_write_sol_baseiterative_string_f
     - Outputs string-type calculation results

.. code-block:: fortran
   :caption: Example source code (One value for each time step)
   :name: example_output_calc_result_baseiterative
   :linenos:

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision:: convergence
     double precision, dimension(:,:), allocatable::grid_x, grid_y
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
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! Read the grid into memory
     call cg_iric_getgridcoord2d_f (grid_x, grid_y, ier)

     ! Output the initial state information.
     time = 0
     convergence = 0.1
     call cg_iric_write_sol_time_f(time, ier)
     ! Output calculation results
     call cg_iric_write_sol_baseiterative_real_f('Convergence', convergence, ier)
     do
       time = time + 10.0

       ! (Perform calculation here)

       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call iric_write_sol_start_f(condFile, ier)
       call cg_iric_write_sol_time_f(time, ier)
       call cg_iric_write_sol_baseiterative_real_f('Convergence', convergence, ier)
       call cg_iric_flush_f(condFile, fin, ier)
       call iric_write_sol_end_f(condFile, ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram
