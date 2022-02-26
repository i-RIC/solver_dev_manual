cg_iric_read_sol_gridcoord2d
==============================

-  Reads the 2D structured grid (for moving grid calculation)

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_gridcoord2d(fid, step, x, y, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_GridCoord2d(fid, step, x, y);

Format (Python)
----------------
.. code-block:: python

   x, y = cg_iRIC_Read_Sol_GridCoord2d(fid, step)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_gridcoord2d
   :file: cg_iric_read_sol_gridcoord2d_args.csv
   :header-rows: 1

