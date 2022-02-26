cg_iric_getgridcoord3d
========================

三次元構造格子を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_getgridcoord3d(fid, x, y, z, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_GetGridCoord3d(fid, x, y, z);

形式 (Python)
---------------
.. code-block:: python

   x, y, z = cg_iRIC_GetGridCoord3d(fid)

引数
----

.. csv-table:: cg_iric_getgridcoord3d の引数
   :file: cg_iric_getgridcoord3d_args.csv
   :header-rows: 1

