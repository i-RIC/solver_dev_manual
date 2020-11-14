cg_iric_read_sol_time_f
=======================

計算結果の時刻の値を取得する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_time_f(step, time, ier)

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

.. csv-table:: cg_iric_read_sol_time_f の引数
   :file: cg_iric_read_sol_time_f_args.csv
   :header-rows: 1

