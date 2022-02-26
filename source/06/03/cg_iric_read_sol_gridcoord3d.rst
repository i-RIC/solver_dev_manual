cg_iric_read_sol_gridcoord3d
==============================

-  Reads the 3D structured grid (for moving grid calculation)

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_gridcoord3d(step, x, y, z, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_GridCoord3d(step, x, y, z);

Format (Python)
----------------
.. code-block:: python

   x, y, z = cg_iRIC_Read_Sol_GridCoord3d(step)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_gridcoord3d
   :file: cg_iric_read_sol_gridcoord3d_args.csv
   :header-rows: 1

