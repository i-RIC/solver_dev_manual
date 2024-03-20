.. _sec_ref_cg_iRIC_Write_Sol_PolyData_Polygon:

cg_iRIC_Write_Sol_PolyData_Polygon
==================================

Writes the polygon shape for the calculation result defined as polygons.

:ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin or :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin_WithGridId` should be called before calling this function.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_PolyData_Polygon(fid, numPoints, x_arr, y_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_PolyData_Polygon(fid, numPoints, x_arr, y_arr)

Format (Python)
-----------------

.. code-block:: python

   x_arr, y_arr = cg_iRIC_Write_Sol_PolyData_Polygon(fid, numPoints)

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

numPoints
~~~~~~~~~

.. list-table:: Description of numPoints
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - numPoints
   * - Input/Output
     - Input

   * - Description
     - The number of vertices in the polygon of polyline
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
     - The array of coordinate X values
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
     - The array of coordinate Y values
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

