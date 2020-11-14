cg_open_f
=========

CGNS ファイルを開く。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_open_f(filename, mode, fid, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_open(filename, mode, fid);

形式 (Python)
---------------
.. code-block:: python

   fid = cg_open(filename, mode)

引数
----

.. csv-table:: cg_open_f の引数
   :file: cg_open_f_args.csv
   :header-rows: 1

備考
----

.. csv-table:: mode の値
   :file: cg_open_f_modes.csv
   :header-rows: 1
