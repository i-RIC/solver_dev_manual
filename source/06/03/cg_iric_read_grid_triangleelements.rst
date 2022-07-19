cg_iric_read_grid_triangleelements
=====================================

Reads the list of IDs of nodes for each triangles in an unstructured grid.

You should pass an array with size (numcells * 3) for ids.
The returned values of ids will be the IDs of nodes for each triangles.
1st, 2nd, 3rd values will be the IDs of nodes of the 1st triangle,
4th, 5th, 6th values will be the IDs of nodes of the 2nd triangle, etc.

You can use :ref:`sec_iriclibfunc_cg_iric_read_grid_cellcount`
to know the number of cells, to allocate memory for ids.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid_triangleelements(fid, ids, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_TriangleElements(fid, ids);

Format (Python)
----------------
.. code-block:: python

   ids = cg_iRIC_Read_Grid_TriangleElements(fid)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_grid_triangleelements
   :file: cg_iric_read_grid_triangleelements_args.csv
   :header-rows: 1

