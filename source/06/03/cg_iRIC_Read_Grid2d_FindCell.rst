.. _sec_ref_cg_iRIC_Read_Grid2d_FindCell:

cg_iRIC_Read_Grid2d_FindCell
============================

Finds and returns the ID of the cell that includes the specified coordinates.

The value of g_handle that should be passed to this function, can be obtained by calling :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open` or :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_FindCell(grid_handle, x, y, cellId, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_FindCell(grid_handle, x, y, cellId)

Format (Python)
-----------------

.. code-block:: python

   cellId = cg_iRIC_Read_Grid2d_FindCell(grid_handle, x, y)

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

x
~

.. list-table:: Description of x
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - x
   * - Input/Output
     - Input

   * - Description
     - X coordinate value
   * - Data type (FORTRAN)
     - double precision
   * - Data type (C/C++)
     - double
   * - Data type (Python)
     - float

y
~

.. list-table:: Description of y
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - y
   * - Input/Output
     - Input

   * - Description
     - Y coordinate value
   * - Data type (FORTRAN)
     - double precision
   * - Data type (C/C++)
     - double
   * - Data type (Python)
     - float

cellId
~~~~~~

.. list-table:: Description of cellId
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - cellId
   * - Input/Output
     - Output

   * - Description
     - Cell ID (Start from 1)
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

