.. _sec_ref_cg_iRIC_Read_Grid2d_Str_Size:

cg_iRIC_Read_Grid2d_Str_Size
============================

Reads the size of the structured grid (the number of nodes in I-direction and J-direction). 

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_Str_Size(fid, isize, jsize, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Str_Size(fid, isize, jsize)

Format (Python)
-----------------

.. code-block:: python

   isize, jsize = cg_iRIC_Read_Grid2d_Str_Size(fid)

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

isize
~~~~~

.. list-table:: Description of isize
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - isize
   * - Input/Output
     - Output

   * - Description
     - The number of grid nodes in I-direction
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int*
   * - Data type (Python)
     - int

jsize
~~~~~

.. list-table:: Description of jsize
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - jsize
   * - Input/Output
     - Output

   * - Description
     - The number of grid nodes in J-direction
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

