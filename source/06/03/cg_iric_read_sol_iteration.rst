cg_iric_read_sol_iteration
============================

計算結果のループ回数の値を取得する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_iteration(step, iteration, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_Iteration(step, &iteration);

形式 (Python)
---------------
.. code-block:: python

   iteration = cg_iRIC_Read_Sol_Iteration(step)

引数
----

.. csv-table:: cg_iric_read_sol_iteration の引数
   :file: cg_iric_read_sol_iteration_args.csv
   :header-rows: 1

