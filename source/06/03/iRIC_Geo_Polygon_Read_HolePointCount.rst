.. _sec_ref_iRIC_Geo_Polygon_Read_HolePointCount:

iRIC_Geo_Polygon_Read_HolePointCount
====================================

Reads the number of vertices of hole polygon.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_Polygon_Read_HolePointCount(geo_handle, holeid, count, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_Polygon_Read_HolePointCount(geo_handle, holeid, count)

Format (Python)
-----------------

.. code-block:: python

   count = iRIC_Geo_Polygon_Read_HolePointCount(geo_handle, holeid)

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
     - The number of vertices constituting the hole polygon
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

