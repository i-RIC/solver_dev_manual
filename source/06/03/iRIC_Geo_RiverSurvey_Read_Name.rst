.. _sec_ref_iRIC_Geo_RiverSurvey_Read_Name:

iRIC_Geo_RiverSurvey_Read_Name
==============================

Reads the name of the cross-section as string.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_Name(geo_handle, csid, strvalue, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_Name(geo_handle, csid, strvalue)

Format (Python)
-----------------

.. code-block:: python

   strvalue = iRIC_Geo_RiverSurvey_Read_Name(geo_handle, csid)

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

strvalue
~~~~~~~~

.. list-table:: Description of strvalue
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - strvalue
   * - Input/Output
     - Output

   * - Description
     - The name of the cross-section
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - char*
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

