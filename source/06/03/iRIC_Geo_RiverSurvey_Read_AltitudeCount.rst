.. _sec_ref_iRIC_Geo_RiverSurvey_Read_AltitudeCount:

iRIC_Geo_RiverSurvey_Read_AltitudeCount
=======================================

Reads the number of altitude data of the cross-section.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_AltitudeCount(geo_handle, csid, count, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_AltitudeCount(geo_handle, csid, count)

Format (Python)
-----------------

.. code-block:: python

   count = iRIC_Geo_RiverSurvey_Read_AltitudeCount(geo_handle, csid)

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
     - The number of values
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

