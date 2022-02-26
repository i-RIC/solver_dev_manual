cg_iric_write_grid3d_coords
============================

-  Outputs a three-dimensional structured grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_grid2d_coords(fid, nx, ny, x, y, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Grid3d_Coords(fid, nx, ny, nz, x, y, z);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Grid3d_Coords(fid, nx, ny, nz, x, y, z)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_grid3d_coords
   :file: cg_iric_write_grid3d_coords_args.csv
   :header-rows: 1

