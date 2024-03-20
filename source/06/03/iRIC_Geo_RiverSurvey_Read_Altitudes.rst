.. _sec_ref_iRIC_Geo_RiverSurvey_Read_Altitudes:

iRIC_Geo_RiverSurvey_Read_Altitudes
===================================

Reads the altitude data of the cross-section.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_Altitudes(geo_handle, csid, position_arr, height_arr, active_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_Altitudes(geo_handle, csid, position_arr, height_arr, active_arr)

Format (Python)
-----------------

.. code-block:: python

   position_arr, height_arr, active_arr = iRIC_Geo_RiverSurvey_Read_Altitudes(geo_handle, csid)

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

position_arr
~~~~~~~~~~~~

.. list-table:: Description of position_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - position_arr
   * - Input/Output
     - Output

   * - Description
     - Altitude position (less than 0: left bank side, grater than 0: right bank side) values
   * - Data type (FORTRAN)
     - double precision, dimension(:)
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - numpy.array

height_arr
~~~~~~~~~~

.. list-table:: Description of height_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - height_arr
   * - Input/Output
     - Output

   * - Description
     - Altitude height (elevation) values
   * - Data type (FORTRAN)
     - double precision, dimension(:)
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - numpy.array

active_arr
~~~~~~~~~~

.. list-table:: Description of active_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - active_arr
   * - Input/Output
     - Output

   * - Description
     - Altitude data active/inactive (1: active, 0: inactive)
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

