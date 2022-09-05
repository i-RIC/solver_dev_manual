cg_iric_write_sol_particle_pos3d_withgridid
=============================================

粒子の位置を出力する。 (3次元)

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_sol_particle_pos3d_withgridid(fid, gid, count, x, y, z, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Particle_Pos3d_WithGridId(fid, gid, count, x, y, z);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_Write_Sol_Particle_Pos3d_WithGridId(fid, gid, x, y, z)

引数
----

.. csv-table:: cg_iric_write_sol_particle_pos3d_withgridid の引数
   :file: cg_iric_write_sol_particle_pos3d_withgridid_args.csv
   :header-rows: 1

