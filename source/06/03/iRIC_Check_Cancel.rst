.. _sec_ref_iRIC_Check_Cancel:

iRIC_Check_Cancel
=================

Checks whether user canceled solver execution.

Format (FORTRAN)
-----------------

.. code-block:: fortran

   call iRIC_Check_Cancel(canceled)

Format (C/C++)
-----------------

.. code-block:: c

   canceled = iRIC_Check_Cancel()

Format (Python)
-----------------

.. code-block:: python

   canceled = iRIC_Check_Cancel()

Arguments and returned value
-------------------------------

canceled
~~~~~~~~

.. list-table:: Description of canceled
   :header-rows: 1

   * - Item
     - Value
   * - Name
     - canceled
   * - Input/Output
     - Output

   * - Description
     - If canceled 1 is returned, if not, 0 is returned.
   * - Data type (FORTRAN)
     - integer
   * - Data type (C/C++)
     - int
   * - Data type (Python)
     - int

