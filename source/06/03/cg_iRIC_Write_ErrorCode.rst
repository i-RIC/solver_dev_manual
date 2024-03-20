.. _sec_ref_cg_iRIC_Write_ErrorCode:

cg_iRIC_Write_ErrorCode
=======================

Writes error code.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_ErrorCode(fid, errorcode, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_ErrorCode(fid, errorcode)

Format (Python)
-----------------

.. code-block:: python

   cg_iRIC_Write_ErrorCode(fid, errorcode)

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

errorcode
~~~~~~~~~

.. list-table:: Description of errorcode
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - errorcode
   * - Input/Output
     - Input

   * - Description
     - Error code
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
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

