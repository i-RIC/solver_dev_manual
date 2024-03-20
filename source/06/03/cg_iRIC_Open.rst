.. _sec_ref_cg_iRIC_Open:

cg_iRIC_Open
============

Opens a CGNS file.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Open(filename, mode, fid, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Open(filename, mode, fid)

Format (Python)
-----------------

.. code-block:: python

   fid = cg_iRIC_Open(filename, mode)

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

mode
~~~~

.. list-table:: Description of mode
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - mode
   * - Input/Output
     - Input

   * - Description
     - Mode (IRIC_MODE_READ, IRIC_MODE_WRITE or IRIC_MODE_MODIFY)
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

fid
~~~

.. list-table:: Description of fid
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - fid
   * - Input/Output
     - Output

   * - Description
     - File ID
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

