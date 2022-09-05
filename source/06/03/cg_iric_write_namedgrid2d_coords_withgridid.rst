cg_iric_write_namedgrid2d_coords_withgridid
=============================================

Outputs a two-dimensional structured grid, specifying the name.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_namedgrid2d_coords_withgridid(fid, name, nx, ny, x, y, gid, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid2d_Coords_WithGridId(fid, name, nx, ny, x, y, gid);

Format (Python)
----------------
.. code-block:: python

   gid = cg_iRIC_Write_NamedGrid2d_Coords_WithGridId(fid, name, nx, ny, x, y)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_write_namedgrid2d_coords_withgridid
   :file: cg_iric_write_namedgrid2d_coords_withgridid_args.csv
   :header-rows: 1

