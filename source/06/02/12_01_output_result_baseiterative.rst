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

   * - cg_iric_write_sol_baseiterative_integer
     - Outputs integer-type calculation results

   * - cg_iric_write_sol_baseiterative_real
     - Outputs double-precision real-type calculation results

   * - cg_iric_write_sol_baseiterative_string
     - Outputs string-type calculation results

.. code-block:: fortran
   :caption: Example source code (One value for each time step)
   :name: example_output_calc_result_baseiterative
   :linenos:

   program SampleProgram
     use iric
     implicit none

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision:: convergence
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     character(len=20):: condFile

     condFile = 'test.cgn'

     ! Open CGNS file
     call cg_iric_open(condFile, IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! Check the grid size
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
     ! Allocate memory for loading the grid
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! Read the grid into memory
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)

     ! Output the initial state information.
     time = 0
     convergence = 0.1

     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)
     call cg_iric_write_sol_baseiterative_real(fin, 'Convergence', convergence, ier)
     call cg_iric_write_sol_end(fin, ier)
     do
       time = time + 10.0

       ! (Perform calculation here)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_baseiterative_real(fin, 'Convergence', convergence, ier)
       call cg_iric_write_sol_end(fin, ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram
