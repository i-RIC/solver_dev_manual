.. _handling_arguments:

Handling command line arguments in Fortran programs
======================================================

When iRIC launches solvers (or grid generating programs), the name of
calculation data file (or grid generating data file) is passed as
an argument. So, solvers (or grid generating programs) have to process
the file name and opens that file.

In FORTRAN, the functions prepared for handling arguments are
different by compilers. In this section, functions for handling
arguments are explained for Intel Fortran Complier.

Intel Fortran Compiler
------------------------

Obtain the number of command line arguments using nargs(),
and obtain the argument value using getarg().

.. code-block:: fortran
   :caption: Example source code for reading arguments for Intel Fortran Compiler
   :linenos:

   icount = nargs()  ! The number includes the executable name, so if user passed one argument, 2 is returned.
   if ( icount.eq.2 ) then
     call getarg(1, condFile, istatus)
   else
     write(*,*) "Input File not specified."
     stop
   endif
