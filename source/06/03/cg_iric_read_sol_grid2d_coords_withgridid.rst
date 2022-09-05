cg_iric_read_sol_grid2d_coords_withgridid
=========================================

Reads the 2D structured grid (for moving grid calculation).

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_grid2d_coords_withgridid(fid, gid, step, x, y, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Grid2d_Coords_WithGridId(fid, gid, step, x, y);

Format (Python)
----------------
.. code-block:: python

   x, y = cg_iRIC_Read_Sol_Grid2d_Coords_WithGridId(fid, gid, step)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_grid2d_coords_withgridid
   :file: cg_iric_read_sol_grid2d_coords_withgridid_args.csv
   :header-rows: 1

