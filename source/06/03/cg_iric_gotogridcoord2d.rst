cg_iric_gotogridcoord2d
=========================

二次元構造格子を読み込む準備を行う。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_gotogridcoord2d(fid, nx, ny, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_GotoGridCoord2d(fid, nx, ny);

形式 (Python)
---------------
.. code-block:: python

   nx, ny = cg_iRIC_GotoGridCoord2d(fid)

引数
----

.. csv-table:: cg_iric_gotogridcoord2d の引数
   :file: cg_iric_gotogridcoord2d_args.csv
   :header-rows: 1

