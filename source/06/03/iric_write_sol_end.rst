iric_write_sol_end
====================

計算結果の出力終了をGUIに通知する。

.. note::

   この関数は、現在は何もせず、呼び出しは不要。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call iric_write_sol_end(filename, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = iRIC_Write_Sol_End(filename);

形式 (Python)
---------------

Python にはこの関数は存在しない

引数
----

.. csv-table:: iric_write_sol_end の引数
   :file: iric_write_sol_end_args.csv
   :header-rows: 1

