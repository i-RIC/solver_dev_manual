.. _sec_ref_cg_iRIC_Write_Sol_ParticleGroup_Pos3d_WithGridId:

cg_iRIC_Write_Sol_ParticleGroup_Pos3d_WithGridId
================================================

Writes the positions of particles.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_ParticleGroup_Pos3d_WithGridId(fid, gid, x, y, z, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_ParticleGroup_Pos3d_WithGridId(fid, gid, x, y, z)

Format (Python)
-----------------

.. code-block:: python

   cg_iRIC_Write_Sol_ParticleGroup_Pos3d_WithGridId(fid, gid, x, y, z)

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

z
~

.. list-table:: Description of z
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - z
   * - Input/Output
     - Input

   * - Description
     - Z coordinate value
   * - Data type (FORTRAN)
     - double precision
   * - Data type (C/C++)
     - double
   * - Data type (Python)
     - float

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

