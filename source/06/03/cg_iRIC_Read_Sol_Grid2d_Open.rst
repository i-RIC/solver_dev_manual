.. _sec_ref_cg_iRIC_Read_Sol_Grid2d_Open:

cg_iRIC_Read_Sol_Grid2d_Open
============================

Opens the grid in calculation result. 

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Sol_Grid2d_Open(fid, step, grid_handle, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Sol_Grid2d_Open(fid, step, grid_handle)

Format (Python)
-----------------

.. code-block:: python

   grid_handle = cg_iRIC_Read_Sol_Grid2d_Open(fid, step)

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

step
~~~~

.. list-table:: Description of step
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - step
   * - Input/Output
     - Input

   * - Description
     - The result step number
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

grid_handle
~~~~~~~~~~~

.. list-table:: Description of grid_handle
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - grid_handle
   * - Input/Output
     - Output

   * - Description
     - The handle of the grid
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

