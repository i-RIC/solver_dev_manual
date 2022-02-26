cg_iric_open
===============

CGNS ファイルを開く。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_open(filename, mode, fid, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Open(filename, mode, fid);

形式 (Python)
---------------
.. code-block:: python

   fid = cg_iRIC_Open(filename, mode)

引数
----

.. csv-table:: cg_iRIC_Open の引数
   :file: cg_iric_open_args.csv
   :header-rows: 1

備考
----

.. csv-table:: mode の値
   :file: cg_iric_open_modes.csv
   :header-rows: 1
