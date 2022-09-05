cg_iric_read_grid_triangleelements_withgridid
================================================

非構造格子の三角形頂点のIDリストを読み込む。

ids に、セルの数 x 3 のサイズの配列を渡すと、 1, 2, 3 番目, 4, 5, 6 番目, ...
にそれぞれ 1番目, 2番目の三角形を構成する頂点の ID が返される。

配列 ids を作成するために、先に cg_iric_read_cellcount で三角形の数を調べる。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid_triangleelements_withgridid(fid, gid, ids, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_TriangleElements_WithGridId(fid, gid, ids);

形式 (Python)
---------------
.. code-block:: python

   ids = cg_iRIC_Read_Grid_TriangleElements_WithGridId(fid)

引数
----

.. csv-table:: cg_iric_read_grid_triangleelements_withgridid の引数
   :file: cg_iric_read_grid_triangleelements_withgridid_args.csv
   :header-rows: 1

