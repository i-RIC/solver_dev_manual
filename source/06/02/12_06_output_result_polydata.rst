.. _iriclib_output_result_polydata:

Value defined at polygons or polylines
==============================================

When you output value defined at polygons or polylines, please use the functions in 
:numref:`table_iriclib_output_polydata_functions`.

When outputting polygons or polylines, you can output multiple groups.
To output data please call `cg_iric_write_sol_polydata_groupbegin_f` and
`cg_iric_write_sol_polydata_groupend_f`, before and after outputting data.

:numref:`example_output_calc_result_polydata` shows an example of
the process to output value defined at polygons or polylines.

.. note:: In functions for outputting value defined at particles,
          all coordinates and values are output with one function calls.
          But in case of polygons or polylines, data for only one polygon or polyline
          is output with each function call.

.. note:: The functions to output value defined at polygons or polylines
          support only two-dimension data.

.. note:: You can mix calculation result defined at polygons and polylines in one group.

.. note:: For polygons and polylines the scalar quantity value only is supported.

.. _table_iriclib_output_polydata_functions:

.. list-table:: Subroutines to use for outputting result defined at polygons or polylines
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_write_sol_polydata_groupbegin_f
     - Start outputting calculation result defined at polygons or polylines.
   * - cg_iric_write_sol_polydata_groupend_f
     - Finish outputting calculation result defined at polygons or polylines.
   * - cg_iric_write_sol_polydata_polygon_f
     - Output calculation result defined as polygon
   * - cg_iric_write_sol_polydata_polyline_f
     - Output calculation result defined as polyline
   * - cg_iric_write_sol_polydata_integer_f
     - Outputs integer-type calculation results, giving a value for a polygon or polyline
   * - cg_iric_write_sol_polydata_real_f
     - Outputs double-precision real-type calculation results, giving a value for a polygon or polyline

.. code-block:: fortran
   :caption: Example source code (Value defined at polygons or polylines)
   :name: example_output_calc_result_polydata
   :linenos:

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     integer:: numpolygons = 10
     integer:: numpoints = 5
     double precision, dimension(:), allocatable:: polydata_x, polydata_y, 
     double precision:: temperature = 26
     integer:: i
     integer:: status = 1
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
     ! Allocate memory for calculation result. Each polygon has five points.
     allocate(polydata_x(numpoints), polydata_y(numpoints))
     ! Read the grid into memory
     call cg_iric_getgridcoord2d_f(grid_x, grid_y, ier)

     ! Output the initial state information.
     time = 0
     call cg_iric_write_sol_time_f(time, ier)

     call cg_iric_write_sol_polydata_groupbegin_f('fish', ier)
     do i = 1, numpolygons
       ! (Specify values for polydata_x, polydata_y, temperature, status)
       call cg_iric_write_sol_polydata_polygon_f(numpoints, polydata_x, polydata_y, ier)
       call cg_iric_write_sol_polydata_real_f('Temperature', temperature, ier)
       call cg_iric_write_sol_polydata_integer_f('Status', status, ier)
     end do
     call cg_iric_write_sol_polydata_groupend_f(ier)

     do
       time = time + 10.0

       ! (Perform calculation here)

       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit

       ! Output calculation results
       call iric_write_sol_start_f(condFile, ier)
       call cg_iric_write_sol_time_f(time, ier)
       call cg_iric_write_sol_polydata_groupbegin_f('fish', ier)
       do i = 1, numpolygons
         ! (Specify values for polydata_x, polydata_y, temperature, status)
         call cg_iric_write_sol_polydata_polygon_f(numpoints, polydata_x, polydata_y, ier)
         call cg_iric_write_sol_polydata_real_f('Temperature', temperature, ier)
         call cg_iric_write_sol_polydata_integer_f('Status', status, ier)
       end do
       call cg_iric_write_sol_polydata_groupend_f(ier)

       if (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram
