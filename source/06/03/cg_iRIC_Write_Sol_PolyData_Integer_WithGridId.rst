.. _sec_ref_cg_iRIC_Write_Sol_PolyData_Integer_WithGridId:

cg_iRIC_Write_Sol_PolyData_Integer_WithGridId
=============================================

Writes the integer calculation result defined at grid polygons or poly lines.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_PolyData_Integer_WithGridId(fid, gid, name, value, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_PolyData_Integer_WithGridId(fid, gid, name, value)

Format (Python)
-----------------

.. code-block:: python

   cg_iRIC_Write_Sol_PolyData_Integer_WithGridId(fid, gid, name, value)

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

value
~~~~~

.. list-table:: Description of value
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - value
   * - Input/Output
     - Input

   * - Description
     - The value of the calculation result
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

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

