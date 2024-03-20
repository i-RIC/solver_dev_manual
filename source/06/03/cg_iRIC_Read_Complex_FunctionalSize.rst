.. _sec_ref_cg_iRIC_Read_Complex_FunctionalSize:

cg_iRIC_Read_Complex_FunctionalSize
===================================

Reads the size of a functional complex type grid attribute.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Complex_FunctionalSize(fid, groupname, num, name, size, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Complex_FunctionalSize(fid, groupname, num, name, size)

Format (Python)
-----------------

.. code-block:: python

   size = cg_iRIC_Read_Complex_FunctionalSize(fid, groupname, num, name)

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

groupname
~~~~~~~~~

.. list-table:: Description of groupname
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - groupname
   * - Input/Output
     - Input

   * - Description
     - The name of the complex condition
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
     - Group number
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

size
~~~~

.. list-table:: Description of size
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - size
   * - Input/Output
     - Output

   * - Description
     - The number of values for the functional consition
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

