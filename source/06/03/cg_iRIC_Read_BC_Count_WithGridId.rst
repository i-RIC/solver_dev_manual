.. _sec_ref_cg_iRIC_Read_BC_Count_WithGridId:

cg_iRIC_Read_BC_Count_WithGridId
================================

Reads the number of boundary condition.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_BC_Count_WithGridId(fid, gid, type, num, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_BC_Count_WithGridId(fid, gid, type, num)

Format (Python)
-----------------

.. code-block:: python

   num = cg_iRIC_Read_BC_Count_WithGridId(fid, gid, type)

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

type
~~~~

.. list-table:: Description of type
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - type
   * - Input/Output
     - Input

   * - Description
     - The name of the boundary condition
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

num
~~~

.. list-table:: Description of num
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - num
   * - Input/Output
     - Output

   * - Description
     - Boundary condition number
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int*
   * - Data type (Python)
     - int

