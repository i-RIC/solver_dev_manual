.. _solver_dev_add_open_close:

Adding calculation data file opening and closing codes
-------------------------------------------------------

Adds codes for opening and closing calculation data file.

The solver has to open calculation data file in the first step, and
close it in the last step.

iRIC will handle the file name of calculation data file as a the first
argument, so open that file.

The way to handle the number of arguments is described in :ref:`handling_arguments`.

Table :numref:`solver_with_open_close` shows the source code with the
lines to open and close calculation data file. The added lines are shown
with highlight.

.. code-block:: fortran
   :caption: The source code with lines to open and close file
   :name: solver_with_open_close
   :linenos:

   program SampleProgram
     use iric
     implicit none
     integer:: fin, ier
     integer:: icount, istatus
     character(200)::condFile

     write(*,*) "Sample Program"

     icount = nargs()
     if ( icount.eq.2 ) then
       call getarg(1, condFile, istatus)
     else
       write(*,*) "Input File not specified."
       stop
     endif

     ! Opens calculation data file.
     call cg_iric_open(condFile, IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"

     ! Closes calculation data file.
     call cg_iric_close(fin, ier)
     stop
   end program SampleProgram

Compile and deploy the executable file, just like in
:ref:`solver_dev_skeleton`.

Check whether it can be launched from iRIC successfully, just like in
:ref:`solver_dev_skeleton`.

Refer to :ref:`iriclib_open_cgns` and
:ref:`iriclib_close_cgns` for the details of the
subroutines added in this section.
