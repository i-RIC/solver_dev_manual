cg_iric_read_grid_functionaltime_withgridid
=============================================

Reads the values of dimension \"Time\" for f_functional grid attribute.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_grid_functionaltime_withgridid(fid, gid, label, values, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_functionalTime_WithGridId(fid, gid, label, values);

Format (Python)
----------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_functionalTime_WithGridId(fid, gid, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_grid_functionaltime_withgridid
   :file: cg_iric_read_grid_functionaltime_withgridid_args.csv
   :header-rows: 1

