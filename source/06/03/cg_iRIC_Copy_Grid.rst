.. _sec_ref_cg_iRIC_Copy_Grid:

cg_iRIC_Copy_Grid
=================

Copy grid between two CGNS files.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call cg_iRIC_Copy_Grid(fid_from, fid_to, ier)

Format (C/C++)
-----------------

.. code-block:: c

   ier = cg_iRIC_Copy_Grid(fid_from, fid_to)

Format (Python)
-----------------

.. code-block:: python

   cg_iRIC_Copy_Grid(fid_from, fid_to)

Arguments and returned value
-------------------------------

fid_from
~~~~~~~~

.. list-table:: Description of fid_from
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - fid_from
   * - Input/Output
     - Input

   * - Description
     - File ID of copy source
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

fid_to
~~~~~~

.. list-table:: Description of fid_to
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - fid_to
   * - Input/Output
     - Input

   * - Description
     - File ID of copy target
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

