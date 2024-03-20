.. _sec_ref_cg_iRIC_Write_Grid1d_Coords:

cg_iRIC_Write_Grid1d_Coords
===========================

Write the one dimensional structured grid.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Grid1d_Coords(fid, isize, x_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Grid1d_Coords(fid, isize, x_arr)

Format (Python)
-----------------

.. code-block:: python

   x_arr = cg_iRIC_Write_Grid1d_Coords(fid, isize)

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
     - Input

   * - Description
     - The number of grid nodes in I-direction
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

x_arr
~~~~~

.. list-table:: Description of x_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - x_arr
   * - Input/Output
     - Output

   * - Description
     - The array of coordinate X values
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

