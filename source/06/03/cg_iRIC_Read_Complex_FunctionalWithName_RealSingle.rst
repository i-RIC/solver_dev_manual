.. _sec_ref_cg_iRIC_Read_Complex_FunctionalWithName_RealSingle:

cg_iRIC_Read_Complex_FunctionalWithName_RealSingle
==================================================

Reads the variable values of functional complex type grid attribute, as single-precision real values. This should be used in case it has multiple values.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Complex_FunctionalWithName_RealSingle(fid, groupname, num, name, paramname, v_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Complex_FunctionalWithName_RealSingle(fid, groupname, num, name, paramname, v_arr)

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

groupname
~~~~~~~~~

.. list-table:: Description of groupname
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - groupname
   * - Input/Output
     - Input

   * - Description
     - The name of the complex condition
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
     - Group number
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

