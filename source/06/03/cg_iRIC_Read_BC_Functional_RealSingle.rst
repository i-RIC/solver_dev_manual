.. _sec_ref_cg_iRIC_Read_BC_Functional_RealSingle:

cg_iRIC_Read_BC_Functional_RealSingle
=====================================

Reads the variable values (X, Y) of functional boundary condition, as single-precision real values.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_BC_Functional_RealSingle(fid, type, num, name, x_arr, y_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_BC_Functional_RealSingle(fid, type, num, name, x_arr, y_arr)

Format (Python)
-----------------

Not Defined for Python

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
     - real, dimension(:)
   * - Data type (C/C++)
     - float*

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
     - real, dimension(:)
   * - Data type (C/C++)
     - float*

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

