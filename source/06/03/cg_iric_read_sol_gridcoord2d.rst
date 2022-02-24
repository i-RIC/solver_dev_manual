cg_iric_read_sol_gridcoord2d
==============================

計算結果の2次元構造格子を取得する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_gridcoord2d(step, x, y, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_GridCoord2d(step, x, y);

形式 (Python)
---------------
.. code-block:: python

   x, y = cg_iRIC_Read_Sol_GridCoord2d(step)

引数
----

.. csv-table:: cg_iric_read_sol_gridcoord2d の引数
   :file: cg_iric_read_sol_gridcoord2d_args.csv
   :header-rows: 1

