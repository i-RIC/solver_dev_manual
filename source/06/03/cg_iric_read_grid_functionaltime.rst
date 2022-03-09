cg_iric_read_grid_functionaltime
==================================

次元「時刻」(Time) の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid_functionaltime(fid, label, values, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_functionalTime(fid, label, values);

形式 (Python)
---------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_functionalTime(fid, label)

引数
----

.. csv-table:: cg_iric_read_grid_functionaltime の引数
   :file: cg_iric_read_grid_functionaltime_args.csv
   :header-rows: 1

