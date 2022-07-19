.. _iriclib_load_grid:

Reading calculation grid
===========================

Reads a calculation grid from the CGNS file. iRIClib offers
subroutines for reading structured grids only.

.. list-table:: Subroutine to use
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_read_grid2d_str_size
     - Reads size of 2D structured grid

   * - cg_iric_read_grid2d_coords
     - Reads a 2D structured grid

   * - cg_iric_read_grid_integer_node
     - Reads the integer attribute values defined for grid nodes

   * - cg_iric_read_grid_real_node
     - Reads the double-precision attribute values defined for grid nodes

   * - cg_iric_read_grid_integer_cell
     - Reads the integer attribute values defined for cells

   * - cg_iric_read_grid_real_cell
     - Reads the double-precision attribute values defined for cells

   * - cg_iric_read_complex_count
     - Reads the number of groups of complex type grid attribute

   * - cg_iric_read_complex_integer
     - Reads the integer attribute values of complex type grid attribute

   * - cg_iric_read_complex_real
     - Reads the double precision attribute values of complex type grid attribute

   * - cg_iric_read_complex_realsingle
     - Reads the single precision attribute values of complex type grid attribute

   * - cg_iric_read_complex_string
     - Reads the string attribute values of complex type grid attribute

   * - cg_iric_read_complex_functionalsize
     - Checks the size of a f_functional-type attribute of complex type grid attribute

   * - cg_iric_read_complex_functional
     - Reads f_functional attribute data of complex type grid attribute

   * - cg_iric_read_complex_functionalwithname
     - Reads f_functional attribute of complex type grid attribute (with multiple values)

   * - cg_iric_read_complex_functional_realsingle
     - Reads f_functional attribute data of complex type grid attribute

   * - cg_iric_read_grid_complex_node
     - Reads the complex attribute values defined at grid nodes

   * - cg_iric_read_grid_complex_cell
     - Reads the complex attribute values defined at grid cells

   * - cg_iric_read_grid_functionaltimesize
     - Reads the number of values of dimension \"Time\" for f_functional grid attribute

   * - cg_iric_read_grid_functionaltime
     - Reads the values of dimension \"Time\" for f_functional grid attribute 

   * - cg_iric_read_grid_functionaldimensionsize
     - Reads the number of values of dimension for f_functional grid attribute

   * - cg_iric_read_grid_functionaldimension_integer
     - Reads the values of integer dimension for f_functional grid attribute

   * - cg_iric_read_grid_functionaldimension_real
     - Reads the values of double-precision dimension for f_functional grid attribute

   * - cg_iric_read_grid_functional_integer_node
     - Reads the values of f_functional integer grid attribute with dimension \"Time\" definied at grid nodes.

   * - cg_iric_read_grid_functional_real_node
     - Reads the values of f_functional double-precision grid attribute with dimension \"Time\" definied at grid nodes.

   * - cg_iric_read_grid_functional_integer_cell
     - Reads the values of f_functional integer grid attribute with dimension \"Time\" definied at grid cells.

   * - cg_iric_read_grid_functional_real_cell
     - Reads the values of f_functional double-precision grid attribute with dimension \"Time\" definied at grid cells.

The same subroutines for getting attributes such as cg_iric_read_grid_integer_node
can be used both for two-dimensional structured grids and
three-dimensional structured grids.

An example description for reading a two-dimensional structured grid is
shown in :numref:`example_load_two_dimensional_grid`.

.. code-block:: fortran
   :caption: Example of source code to read a grid
   :name: example_load_two_dimensional_grid
   :linenos:

   program Sample3
     use iric
     implicit none
   
     integer:: fin, ier, discharge_size, i, j
     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: elevation
     integer, dimension(:,:), allocatable:: obstacle
     integer:: rain_timeid
     integer:: rain_timesize
     double precision, dimension(:), allocatable:: rain_time
     double precision, dimension(:,:), allocatable:: rain
   
     ! Open CGNS file
     call cg_iric_open('test.cgn', IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Check the grid size
     call cg_iric_read_grid2d_str_size(fin, isize, jsize, ier)
   
     ! Allocate memory for loading the grid
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! Read the grid into memory
     call cg_iric_read_grid2d_coords(fin, grid_x, grid_y, ier)
   
     if (ier /=0) STOP "*** No grid data ***"
     ! (Output)
     print *, 'grid x,y: isize, jsize=', isize, jsize
     do i = 1, min(isize,5)
       do j = 1, min(jsize,5)
         print *, ' (',i,',',j,')=(',grid_x(i,j),',',grid_y(i,j),')'
       end do
     end do
   
     ! Allocate memory for elevation attribute values that are defined for grid nodes.
     allocate(elevation(isize, jsize))
     ! Read the attribute values.
     call cg_iric_read_grid_real_node(fin, 'Elevation', elevation, ier)
     print *, 'Elevation: isize, jsize=', isize, jsize
     do i = 1, min(isize,5)
       do j = 1, min(jsize,5)
         print *, ' (',i,',',j,')=(',elevation(i,j),')'
       end do
     end do
   
     ! Allocate memory for the obstacle attribute that is defined for cells. The size is (isize-1) * (jsize-1) since it is cell attribute.
     allocate(obstacle(isize-1, jsize-1))
     ! Read the attribute values in.
     call cg_iric_read_grid_integer_cell(fin, 'Obstacle', obstacle, ier)
     print *, 'Obstacle: isize -1, jsize-1=', isize-1, jsize-1
     do i = 1, min(isize-1,5)
       do j = 1, min(jsize-1,5)
         print *, ' (',i,',',j,')=(',obstacle(i,j),')'
       end do
     end do
     ! Read the number of times for Rain
     call cg_iric_read_grid_functionaltimesize(fin, 'Rain', rain_timesize);
     ! Allocate memory for time values of Rain
     allocate(rain_time(rain_timesize))
   
     ! Allocate memory for the rain attribute that is defined for cells. The size is (isize-1) * (jsize-1) since it is cell attribute.  allocate(rain(isize-1, jsize-1))
     ! Read the attribute at Time = 1
     rain_timeid = 1
     call cg_iric_read_grid_functional_real_cell(fin, 'Rain', rain_timeid, rain, ier)
     print *, 'Rain: isize -1, jsize-1=', isize-1, jsize-1
     do i = 1, min(isize-1,5)
       do j = 1, min(jsize-1,5)
         print *, ' (',i,',',j,')=(',rain(i,j),')'
       end do
     end do
   
     ! Deallocate memory that has been allocated
     deallocate(grid_x, grid_y, elevation, obstacle, rain_time, rain)
   
     ! Close CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program Sample3

Processing for a three-dimensional grid can be described in the same manner.
