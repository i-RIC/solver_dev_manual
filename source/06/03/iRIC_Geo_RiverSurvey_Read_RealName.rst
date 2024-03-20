.. _sec_ref_iRIC_Geo_RiverSurvey_Read_RealName:

iRIC_Geo_RiverSurvey_Read_RealName
==================================

Reads the name of the crosssection as real number.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_RealName(geo_handle, csid, name, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_RealName(geo_handle, csid, name)

Format (Python)
-----------------

.. code-block:: python

   name = iRIC_Geo_RiverSurvey_Read_RealName(geo_handle, csid)

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

name
~~~~

.. list-table:: Description of name
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - name
   * - Input/Output
     - Output

   * - Description
     - The name of the geographic data
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

