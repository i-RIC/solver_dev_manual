.. _sec_ref_iRIC_InitOption:

iRIC_InitOption
===============

Set up the options for the solver.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_InitOption(option, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = iRIC_InitOption(option)

Format (Python)
-----------------

.. code-block:: python

   iRIC_InitOption(option)

Arguments and returned value
-------------------------------

option
~~~~~~

.. list-table:: Description of option
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - option
   * - Input/Output
     - Input

   * - Description
     - The value that corresponds to an option
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
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

