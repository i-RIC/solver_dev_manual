.. _sec_ref_cg_iRIC_Read_BC_StringLen_WithGridId:

cg_iRIC_Read_BC_StringLen_WithGridId
====================================

Reads the length of a string boundary condition.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_BC_StringLen_WithGridId(fid, gid, type, num, name, length, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_BC_StringLen_WithGridId(fid, gid, type, num, name, length)

Format (Python)
-----------------

.. code-block:: python

   length = cg_iRIC_Read_BC_StringLen_WithGridId(fid, gid, type, num, name)

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
     - Input

   * - Description
     - Boundary condition number
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
     - The name of the variable
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

length
~~~~~~

.. list-table:: Description of length
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - length
   * - Input/Output
     - Output

   * - Description
     - The length of the string
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

