.. _sec_ref_cg_iRIC_Read_Sol_BaseIterative_String:

cg_iRIC_Read_Sol_BaseIterative_String
=====================================

complex type the Reads calculation result defined globally.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Sol_BaseIterative_String(fid, step, name, strvalue, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Sol_BaseIterative_String(fid, step, name, strvalue)

Format (Python)
-----------------

.. code-block:: python

   strvalue = cg_iRIC_Read_Sol_BaseIterative_String(fid, step, name)

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

step
~~~~

.. list-table:: Description of step
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - step
   * - Input/Output
     - Input

   * - Description
     - The result step number
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
     - The name of the calculation result
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

strvalue
~~~~~~~~

.. list-table:: Description of strvalue
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - strvalue
   * - Input/Output
     - Output

   * - Description
     - The value of the calculation result
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - char*
   * - Data type (Python)
     - str

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

