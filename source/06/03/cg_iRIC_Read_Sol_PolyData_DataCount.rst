.. _sec_ref_cg_iRIC_Read_Sol_PolyData_DataCount:

cg_iRIC_Read_Sol_PolyData_DataCount
===================================

Reads the number of calculation results defined at polygons or poly lines.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Sol_PolyData_DataCount(fid, step, groupname, count, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Sol_PolyData_DataCount(fid, step, groupname, count)

Format (Python)
-----------------

.. code-block:: python

   count = cg_iRIC_Read_Sol_PolyData_DataCount(fid, step, groupname)

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
     - The name of the polygon (or polyline) group
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

count
~~~~~

.. list-table:: Description of count
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - count
   * - Input/Output
     - Output

   * - Description
     - The number of polygons (or poly lines)
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int*
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

