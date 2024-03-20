.. _sec_ref_cg_iRIC_Read_Grid_TriangleElementsSize:

cg_iRIC_Read_Grid_TriangleElementsSize
======================================

Reads the size of array needed to load the IDs of nodes for each triangles in an unstructured grid.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid_TriangleElementsSize(fid, tsize, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid_TriangleElementsSize(fid, tsize)

Format (Python)
-----------------

.. code-block:: python

   tsize = cg_iRIC_Read_Grid_TriangleElementsSize(fid)

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

tsize
~~~~~

.. list-table:: Description of tsize
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - tsize
   * - Input/Output
     - Output

   * - Description
     - The number of triangles
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

