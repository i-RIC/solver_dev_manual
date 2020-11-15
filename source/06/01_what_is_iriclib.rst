What is iRIClib?
=================

iRIClib is a library for interfacing a river simulation solver with
iRIC.

iRIC uses a CGNS file for input/output to/from solvers and grid
generating programs. Input-output subroutines for CGNS files are
published as an open-source library called cgnslib (see :ref:`about_cgns` ).
However, describing the necessary input-output directly using cgnslib
would require complicated processing description.

Therefore, the iRIC project offers iRIClib as a library of wrapper
subroutines that makes possible the abbreviated description of
input-output processing which is frequently used by solvers that work
together with iRIC. With these subroutines, input-output processing of a
solver that performs calculation using a single structured grid can be
described easily.

Note that iRIClib does not offer subroutines necessary for a solver that
uses multiple grids or an unstructured grid. In case of such solvers, it
is necessary to use cgnslib subroutines directly.

This chapter describes the groups of subroutines included in iRIClib,
and examples of using them, along with compilation procedures.

Languages supported by iRIClib 
===============================

iRIClib is supported for the following languages:

* FORTRAN
* C/C++
* Python

In this manual examples are described with FORTRAN mainly.

In this section, how to use iRIClib from FORTRAN, C/C++, and Python are briefly explained.

Please note that arguments and returned values depends on the language. Please refer to
the subsections for each functions in :ref:`iriclib_reference`
about the format to use the functions from each languages.

FORTRAN
---------------

Call iRIClib functions after including the header, like shown in :numref:`iriclib_init_example_fortran`.

.. _iriclib_init_example_fortran:

.. code-block:: fortran
   :caption: Example of using iRIClib from FORTRAN
   :linenos:

   include 'iriclib_f.h'

   call cg_iric_init_f(fid, ier)

C/C++
------------

Call iRIClib functions after including the header, like shown in :numref:`iriclib_init_example_c`.

.. _iriclib_init_example_c:

.. code-block:: c
   :caption: Example of using iRIClib from C/C++
   :linenos:

   #include "iriclib.h"

   // (abbr.)
   ier = cg_iric_init(fid);

Python
------------

Call iRIClib functions after importing iric module, like shown in :numref:`iriclib_init_example_python`.

.. _iriclib_init_example_python:

.. code-block:: python
   :caption: Example of using iRIClib from Python
   :linenos:

   from iric import *

   cg_iric_init(fid)

How to read this chapter
=========================

In this chapter, first :ref:`iriclib_overview` explains what kinds of information
input/output iRIC assumes a solver to perform, and what subroutines are
available for each kind of processing. First, read Section to understand
the general concept of iRIClib.

Since :ref:`iriclib_overview` gives only an outline of subroutines, see 
:ref:`iriclib_reference` for detailed information, such as lists of arguments
for those subroutines.
