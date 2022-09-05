cg_iric_write_sol_particle_pos3d_withgridid
=============================================

Outputs particle positions (three-dimensions).

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_write_sol_particle_pos3d_withgridid(fid, gid, count, x, y, z, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Particle_Pos3d_WithGridId(fid, gid, count, x, y, z);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Write_Sol_Particle_Pos3d_WithGridId(fid, gid, x, y, z)

Arguments
---------

.. csv-table:: Arguments of cg_iric_write_sol_particle_pos3d_withgridid
   :file: cg_iric_write_sol_particle_pos3d_withgridid_args.csv
   :header-rows: 1

