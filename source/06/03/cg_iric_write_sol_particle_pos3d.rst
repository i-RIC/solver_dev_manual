cg_iric_write_sol_particle_pos3d
==================================

粒子の位置を出力する。 (3次元)

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_sol_particle_pos3d(fid, count, x, y, z, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_Particle_Pos3d(fid, count, x, y, z);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_Write_Sol_Particle_Pos3d(fid, x, y, z)

引数
----

.. csv-table:: cg_iric_write_sol_particle_pos3d の引数
   :file: cg_iric_write_sol_particle_pos3d_args.csv
   :header-rows: 1

