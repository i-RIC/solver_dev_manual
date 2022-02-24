iric_check_lock
=================

CGNSファイルがGUIによってロックされているか確認する。

.. note::

   この関数は、現在は何もせず、呼び出しは不要。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call iric_check_lock(filename, locked)

形式 (C/C++)
---------------
.. code-block:: c

   iRIC_Check_Lock(filename, locked);

形式 (Python)
---------------

Python にはこの関数は存在しない

引数
----

.. csv-table:: iric_check_lock の引数
   :file: iric_check_lock_args.csv
   :header-rows: 1

