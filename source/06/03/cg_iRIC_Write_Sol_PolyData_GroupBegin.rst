.. _sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin:

cg_iRIC_Write_Sol_PolyData_GroupBegin
=====================================

Starts outputting calculation result defined at polygons or poly lines.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_PolyData_GroupBegin(fid, groupname, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_PolyData_GroupBegin(fid, groupname)

Format (Python)
-----------------

.. code-block:: python

   cg_iRIC_Write_Sol_PolyData_GroupBegin(fid, groupname)

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

