.. _sec_ref_cg_iRIC_Write_Sol_JFace_Integer:

cg_iRIC_Write_Sol_JFace_Integer
===============================

Writes the integer calculation result defined at grid J-direction cell boudary faces (edges).

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Write_Sol_JFace_Integer(fid, name, v_arr, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Write_Sol_JFace_Integer(fid, name, v_arr)

Format (Python)
-----------------

.. code-block:: python

   v_arr = cg_iRIC_Write_Sol_JFace_Integer(fid, name)

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
     - The name of the calculation result
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
     - The array of calculation result values
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

