cg_iric_writegridcoord3d
==========================

-  Outputs a three-dimensional structured grid.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_writegridcoord2d(fid, nx, ny, x, y, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_WriteGridCoord3d(fid, nx, ny, nz, x, y, z);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_WriteGridCoord3d(fid, nx, ny, nz, x, y, z)

Arguments
---------

.. csv-table:: Arguments of cg_iric_writegridcoord3d
   :file: cg_iric_writegridcoord3d_args.csv
   :header-rows: 1

