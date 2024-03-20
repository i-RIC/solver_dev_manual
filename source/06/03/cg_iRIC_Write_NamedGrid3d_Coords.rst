.. _sec_ref_cg_iRIC_Write_NamedGrid3d_Coords:

cg_iRIC_Write_NamedGrid3d_Coords
================================

Write the three dimensional structured grid.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_NamedGrid3d_Coords(fid, name, isize, jsize, ksize, x_arr, y_arr, z_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid3d_Coords(fid, name, isize, jsize, ksize, x_arr, y_arr, z_arr)

Format (Python)
-----------------

.. code-block:: python

   x_arr, y_arr, z_arr = cg_iRIC_Write_NamedGrid3d_Coords(fid, name, isize, jsize, ksize)

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

name
~~~~

.. list-table:: Description of name
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - name
   * - Input/Output
     - Input

   * - Description
     - The name of the grid
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

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

jsize
~~~~~

.. list-table:: Description of jsize
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - jsize
   * - Input/Output
     - Input

   * - Description
     - The number of grid nodes in J-direction
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

ksize
~~~~~

.. list-table:: Description of ksize
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - ksize
   * - Input/Output
     - Input

   * - Description
     - The number of grid nodes in K-direction
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

y_arr
~~~~~

.. list-table:: Description of y_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - y_arr
   * - Input/Output
     - Output

   * - Description
     - The array of coordinate Y values
   * - Data type (FORTRAN)
     - double precision, dimension(:)
   * - Data type (C/C++)
     - double*
   * - Data type (Python)
     - numpy.array

z_arr
~~~~~

.. list-table:: Description of z_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - z_arr
   * - Input/Output
     - Output

   * - Description
     - The array of coordinate Z values
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

