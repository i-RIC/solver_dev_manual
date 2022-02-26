.. _iriclib_output_grid:

Outputting calculation grids
==================================

Outputs the calculation grid to the CGNS file.

Unlike ordinary solvers that simply read calculation grids from the CGNS file,
these subroutines are to be used in a particular kind of solver
in which a grid is created on the solver side or
a three-dimensional grid is generated from a two-dimensional grid.

Grid creating program always uses these subroutines.

The subroutines here should be used when a solver output the grid
in the initial state. When you want to output the grid shape 
modified after starting calculation, use the subroutines
described in :ref:`iriclib_output_grid_in_sol`.

.. list-table:: Subroutines to use
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_write_grid1d_coords
     - Outputs a one-dimensional structured grid

   * - cg_iric_write_grid2d_coords
     - Outputs a two-dimensional structured grid

   * - cg_iric_write_grid3d_coords
     - Outputs a three-dimensional structured grid

   * - cg_iric_write_grid_real_node
     - Outputs a grid node attribute with real number value

   * - cg_iric_write_grid_integer_node
     - Outputs a grid node attribute with integer value

   * - cg_iric_write_grid_real_cell
     - Outputs a grid cell attribute with real number value

   * - cg_iric_write_grid_integer_cell
     - Outputs a grid cell attribute with integer value

:numref:`example_export_three_dimensional_grid` shows an example of
the procedure of reading a two-dimensional grid, dividing it to
generate a three-dimensional grid, and then outputting the resulting grid.

.. code-block:: fortran
   :caption: Example of source code to output a grid
   :name: example_export_three_dimensional_grid
   :linenos:

   program Sample7
     use iric
     implicit none
   
     integer:: fin, ier, isize, jsize, ksize, i, j, k, aret
     double precision:: time
     double precision:: convergence
     double precision, dimension(:,:), allocatable::grid_x, grid_y, elevation
     double precision, dimension(:,:,:), allocatable::grid3d_x, grid3d_y, grid3d_z
     double precision, dimension(:,:,:), allocatable:: velocity, density
   
     ! Open CGNS file.
     call cg_iric_open('test3d.cgn', IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Check the grid size.
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
     ! Allocate memory for loading the grid.
     allocate(grid_x(isize,jsize), grid_y(isize,jsize), elevation(isize,jsize))
     ! Read the grid into memory.
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)
     call cg_iric_read_grid_real_node(fin, 'Elevation', elevation, ier)

     ! Generate a 3D grid from the 2D grid that has been read in.
     ! To obtain a 3D grid, the grid is divided into 5 in z direction.
   
     ksize = 6
     allocate(grid3d_x(isize,jsize,ksize), grid3d_y(isize,jsize,ksize), grid3d_z(isize,jsize,ksize))
     allocate(velocity(isize,jsize,ksize), STAT = aret)
     print *, aret
     allocate(density(isize,jsize,ksize), STAT = aret)
     print *, aret
     do i = 1, isize
       do j = 1, jsize
         do k = 1, ksize
           grid3d_x(i,j,k) = grid_x(i,j)
           grid3d_y(i,j,k) = grid_y(i,j)
           grid3d_z(i,j,k) = elevation(i,j) + (k - 1)
           velocity(i,j,k) = 0
           density(i,j,k) = 0
         end do
       end do
     end do
     ! Output the generated 3D grid
     call cg_iric_write_grid3d_coords(fin, isize, jsize, ksize, grid3d_x, grid3d_y, grid3d_z, ier)
   
     ! Output the initial state information
     time = 0
     convergence = 0.1
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)
     ! Output the grid.
     call cg_iric_write_sol_grid3d_coords(fin, grid3d_x, grid3d_y, grid3d_z, ier)
     ! Output calculation results.
     call cg_iric_write_sol_node_real(fin, 'Velocity', velocity, ier)
     call cg_iric_write_sol_node_real(fin, 'Density', density, ier)
     call cg_iric_write_sol_baseiterative_real(fin, 'Convergence', convergence, ier)
     call cg_iric_write_sol_end(fin, ier)

     do
       time = time + 10.0
       ! (Perform calculation here. The grid shape also changes.)
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       ! Output the grid.
       call cg_iric_write_sol_grid3d_coords(fin, grid3d_x, grid3d_y, grid3d_z, ier)
       ! Output calculation results.
       call cg_iric_write_sol_node_real(fin, 'Velocity', velocity, ier)
       call cg_iric_write_sol_node_real(fin, 'Density', density, ier)
       call cg_iric_write_sol_baseiterative_real(fin, 'Convergence', convergence, ier)
       call cg_iric_write_sol_end(fin, ier)

       If (time > 100) exit
     end do
   
     ! Close CGNS file.
     call cg_iric_close(fin, ier)
     stop
   end program Sample7
