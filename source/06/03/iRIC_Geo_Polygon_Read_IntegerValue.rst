.. _sec_ref_iRIC_Geo_Polygon_Read_IntegerValue:

iRIC_Geo_Polygon_Read_IntegerValue
==================================

Reads the value of polygon data as integer.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_Polygon_Read_IntegerValue(geo_handle, value, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_Polygon_Read_IntegerValue(geo_handle, value)

Format (Python)
-----------------

.. code-block:: python

   value = iRIC_Geo_Polygon_Read_IntegerValue(geo_handle)

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

value
~~~~~

.. list-table:: Description of value
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - value
   * - Input/Output
     - Output

   * - Description
     - The value of the condition
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

