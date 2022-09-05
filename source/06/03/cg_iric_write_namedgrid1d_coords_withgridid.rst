cg_iric_write_namedgrid1d_coords_withgridid
================================================

Outputs a one-dimensional structured grid, specifying the name.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_namedgrid1d_coords_withgridid(fid, name, nx, x, gid, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid1d_Coords_WithGridId(fid, name, nx, x);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_NamedGrid1d_Coords_WithGridId(fid, name, nx, x)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_write_namedgrid1d_coords_withgridid
   :file: cg_iric_write_namedgrid1d_coords_withgridid_args.csv
   :header-rows: 1
