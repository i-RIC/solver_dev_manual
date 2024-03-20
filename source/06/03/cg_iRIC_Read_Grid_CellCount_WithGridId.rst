.. _sec_ref_cg_iRIC_Read_Grid_CellCount_WithGridId:

cg_iRIC_Read_Grid_CellCount_WithGridId
======================================

Reads the number of cells of the grid. 

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid_CellCount_WithGridId(fid, gid, count, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid_CellCount_WithGridId(fid, gid, count)

Format (Python)
-----------------

.. code-block:: python

   count = cg_iRIC_Read_Grid_CellCount_WithGridId(fid, gid)

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

gid
~~~

.. list-table:: Description of gid
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - gid
   * - Input/Output
     - Input

   * - Description
     - Grid ID (Start from 1)
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
     - The number of cells of the grid
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

