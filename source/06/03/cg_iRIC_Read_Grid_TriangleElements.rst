.. _sec_ref_cg_iRIC_Read_Grid_TriangleElements:

cg_iRIC_Read_Grid_TriangleElements
==================================

Reads IDs of nodes constituting the triangles of the unstructured grid. 

You should pass an array with size (numcells * 3) for id_arr. The returned values of ids will be the IDs of nodes for each triangles. 1st, 2nd, 3rd values will be the IDs of nodes of the 1st triangle, 4th, 5th, 6th values will be the IDs of nodes of the 2nd triangle, etc.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid_TriangleElements(fid, id_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid_TriangleElements(fid, id_arr)

Format (Python)
-----------------

.. code-block:: python

   id_arr = cg_iRIC_Read_Grid_TriangleElements(fid)

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

id_arr
~~~~~~

.. list-table:: Description of id_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - id_arr
   * - Input/Output
     - Output

   * - Description
     - The array of IDs constituting the triangles (start from 1)
   * - Data type (FORTRAN)
     - integer, dimension(:)
   * - Data type (C/C++)
     - int*
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

