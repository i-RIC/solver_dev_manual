Adding grid generating data file opening and closing codes
-----------------------------------------------------------

Adds codes for opening and closing grid generating data file.

The grid generating program has to open calculation data file in the
first step, and close it in the last step.

iRIC will handle the file name of grid generating data file as the first
argument, so open that file.

The way to handle the number of arguments is described in :ref:`handling_arguments`.

:numref:`gridgenerator_with_open_close` shows the source code with the
lines to open and close grid
generating data file. The added lines are shown with highlight.

.. code-block:: fortran
   :caption: The source code with lines to open and close file
   :name: gridgenerator_with_open_close
   :linenos:

   program SampleProgram
     use iric
     implicit none
   
     integer:: fin, ier
     integer:: icount, istatus
   
     character(200)::condFile
   
     icount = nargs()
     if ( icount.eq.2 ) then
       call getarg(1, condFile, istatus)
     else
       stop "Input File not specified."
     endif
   
     ! Opens grid generating data file
     call cg_iric_open(condFile, IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! Closes grid generating data file
     call cg_iric_close(fin, ier)
   end program SampleProgram

Compile the executable file, just like in :ref:`gridgenerator_dev_skeleton`.

Check that the source code can be compiled successfully.

Refer to :ref:`iriclib_open_cgns` and
:ref:`iriclib_close_cgns` for the details of the
subroutines added in this section.
