.. _iriclib_output_grid_in_sol:

Outputting calculation grids (only in the case of a moving grid)
=================================================================

Outputs the calculation grid to the CGNS file.

If the grid shape does not change in the calculation process,
this output is not necessary.

Before outputting the calculation grid at a specific time,
be sure to output the time (or iteration count) information
as described in :ref:`iriclib_output_time`.

The subroutines described in this section should be used for
outputting a calculation grid only when the grid shape is
changed in the course of calculation.
When outputting a grid in the following cases, use the subroutines
described in :ref:`iriclib_output_grid`.

* A new grid has been created in the solver.
* A grid of different number of dimensions or a grid having a
  different grid node count has been created by performing
  re-division of the grid or the like.
* A grid is created in the grid generating program

.. list-table:: Subroutines to use
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_write_sol_grid2d_coords
     - Outputs a two-dimensional structured grid

   * - cg_iric_write_sol_grid3d_coords
     - Outputs a three-dimensional structured grid

:numref:`example_output_grid_in_sol` shows an example of outputting
a two-dimensional structured grid after starting calculation.

.. code-block:: fortran
   :caption: Example of source code to output grids after starting calculation
   :name: example_output_grid_in_sol
   :linenos:

   program Sample5
     use iric
     implicit none
   
     integer:: fin, ier, isize, jsize
     double precision:: time
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
   
     ! Open CGNS file.
     call cg_iric_open('test.cgn', IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Check the grid size.
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
     ! Allocate memory for loading the grid.
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! Read the grid into memory.
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)
   
     ! Output the initial state information.
     time = 0
   
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)
     ! Output the grid.
     call cg_iric_write_sol_grid2d_coords(fin, grid_x, grid_y, ier)
     call cg_iric_write_sol_end(fin, ier)

     do
       time = time + 10.0
       ! (Perform calculation here.)
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       call cg_iric_write_sol_grid2d_coords(fin, grid_x, grid_y, ier)
       call cg_iric_write_sol_end(fin, ier)
       If (time > 1000) exit
     end do
   
     ! Close CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program Sample5
