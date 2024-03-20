.. _sec_ref_cg_iRIC_Read_Grid_Real_IFace:

cg_iRIC_Read_Grid_Real_IFace
============================

I-direction cell boudary faces (edges) the double precision real grid attribute values defined at Reads.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Grid_Real_IFace(fid, name, v_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Grid_Real_IFace(fid, name, v_arr)

Format (Python)
-----------------

.. code-block:: python

   v_arr = cg_iRIC_Read_Grid_Real_IFace(fid, name)

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
     - The name of the grid attribute
   * - Data type (FORTRAN)
     - character(*)
   * - Data type (C/C++)
     - const char*
   * - Data type (Python)
     - str

v_arr
~~~~~

.. list-table:: Description of v_arr
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - v_arr
   * - Input/Output
     - Output

   * - Description
     - The array of grid attribute values
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

