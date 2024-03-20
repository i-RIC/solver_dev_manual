.. _sec_ref_cg_iRIC_Write_BC_Functional_WithGridId:

cg_iRIC_Write_BC_Functional_WithGridId
======================================

Writes the variable values (X, Y) of functional boundary condition.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_BC_Functional_WithGridId(fid, gid, type, num, name, length, x_arr, y_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_BC_Functional_WithGridId(fid, gid, type, num, name, length, x_arr, y_arr)

Format (Python)
-----------------

.. code-block:: python

   x_arr, y_arr = cg_iRIC_Write_BC_Functional_WithGridId(fid, gid, type, num, name, length)

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

gid
~~~

.. list-table:: Description of gid
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - gid
   * - Input/Output
     - Input

   * - Description
     - Grid ID (Start from 1)
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

name
~~~~

.. list-table:: Description of name
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - name
   * - Input/Output
     - Input

   * - Description
     - The name of the variable
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

length
~~~~~~

.. list-table:: Description of length
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - length
   * - Input/Output
     - Input

   * - Description
     - The number of the valus of the condition
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

x_arr
~~~~~

.. list-table:: Description of x_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - x_arr
   * - Input/Output
     - Output

   * - Description
     - The array of X values
   * - Data type (FORTRAN)
     - double precision, dimension(:)
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - numpy.array

y_arr
~~~~~

.. list-table:: Description of y_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - y_arr
   * - Input/Output
     - Output

   * - Description
     - The array of Y values
   * - Data type (FORTRAN)
     - double precision, dimension(:)
   * - Data type (C/C++)
     - double*
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

