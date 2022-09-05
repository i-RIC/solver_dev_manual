cg_iric_read_sol_grid3d_coords_withgridid
=========================================

Reads the 3D structured grid (for moving grid calculation).

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_grid3d_coords_withgridid(fid, gid, step, x, y, z, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Grid3d_Coords_WithGridId(fid, gid, step, x, y, z);

Format (Python)
----------------
.. code-block:: python

   x, y, z = cg_iRIC_Read_Sol_Grid3d_Coords_WithGridId(fid, gid, step)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_grid3d_coords_withgridid
   :file: cg_iric_read_sol_grid3d_coords_withgridid_args.csv
   :header-rows: 1

