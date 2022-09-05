cg_iric_read_grid_integer_cell_withgridid
===========================================

Reads the integer attribute values defined at cells of a grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid_integer_cell_withgridid(fid, gid, label, values, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_Integer_Cell_WithGridId(fid, gid, label, values);

Format (Python)
----------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_Integer_Cell_WithGridId(fid, gid, label)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid_integer_cell_withgridid
   :file: cg_iric_read_grid_integer_cell_withgridid_args.csv
   :header-rows: 1

