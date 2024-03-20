.. _sec_ref_cg_iRIC_Read_BC_FunctionalWithName_RealSingle_WithGridId:

cg_iRIC_Read_BC_FunctionalWithName_RealSingle_WithGridId
========================================================

Reads the variable values of functional boundary condition, as single-precision real values. This should be used in case it has multiple values.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_BC_FunctionalWithName_RealSingle_WithGridId(fid, gid, type, num, name, paramname, v_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_BC_FunctionalWithName_RealSingle_WithGridId(fid, gid, type, num, name, paramname, v_arr)

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

paramname
~~~~~~~~~

.. list-table:: Description of paramname
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - paramname
   * - Input/Output
     - Input

   * - Description
     - The name of the value
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*

v_arr
~~~~~

.. list-table:: Description of v_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - v_arr
   * - Input/Output
     - Output

   * - Description
     - The array of the values
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

