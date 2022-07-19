.. _how_to_link:

Linking iRIClib using Fortran
===============================================

When you develop solvers (or grid generating programs), you have to link
the program with iRIClib.

We will explain the procedure to compile the source code (solver.f90).
We assume that the settings for compilers (like path settings)
are already finished.

.. _linking_on_ifort:

Intel Fortran Compiler (Windows)
----------------------------------

Put solver.f, cgnsdll_x64_ifort.lib, iriclib_x64_ifort.lib, cgnslib_f.h, iriclib_f.h
in a same folder, move to that folder with command prompt, and run the following
command to create an executable file named solver.exe.

.. code-block:: batch

   ifort iric.f90 solver.f90 iriclib.lib /MD
