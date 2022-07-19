.. _iriclib_load_bc:

Reading boundary conditions
=================================

Reads boundary conditions from CGNS file.

.. list-table:: Subroutine to use
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_read_bc_count
     - Reads the number of boundary condition

   * - cg_iric_read_bc_indicessize
     - Reads the number of nodes (or cells) where boundary condition is assigned.

   * - cg_iric_read_bc_indices
     - Reads the indices of nodes (or cells) where boundary condition is assigned.

   * - cg_iric_read_bc_integer
     - Reads a integer boundary condition value

   * - cg_iric_read_bc_real
     - Reads a double-precision real boundary condition value

   * - cg_iric_read_bc_realsingle
     - Reads a single-precision real boundary condition value

   * - cg_iric_read_bc_string
     - Reads a string-type boundary condition value

   * - cg_iric_read_bc_functionalsize
     - Reads a functional-type boundary condition value

   * - cg_iric_read_bc_functional
     - Reads a functional-type boundary condition value

   * - cg_iric_read_bc_functionalwithname
     - Reads a functional-type boundary condition value (with multiple values)

You can define multiple boundary conditions with the same type,
to one grid. For example, you can define multiple inflows to a grid,
and set discharge value for them independently.

:numref:`example_load_boundary_condition` shows an example to
read boundary conditions. In this example the number of inflows is read by
cg_iric_read_bc_count first, memories are allocated, and at last,
the values are loaded.

The name of boundary condition user specifys on iRIC GUI can be
loaded using cg_iric_read_bc_string. Please refer to 6.4.48 for detail.

.. code-block:: fortran
   :caption: Example of source code to read boundary conditions
   :name: example_load_boundary_condition
   :linenos:

   program Sample8
     use iric
     implicit none
   
     integer:: fin, ier, isize, jsize, ksize, i, j, k, aret
     integer:: condid, indexid
     integer:: condcount, indexlenmax, funcsizemax
     integer:: tmplen
     integer, dimension(:), allocatable:: condindexlen
     integer, dimension(:,:,:), allocatable:: condindices
     integer, dimension(:), allocatable:: intparam
     double precision, dimension(:), allocatable:: realparam
     character(len=200), dimension(:), allocatable:: stringparam
     character(len=200):: tmpstr
     integer, dimension(:), allocatable:: func_size
     double precision, dimension(:,:), allocatable:: func_param;
     double precision, dimension(:,:), allocatable:: func_value;
   
     ! Opens CGNS file
     call cg_iric_open('bctest.cgn', IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Initializes iRIClib 
     call cg_iric_init(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! Reads the number of inflows 
     call cg_iric_read_bc_count(fin, 'inflow', condcount)
     ! Allocate memory to load parameters 
     allocate(condindexlen(condcount), intparam(condcount), realparam(condcount))
     allocate(stringparam(condcount), func_size(condcount))
     print *, 'condcount ', condcount
   
     ! Reads the number of grid node indices where boundary condition is assigned, and the size of functional-type condition.
     indexlenmax = 0
     funcsizemax = 0
     do condid = 1, condcount
       call cg_iric_read_bc_indicessize(fin, 'inflow', condid, condindexlen(condid), ier)
       if (indexlenmax < condindexlen(condid)) then
         indexlenmax = condindexlen(condid)
       end if
       call cg_iric_read_bc_functionalsize(fin, 'inflow', condid, 'funcparam', func_size(condid), ier);
       if (funcsizemax < func_size(condid)) then
         funcsizemax = func_size(condid)
       end if
     end do
     
     ! Allocates memory to load grid node indices and functional-type boundary condition
     allocate(condindices(condcount, 2, indexlenmax))
     allocate(func_param(condcount, funcsizemax), func_value(condcount, funcsizemax))
     ! Loads indices and boundary condition 
     do condid = 1, condcount
       call cg_iric_read_bc_indices(fin, 'inflow', condid, condindices(condid:condid,:,:), ier)
       call cg_iric_read_bc_integer(fin, 'inflow', condid, 'intparam', intparam(condid:condid), ier)
       call cg_iric_read_bc_real(fin, 'inflow', condid, 'realparam', realparam(condid:condid), ier)
       call cg_iric_read_bc_string(fin, 'inflow', condid, 'stringparam', tmpstr, ier)
       stringparam(condid) = tmpstr
       call cg_iric_read_bc_functional(fin, 'inflow', condid, 'funcparam', func_param(condid:condid,:), func_value(condid:condid,:), ier)
     end do
   
     ! Displays the boundary condition loaded. 
     do condid = 1, condcount
       do indexid = 1, condindexlen(condid)
         print *, 'condindices ', condindices(condid:condid,:,indexid:indexid)
       end do
       print *, 'intparam ', intparam(condid:condid)
       print *, 'realparam ', realparam(condid:condid)
       print *, 'stringparam ', stringparam(condid)
       print *, 'funcparam X ', func_param(condid:condid, 1:func_size(condid))
       print *, 'funcparam Y ', func_value(condid:condid, 1:func_size(condid))
     end do
     
     ! Closes CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program Sample8
