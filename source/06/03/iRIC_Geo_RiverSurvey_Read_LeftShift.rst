.. _sec_ref_iRIC_Geo_RiverSurvey_Read_LeftShift:

iRIC_Geo_RiverSurvey_Read_LeftShift
===================================

Reads the shift offset value of the cross-section.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_LeftShift(geo_handle, csid, shift, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_LeftShift(geo_handle, csid, shift)

Format (Python)
-----------------

.. code-block:: python

   shift = iRIC_Geo_RiverSurvey_Read_LeftShift(geo_handle, csid)

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

shift
~~~~~

.. list-table:: Description of shift
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - shift
   * - Input/Output
     - Output

   * - Description
     - The amount of left shift
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

