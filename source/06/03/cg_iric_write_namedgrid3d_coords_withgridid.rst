cg_iric_write_namedgrid3d_coords_withgridid
==============================================

Outputs a three-dimensional structured grid, specifying the name.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_namedgrid3d_coords_withgridid(fid, name, nx, ny, nz, x, y, z, gid, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid3d_Coords_WithGridId(fid, name, nx, ny, nz, x, y, z);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_NamedGrid3d_Coords_WithGridId(fid, name, nx, ny, nz, x, y, z)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_write_namedgrid3d_coords_withgridid
   :file: cg_iric_write_namedgrid3d_coords_withgridid_args.csv
   :header-rows: 1

