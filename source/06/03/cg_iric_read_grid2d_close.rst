.. _sec_iriclibfunc_cg_iric_read_grid2d_close:

cg_iric_read_grid2d_close
===========================

Closes the grid opened with :ref:`sec_iriclibfunc_cg_iric_read_grid2d_open`, :ref:`sec_iriclibfunc_cg_iric_read_sol_grid2d_open`.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid2d_close(g_handle, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Close(g_handle);

Format (Python)
----------------
.. code-block:: python

   cg_iRIC_Read_Grid2d_Close(g_handle)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid2d_close
   :file: cg_iric_read_grid2d_close_args.csv
   :header-rows: 1
