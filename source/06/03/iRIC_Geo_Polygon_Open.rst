.. _sec_ref_iRIC_Geo_Polygon_Open:

iRIC_Geo_Polygon_Open
=====================

Opens the geographic data file that contains polygon data.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Geo_Polygon_Open(filename, geo_handle, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_Geo_Polygon_Open(filename, geo_handle)

Format (Python)
-----------------

.. code-block:: python

   geo_handle = iRIC_Geo_Polygon_Open(filename)

Arguments and returned value
-------------------------------

filename
~~~~~~~~

.. list-table:: Description of filename
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - filename
   * - Input/Output
     - Input

   * - Description
     - File name
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

geo_handle
~~~~~~~~~~

.. list-table:: Description of geo_handle
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - geo_handle
   * - Input/Output
     - Output

   * - Description
     - Handle of geographic data
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

