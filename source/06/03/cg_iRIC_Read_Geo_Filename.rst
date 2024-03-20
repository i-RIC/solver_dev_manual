.. _sec_ref_cg_iRIC_Read_Geo_Filename:

cg_iRIC_Read_Geo_Filename
=========================

Reads the file name and data type of geographic data.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Geo_Filename(fid, name, geoid, strvalue, type, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Geo_Filename(fid, name, geoid, strvalue, type)

Format (Python)
-----------------

.. code-block:: python

   strvalue, type = cg_iRIC_Read_Geo_Filename(fid, name, geoid)

Arguments and returned value
-------------------------------

fid
~~~

.. list-table:: Description of fid
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - fid
   * - Input/Output
     - Input

   * - Description
     - File ID
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
     - Input

   * - Description
     - The name of the geographic data
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

geoid
~~~~~

.. list-table:: Description of geoid
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - geoid
   * - Input/Output
     - Input

   * - Description
     - ID of geographic data (Start from 1)
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
     - File name
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - char*
   * - Data type (Python)
     - str

type
~~~~

.. list-table:: Description of type
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - type
   * - Input/Output
     - Output

   * - Description
     - Type of geographic data (1: polygon, 2 = cross-section data)
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

