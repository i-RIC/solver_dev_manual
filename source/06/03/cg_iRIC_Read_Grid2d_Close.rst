.. _sec_ref_cg_iRIC_Read_Grid2d_Close:

cg_iRIC_Read_Grid2d_Close
=========================

Closes the grid opened with :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_Close(grid_handle, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Close(grid_handle)

Format (Python)
-----------------

.. code-block:: python

   cg_iRIC_Read_Grid2d_Close(grid_handle)

Arguments and returned value
-------------------------------

grid_handle
~~~~~~~~~~~

.. list-table:: Description of grid_handle
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - grid_handle
   * - Input/Output
     - Input

   * - Description
     - The handle of the grid
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

