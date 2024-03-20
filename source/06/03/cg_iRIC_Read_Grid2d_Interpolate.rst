.. _sec_ref_cg_iRIC_Read_Grid2d_Interpolate:

cg_iRIC_Read_Grid2d_Interpolate
===============================

Returns the information to interpolate the value at the specified coordinates, with the values defined at grid nodes.

The value of g_handle that should be passed to this function, can be obtained by calling :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open` or :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid2d_Interpolate(grid_handle, x, y, ok, count, nodeids_arr, weights_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Interpolate(grid_handle, x, y, ok, count, nodeids_arr, weights_arr)

Format (Python)
-----------------

.. code-block:: python

   ok, count, nodeids_arr, weights_arr = cg_iRIC_Read_Grid2d_Interpolate(grid_handle, x, y)

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

ok
~~

.. list-table:: Description of ok
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - ok
   * - Input/Output
     - Output

   * - Description
     - 1 if a cell is found, 0 if not
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int*
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
     - The number of nodes of the cell that contains the specified point
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int*
   * - Data type (Python)
     - int

nodeids_arr
~~~~~~~~~~~

.. list-table:: Description of nodeids_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - nodeids_arr
   * - Input/Output
     - Output

   * - Description
     - The array of IDs of grid nodes constituting the cell (start from 1)
   * - Data type (FORTRAN)
     - integer, dimension(:)
   * - Data type (C/C++)
     - int*
   * - Data type (Python)
     - numpy.array

weights_arr
~~~~~~~~~~~

.. list-table:: Description of weights_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - weights_arr
   * - Input/Output
     - Output

   * - Description
     - The array of weight values to interpolate the value at the coordinates from the those defined at cell vertices
   * - Data type (FORTRAN)
     - double precision, dimension(:)
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - numpy.array

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

