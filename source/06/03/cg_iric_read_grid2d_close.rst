.. _sec_iriclibfunc_cg_iric_read_grid2d_close:

cg_iric_read_grid2d_close
===========================

:ref:`sec_iriclibfunc_cg_iric_read_grid2d_open`, :ref:`sec_iriclibfunc_cg_iric_read_sol_grid2d_open`
で開いた格子を閉じる。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid2d_close(g_handle, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Close(g_handle);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_Read_Grid2d_Close(g_handle)

引数
----

.. csv-table:: cg_iric_read_grid2d_close の引数
   :file: cg_iric_read_grid2d_close_args.csv
   :header-rows: 1
