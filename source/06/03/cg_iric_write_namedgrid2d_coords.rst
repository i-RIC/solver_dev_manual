cg_iric_write_namedgrid2d_coords
==================================

Outputs a two-dimensional structured grid, specifying the name.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_namedgrid2d_coords(fid, name, nx, ny, x, y, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid2d_Coords(fid, name, nx, ny, x, y);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_NamedGrid2d_Coords(fid, name, nx, ny, x, y)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_write_namedgrid2d_coords
   :file: cg_iric_write_namedgrid2d_coords_args.csv
   :header-rows: 1

