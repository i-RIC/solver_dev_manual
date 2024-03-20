.. _sec_ref_cg_iRIC_Write_Sol_Time:

cg_iRIC_Write_Sol_Time
======================

Writes time.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_Time(fid, time, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_Time(fid, time)

Format (Python)
-----------------

.. code-block:: python

   cg_iRIC_Write_Sol_Time(fid, time)

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

time
~~~~

.. list-table:: Description of time
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - time
   * - Input/Output
     - Input

   * - Description
     - Time
   * - Data type (FORTRAN)
     - double precision
   * - Data type (C/C++)
     - double
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

