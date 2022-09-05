cg_iric_read_grid_functionaltime_withgridid
=============================================

次元「時刻」(Time) の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid_functionaltime_withgridid(fid, gid, label, values, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_functionalTime_WithGridId(fid, gid, label, values);

形式 (Python)
---------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_functionalTime_WithGridId(fid, gid, label)

引数
----

.. csv-table:: cg_iric_read_grid_functionaltime_withgridid の引数
   :file: cg_iric_read_grid_functionaltime_withgridid_args.csv
   :header-rows: 1

