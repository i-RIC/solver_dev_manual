.. _sec_ref_iRIC_Geo_Polygon_Read_HolePoints:

iRIC_Geo_Polygon_Read_HolePoints
================================

Reads the coordinates of hole polygon vertices.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_Polygon_Read_HolePoints(geo_handle, holeid, x_arr, y_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_Polygon_Read_HolePoints(geo_handle, holeid, x_arr, y_arr)

Format (Python)
-----------------

.. code-block:: python

   x_arr, y_arr = iRIC_Geo_Polygon_Read_HolePoints(geo_handle, holeid)

Arguments and returned value
-------------------------------

geo_handle
~~~~~~~~~~

.. list-table:: Description of geo_handle
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - geo_handle
   * - Input/Output
     - Input

   * - Description
     - Handle of geographic data
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

holeid
~~~~~~

.. list-table:: Description of holeid
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - holeid
   * - Input/Output
     - Input

   * - Description
     - Polygon hole ID (Start from 1)
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

