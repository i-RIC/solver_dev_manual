cg_iric_gotogridcoord3d
=========================

三次元構造格子を読み込む準備を行う。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_gotogridcoord3d(fid, nx, ny, nz, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_GotoGridCoord3d(fid, nx, ny, nz);

形式 (Python)
---------------
.. code-block:: python

   nx, ny, nz = cg_iRIC_GotoGridCoord3d(fid)

引数
----

.. csv-table:: cg_iric_gotogridcoord3d の引数
   :file: cg_iric_gotogridcoord3d_args.csv
   :header-rows: 1

