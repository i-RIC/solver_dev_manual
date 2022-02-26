.. _iriclib_output_time:

Outputting time (or iteration count)
=====================================

Outputs the timestamp information or the iteration count to the CGNS file.

Be sure to perform this before outputting the calculation grid or calculation results.

Also note that the time and iteration-count information cannot be output
at the same time. Output either, not both. 

.. list-table:: Subroutines to use
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_write_sol_start
     - Starts outputting calculation results

   * - cg_iric_write_sol_end
     - Ends outputting calculation results

   * - cg_iric_write_sol_time
     - Outputs time

   * - cg_iric_write_sol_iteration
     - Outputs iteration count

:numref:`example_output_time` shows an example of source code to
output timestamp information.

.. code-block:: fortran
   :caption: Example of source code to output time
   :name: example_output_time
   :linenos:

   program Sample4
     use iric
     implicit none
   
     integer:: fin, ier, i
     double precision:: time
   
     ! Open CGNS file.
     call cg_iric_open('test.cgn', IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Output the initial state information.
     time = 0
   
     call cg_iric_write_sol_start(fin, ier)
     call cg_iric_write_sol_time(fin, time, ier)
     ! (Here, output initial calculation grid or calculation results.)
     call cg_iric_write_sol_end(fin, ier)
   
     do
       time = time + 10.0
       ! (Perform calculation here.)
       call cg_iric_write_sol_start(fin, ier)
       call cg_iric_write_sol_time(fin, time, ier)
       ! (Here, output calculation grid or calculation results.)
       call cg_iric_write_sol_end(fin, ier)
       If (time > 1000) exit
     end do
   
     ! Close CGNS file.
     call cg_iric_close(fin, ier)
     stop
   end program Sample4
