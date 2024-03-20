.. _sec_ref_iRIC_Geo_RiverSurvey_Read_FixedPointL:

iRIC_Geo_RiverSurvey_Read_FixedPointL
=====================================

Reads the data of left bank extension line of the cross-section.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_RiverSurvey_Read_FixedPointL(geo_handle, csid, set, dirx, diry, index, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_FixedPointL(geo_handle, csid, set, dirx, diry, index)

Format (Python)
-----------------

.. code-block:: python

   set, dirx, diry, index = iRIC_Geo_RiverSurvey_Read_FixedPointL(geo_handle, csid)

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

set
~~~

.. list-table:: Description of set
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - set
   * - Input/Output
     - Output

   * - Description
     - If defined, the value is 1, otherwise 0
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int*
   * - Data type (Python)
     - int

dirx
~~~~

.. list-table:: Description of dirx
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - dirx
   * - Input/Output
     - Output

   * - Description
     - X component of direction vector
   * - Data type (FORTRAN)
     - double precision
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - float

diry
~~~~

.. list-table:: Description of diry
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - diry
   * - Input/Output
     - Output

   * - Description
     - Y component of direction vector
   * - Data type (FORTRAN)
     - double precision
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - float

index
~~~~~

.. list-table:: Description of index
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - index
   * - Input/Output
     - Output

   * - Description
     - The ID of the altitude data where the left bank extension line starts
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

