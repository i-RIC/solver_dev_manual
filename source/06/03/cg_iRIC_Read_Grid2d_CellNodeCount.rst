.. _sec_ref_cg_iRIC_Read_Grid2d_CellNodeCount:

cg_iRIC_Read_Grid2d_CellNodeCount
=================================

Reads the number of nodes in the specified cell.

The value of g_handle that should be passed to this function, can be obtained by calling :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open` or :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_CellNodeCount(grid_handle, cellId, count, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_CellNodeCount(grid_handle, cellId, count)

Format (Python)
-----------------

.. code-block:: python

   count = cg_iRIC_Read_Grid2d_CellNodeCount(grid_handle, cellId)

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

cellId
~~~~~~

.. list-table:: Description of cellId
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - cellId
   * - Input/Output
     - Input

   * - Description
     - Cell ID (Start from 1)
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

count
~~~~~

.. list-table:: Description of count
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - count
   * - Input/Output
     - Output

   * - Description
     - The number of nodes constituting a cell
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

