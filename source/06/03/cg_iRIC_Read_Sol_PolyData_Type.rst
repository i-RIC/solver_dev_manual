.. _sec_ref_cg_iRIC_Read_Sol_PolyData_Type:

cg_iRIC_Read_Sol_PolyData_Type
==============================

Reads the types of calculation results defined at polygons or poly lines.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Sol_PolyData_Type(fid, step, groupname, v_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Sol_PolyData_Type(fid, step, groupname, v_arr)

Format (Python)
-----------------

.. code-block:: python

   v_arr = cg_iRIC_Read_Sol_PolyData_Type(fid, step, groupname)

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
     - The array of data types (1: polygon, 2: poly line)
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

