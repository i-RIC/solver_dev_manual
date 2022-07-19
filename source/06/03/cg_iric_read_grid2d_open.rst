.. _sec_iriclibfunc_cg_iric_read_grid2d_open:

cg_iric_read_grid2d_open
===========================

格子を開く。

この関数で開いた格子は、 :ref:`sec_iriclibfunc_cg_iric_read_grid2d_close` を使用して閉じる。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid2d_open(fid, g_handle, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Open(fid, &g_handle);

形式 (Python)
---------------
.. code-block:: python

   g_handle = cg_iRIC_Read_Grid2d_Open(fid)

引数
----

.. csv-table:: cg_iric_read_grid2d_open の引数
   :file: cg_iric_read_grid2d_open_args.csv
   :header-rows: 1
