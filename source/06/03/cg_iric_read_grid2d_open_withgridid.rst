.. _sec_iriclibfunc_cg_iric_read_grid2d_open_withgridid:

cg_iric_read_grid2d_open_withgridid
======================================

Opens the grid

The grid opened with this subroutine can be closed with :ref:`sec_iriclibfunc_cg_iric_read_grid2d_close`.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid2d_open_withgridid(fid, gid, g_handle, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid2d_Open_WithGridId(fid, gid, &g_handle);

Format (Python)
----------------
.. code-block:: python

   g_handle = cg_iRIC_Read_Grid2d_Open_WithGridId(fid, gid)

Arguments
-----------

.. csv-table:: Arguments of cg_iric_read_grid2d_open_withgridid
   :file: cg_iric_read_grid2d_open_withgridid_args.csv
   :header-rows: 1
