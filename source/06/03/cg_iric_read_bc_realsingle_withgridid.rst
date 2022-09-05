cg_iric_read_bc_realsingle_withgridid
=======================================

実数(単精度)型の境界条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_bc_realsingle_withgridid(fid, gid, type, num, label, realvalue, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_RealSingle_WithGridId(fid, gid, type, num, label, &realvalue);

形式 (Python)
---------------

Python にはこの関数は存在しない

引数
----

.. csv-table:: cg_iric_read_bc_realsingle_withgridid の引数
   :file: cg_iric_read_bc_realsingle_withgridid_args.csv
   :header-rows: 1

