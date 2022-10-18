.. _solver_dev_add_outputting:


Adding codes to output time and calculation results
----------------------------------------------------

Adds codes to output time and calculation results.

When you develop a solver that is used for time-dependent flow, you have
to repeat outputting time and calculation results for the number of time
steps.

Before starting outputting calculation results, the solver should check
whether user canceled calculation. If canceled, the solver should stop.

In solver definition files, no definition is written about the
calculation results the solver output. So, you do not have to take care
about the correspondence relation between solver definition file and the
solver code about them.

:numref:`solver_with_outputting` shows the source code with
lines to output time and
calculations. The added lines are shown with highlight.

.. code-block:: fortran
   :caption: Source code with lines to output time and calculation results
   :name: solver_with_outputting
   :linenos:

     ! (abbr.)
     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: elevation
     integer, dimension(:,:), allocatable:: obstacle
     double precision:: time
     integer:: iteration
     integer:: canceled
     integer:: locked
     double precision, dimension(:,:), allocatable:: velocity_x, velocity_y
     double precision, dimension(:,:), allocatable:: depth
     integer, dimension(:,:), allocatable:: wetflag
     double precision:: convergence

     ! (abbr.)

     ! Loads grid attributes 
     call cg_iric_read_grid_real_node(fin, "Elevation", elevation, ier)
     call cg_iric_read_grid_integer_cell(fin, "Obstacle", obstacle, ier)

     allocate(velocity_x(isize,jsize), velocity_y(isize,jsize), depth(isize,jsize), wetflag(isize,jsize))
     iteration = 0
     time = 0
     do
       time = time + timestep
       ! (Execute the calculation here. The grid shape changes.)

       call iric_check_cancel(canceled)
       if (canceled == 1) exit
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       ! Outputs grid
       call cg_iric_write_sol_grid2d_coords(fin, grid_x, grid_y, ier)
       ! Outputs calculation result
       call cg_iric_write_sol_node_real(fin, 'VelocityX', velocity_x, ier)
       call cg_iric_write_sol_node_real(fin, 'VelocityY', velocity_y, ier)
       call cg_iric_write_sol_node_real(fin, 'Depth', depth, ier)
       call cg_iric_write_sol_node_integer(fin, 'Wet', wetflag, ier)
       call cg_iric_write_sol_baseiterative_real(fin, 'Convergence', convergence, ier)
       call cg_iric_write_sol_end(fin, ier)
       iteration = iteration + 1
       if (iteration > maxiterations) exit
     end do
   
     ! Closes calculation data file
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram

Refer to :ref:`iriclib_output_time` and :ref:`iriclib_output_result`
for the details of the subroutines to
output time and calculation results. Refer to 
:ref:`iriclib_output_grid_in_sol` for the
details of the subroutines to output the grid coordinates in case of
moving grid.

For the calculation results, some special names is named in iRIC. You
should use that name for calculation results used for a certain purpose.
Refer to :ref:`special_result_names` for the special names.
