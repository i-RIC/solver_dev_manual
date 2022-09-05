cg_iric_copy_grid_withgridid
================================

Copy grid from one CGNS file to another.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_copy_grid_withgridid(fid_from, fid_to, gid, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Copy_Grid_WithGridId(fid_from, fid_to, gid);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Copy_Grid_WithGridId(fid_from, fid_to, gid)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_copy_grid_withgridid
   :file: cg_iric_copy_grid_withgridid_args.csv
   :header-rows: 1
