.. _sec_iriclibfunc_cg_iric_read_grid2d_open:

cg_iric_read_grid2d_open
===========================

Opens the grid

The grid opened with this subroutine can be closed with :ref:`sec_iriclibfunc_cg_iric_read_grid2d_close`.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid2d_open(fid, g_handle, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Open(fid, &g_handle);

Format (Python)
----------------
.. code-block:: python

   g_handle = cg_iRIC_Read_Grid2d_Open(fid)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid2d_open
   :file: cg_iric_read_grid2d_open_args.csv
   :header-rows: 1
