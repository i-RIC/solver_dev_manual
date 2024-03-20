.. _sec_ref_cg_iRIC_Read_Sol_Iteration:

cg_iRIC_Read_Sol_Iteration
==========================

Reads the loop iteration value.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Read_Sol_Iteration(fid, step, iteration, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Read_Sol_Iteration(fid, step, iteration)

Format (Python)
-----------------

.. code-block:: python

   iteration = cg_iRIC_Read_Sol_Iteration(fid, step)

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

step
~~~~

.. list-table:: Description of step
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - step
   * - Input/Output
     - Input

   * - Description
     - The result step number
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

iteration
~~~~~~~~~

.. list-table:: Description of iteration
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - iteration
   * - Input/Output
     - Output

   * - Description
     - Iteration count
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

