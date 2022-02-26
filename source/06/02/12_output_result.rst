.. _iriclib_output_result:

Outputting calculation results
==================================

Outputs the calculation results to the CGNS file.

The calculation result types that iRIClib can output are as follows:

* One value for each time step
* Value defined at grid nodes
* Value defined at grid cells
* Value defined at grid edges
* Value defined at particles
* Value defined at particles (groups supported)
* Value defined at polygon or polydata

In case of outputting every types, you have to use the
functions in :numref:`table_iriclib_output_start_and_end_functions`
and :numref:`table_iriclib_output_time_functions`.

Please refer to :ref:`iriclib_output_result_baseiterative`
to :ref:`iriclib_output_result_polydata` for detailed procedure to 
output each types.

.. _table_iriclib_output_start_and_end_functions:

.. list-table:: Subroutines to use before and after outputting calculation result for each timestep
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - iric_check_cancel
     - Checks whether user canceled solver execution

   * - cg_iric_write_sol_start
     - Starts outputting calculation result

   * - cg_iric_write_sol_end
     - Ends outputting calculation result

.. _table_iriclib_output_time_functions:

.. list-table:: Subroutines to output time and iteration count
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_write_sol_time
     - Outputs time

   * - cg_iric_write_sol_iteration
     - Outputs iteration count

.. note:: Vector quantities and scalar quantities

   In iRIClib, the same subroutines are used to output vector quantities and
   scalar quantities.
   
   When outputting vector quantities,
   output each component with names like \"VelocityX\" and \"VelocityY\".

   Please note that if you use names whose last character is \"X\", \"Y\", or \"Z\",
   the value is not loaded properly by GUI, and user can not visualize the value.
   You can use lower case letters "\x\", \"y\", or \"z\" instead.

.. note:: Special names for calculation results

   For calculation results, iRIC defines special names, and when you want to output
   calculation result for certain purposes, you should use those names.
   Refer to :ref:`special_result_names` for those names.

.. note:: Grid nodes, grid cells, and grid edges

   For grid related values, now iRIClib has function to output values defined at
   grid nodes, grid cells and grid edges.

   Basically, please select the functions so that you can output the values at the
   position where the variable is defined in your solver.

   There is an exception: Please output vector quantities at grid nodes.
   If you output vector quantities at grid cells, iRIC GUI can not visualize
   arrows, streamlines or particles for that value.

.. toctree::
   :maxdepth: 1

   12_01_output_result_baseiterative
   12_02_output_result_gridnode
   12_03_output_result_gridcell
   12_04_output_result_gridedge
   12_05_output_result_particle
   12_06_output_result_particlegroup
   12_07_output_result_polydata
