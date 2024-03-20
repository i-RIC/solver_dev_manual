.. _sec_ref_cg_iRIC_Read_BC_Indices:

cg_iRIC_Read_BC_Indices
=======================

Reads the elements (nodes, cells, or edges) where the boundary condition is defined.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_BC_Indices(fid, type, num, idx_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_BC_Indices(fid, type, num, idx_arr)

Format (Python)
-----------------

.. code-block:: python

   idx_arr = cg_iRIC_Read_BC_Indices(fid, type, num)

Arguments and returned value
-------------------------------

fid
~~~

.. list-table:: Description of fid
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - fid
   * - Input/Output
     - Input

   * - Description
     - File ID
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

type
~~~~

.. list-table:: Description of type
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - type
   * - Input/Output
     - Input

   * - Description
     - The name of the boundary condition
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

num
~~~

.. list-table:: Description of num
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - num
   * - Input/Output
     - Input

   * - Description
     - Boundary condition number
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

idx_arr
~~~~~~~

.. list-table:: Description of idx_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - idx_arr
   * - Input/Output
     - Output

   * - Description
     - The array of index values
   * - Data type (FORTRAN)
     - integer, dimension(:)
   * - Data type (C/C++)
     - int*
   * - Data type (Python)
     - numpy.array

ier
~~~

.. list-table:: Description of ier
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - ier
   * - Input/Output
     - Output

   * - Description
     - Error code. 0 means success, other values mean error.
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - (Not defined)

