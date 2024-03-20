.. _sec_ref_cg_iRIC_Close:

cg_iRIC_Close
=============

Closes the CGNS file.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Close(fid, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Close(fid)

Format (Python)
-----------------

.. code-block:: python

   cg_iRIC_Close(fid)

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

