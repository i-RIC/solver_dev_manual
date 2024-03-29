Reading calculation result
==============================

Read calculation result from CGNS files.

.. list-table:: Subroutines to use
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_read_sol_count
     - Reads the number of calculation result

   * - cg_iric_read_sol_time
     - Reads the time value

   * - cg_iric_read_sol_iteration
     - Reads the loop iteration value

   * - cg_iric_read_sol_baseiterative_integer
     - Reads the integer-type calculation result value

   * - cg_iric_read_sol_baseiterative_real
     - Reads the double-precision real-type calculation result value

   * - cg_iric_read_sol_gridcoord2d
     - Reads the 2D structured grid (for moving grid calculation)

   * - cg_iric_read_sol_gridcoord3d
     - Reads the 3D structured grid (for moving grid calculation)

   * - cg_iric_read_sol_node_integer
     - Reads the integer-type calculation result, having a value for each grid node

   * - cg_iric_read_sol_node_real
     - Reads the double-precision real-type calculation result, having a value for each grid node

   * - cg_iric_read_sol_cell_integer
     - Reads the integer-type calculation result, having a value for each grid cell

   * - cg_iric_read_sol_cell_real
     - Reads the double-precision real-type calculation result, having a value for each grid cell

:numref:`example_load_calculatioin_result` shows an example of reading
caluculation result from CGNS file, and output to standard output.

.. code-block:: fortran
   :caption: Example of reading calculation result
   :name: example_load_calculatioin_result
   :linenos:

   program SampleX
     use iric
     implicit none

     integer:: fin, ier, isize, jsize, solid, solcount, iter, i, j
     double precision, dimension(:,:), allocatable::grid_x, grid_y, result_real

     ! Opening CGNS file
     call cg_iric_open('test.cgn', IRIC_MODE_READ, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! Reads grid size
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)

     ! Allocate memory for reading calculation result
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     allocate(result_real(isize, jsize))

     ! Reads calculation result, and output to standard output.
     call cg_iric_read_sol_count(fin, solcount, ier)
     do solid = 1, solcount
       call cg_iric_read_sol_iteration(fin, solid, iter, ier)
       call cg_iric_read_sol_gridcoord2d(fin, solid, grid_x, grid_y, ier)
       call cg_iric_read_sol_real(fin, solid, 'result_real', result_real, ier)

       print *, 'iteration: ', iter
       print *, 'grid_x, grid_y, result: '
       do i = 1, isize
         do j = 1, jsize
           print *, '(', i, ', ', j, ') = (', grid_x(i, j), ', ', grid_y(i, j), ', ', result_real(i, j), ')'
         end do
       end do
     end do

     ! Closing CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program SampleX

The functions are used in calculation analysis program (See :ref:`how_to_dev_analysistool`).
