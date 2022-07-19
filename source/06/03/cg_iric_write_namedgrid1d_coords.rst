cg_iric_write_namedgrid1d_coords
=====================================

Outputs a one-dimensional structured grid, specifying the name.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_namedgrid1d_coords(fid, name, nx, x, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_NamedGrid1d_Coords(fid, name, nx, x);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_NamedGrid1d_Coords(fid, name, nx, x)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_write_namedgrid1d_coords
   :file: cg_iric_write_namedgrid1d_coords_args.csv
   :header-rows: 1
