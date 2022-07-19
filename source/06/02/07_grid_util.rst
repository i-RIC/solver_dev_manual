Investigating grid
======================

Open a handle to a grid, and investigate the grid, like calculate the area of cells in grid, find the cell that 
includes a certain coordinate. After investigating the grid, close the handle to the grid.

The functionis in this group can be used for both structured grids and unstructured grids.
The procedure to investigate grid is as below:

1. Open the grid contained in the CGNS file, and get the handle to the grid.
2. Investigate the grid by calling the functions in the group, with then handle as an argument.
3. After the investigation, close the grid with the handle.

.. list-table:: Subroutine to use
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_read_grid2d_open
     - Opens the grid

   * - cg_iric_read_sol_grid2d_open
     - Opens the grid in calculation result

   * - cg_iric_read_grid2d_close
     - Closes the grid

   * - cg_iric_read_grid2d_cellarea
     - Calculates and returns the area of a cell in the grid

   * - cg_iric_read_grid2d_findcell
     - Find and returns the ID of the cell that includes the specified coordinates

   * - cg_iric_read_grid2d_cellnodecount
     - Returns the number of nodes in the specified cell

   * - cg_iric_read_grid2d_interpolate
     - Returns the information to interpolate the value at the specified coordinates, with the values defined at grid nodes

   * - cg_iric_read_grid2d_interpolatewithcell
     - Returns the information to interpolate the value at the specified coordinates, with the values defined at grid nodes

:numref:`example_grid_util` shows an example of investigating the grid.

.. code-block:: fortran
   :caption: Example source code of investigating the grid
   :name: example_grid_util
   :linenos:

   program TestX
     use iric
     implicit none

     integer:: i, ok
     integer:: fin, g_handle, ier
     integer:: nodecount, cellnodecount,
     double precision: area
     double precision, dimension(:), allocatable:: depth
     integer, dimension(4):: nodeid_arr
     double precision:: depth_interpolated
     double precision, dimension(4):: weights_arr
   
     ! Opens CGNS file
     call cg_iric_open("test.cgn", IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! Opens the grid
     call cg_iric_read_grid2d_open(fin, g_handle, ier)

     ! Calculates the area of the cell
     call cg_iric_read_grid2d_cellarea(g_handle, 1, area, ier)

     ! Gets the number of nodes in the grid
     call cg_iric_read_grid_nodecount(fin, nodecount, ier)

     ! Allocate memory
     allocate(depth(nodecount))

     ! Gets the values of calculation result 'depth'
     call cg_iric_read_sol_node_real(fin, 1, 'depth', depth, ier)

     ! Gets the informationi to interpolate value at coordinates (10.8, 12.5)
     call cg_iric_read_grid2d_interpolate(g_handle, 10.8, 12.5, ok, cellnodecount, nodeid_arr, weights_arr)

     ! Calculates the interpolated value of depth at coordinates (10.8, 12.5)
     depth_interpolated = 0
     do i = 1, cellnodecount
       depth_interpolated = depth_interpolated + depth(nodeid_arr(i)) * weights_arr(i)
     end do

     ! Closes the grid
     call cg_iric_read_grid2d_close(g_handle, ier)

     deallocate(depth)
     stop
   end program TestX
