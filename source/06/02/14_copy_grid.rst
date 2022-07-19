Copy grid
========================

Copy grid between two CGNS files.
The function can be used for both structured grids and unstructured grids.

.. list-table:: 利用する関数
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_copy_grid
     - Copys the grid

:numref:`example_copy_grid` shows an example of opening two CGNS files, 
and copy the grid from one to another.

.. code-block:: fortran
   :caption: Example source code to copy grid
   :name: example_copy_grid
   :linenos:

   program SampleX
     use iric
     implicit none

     integer:: fid_from, fid_to, ier

     ! Opens CGNS files
     call cg_iric_open('test1.cgn', IRIC_MODE_READ, fid_from, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     call cg_iric_open('test1.cgn', IRIC_MODE_MODIFY, fid_to, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! Copy grid
     call cg_iric_copy_grid(fid_from, fid_to, ier)

     ! Closes CGNS files
     call cg_iric_close(fid_from, ier)
     call cg_iric_close(fid_to, ier)
     stop
   end program SampleX
