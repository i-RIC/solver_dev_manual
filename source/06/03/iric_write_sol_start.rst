iric_write_sol_start
======================

計算結果の出力開始をGUIに通知する。

.. note::

   この関数は、現在は何もせず、呼び出しは不要。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call iric_write_sol_start(filename, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = iRIC_Write_Sol_Start(filename);

形式 (Python)
---------------

Python にはこの関数は存在しない

引数
----

.. csv-table:: iric_write_sol_start の引数
   :file: iric_write_sol_start_args.csv
   :header-rows: 1

