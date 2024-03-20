.. _sec_ref_iRIC_Geo_RiverSurvey_Read_Position:

iRIC_Geo_RiverSurvey_Read_Position
==================================

Reads the coordinates of the cross-section center point.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_Position(geo_handle, csid, x, y, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_Position(geo_handle, csid, x, y)

Format (Python)
-----------------

.. code-block:: python

   x, y = iRIC_Geo_RiverSurvey_Read_Position(geo_handle, csid)

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

csid
~~~~

.. list-table:: Description of csid
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - csid
   * - Input/Output
     - Input

   * - Description
     - Cross-Section ID (Start from 1)
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

x
~

.. list-table:: Description of x
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - x
   * - Input/Output
     - Output

   * - Description
     - X coordinate value
   * - Data type (FORTRAN)
     - double precision
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - float

y
~

.. list-table:: Description of y
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - y
   * - Input/Output
     - Output

   * - Description
     - Y coordinate value
   * - Data type (FORTRAN)
     - double precision
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - float

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

