.. _sec_ref_cg_iRIC_Read_RealSingle:

cg_iRIC_Read_RealSingle
=======================

Reads the value of a single-precision real calculation condition.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_RealSingle(fid, name, value, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_RealSingle(fid, name, value)

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

value
~~~~~

.. list-table:: Description of value
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - value
   * - Input/Output
     - Output

   * - Description
     - The value of the condition
   * - Data type (FORTRAN)
     - real
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

