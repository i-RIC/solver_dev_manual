cg_iric_read_sol_time
=======================

計算結果の時刻の値を取得する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_time(step, time, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Time(step, &time);

形式 (Python)
---------------
.. code-block:: python

   time = cg_iRIC_Read_Sol_Time(step)

引数
----

.. csv-table:: cg_iric_read_sol_time の引数
   :file: cg_iric_read_sol_time_args.csv
   :header-rows: 1

