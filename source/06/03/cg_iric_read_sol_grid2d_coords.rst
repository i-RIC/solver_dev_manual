cg_iric_read_sol_grid2d_coords
==============================

Reads the 2D structured grid (for moving grid calculation).

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_grid2d_coords(fid, step, x, y, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Grid2d_Coords(fid, step, x, y);

Format (Python)
----------------
.. code-block:: python

   x, y = cg_iRIC_Read_Sol_Grid2d_Coords(fid, step)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_grid2d_coords
   :file: cg_iric_read_sol_grid2d_coords_args.csv
   :header-rows: 1

