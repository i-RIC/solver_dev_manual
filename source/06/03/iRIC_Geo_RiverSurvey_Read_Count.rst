.. _sec_ref_iRIC_Geo_RiverSurvey_Read_Count:

iRIC_Geo_RiverSurvey_Read_Count
===============================

Reads the number of the cross-sections in cross-section data.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_Count(geo_handle, count, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_Count(geo_handle, count)

Format (Python)
-----------------

.. code-block:: python

   count = iRIC_Geo_RiverSurvey_Read_Count(geo_handle)

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

