cg_iric_read_grid_functional_integer_cell_withgridid
======================================================

次元「時刻」を持つ、セルで定義された整数の属性を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid_functional_integer_cell_withgridid(fid, gid, label, dimid, values, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_functional_Integer_Cell_WithGridId(fid, gid, label, dimid, values);

形式 (Python)
---------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_functional_Integer_Cell_WithGridId(fid, gid, label, dimid)

引数
----

.. csv-table:: cg_iric_read_grid_functional_integer_cell_withgridid の引数
   :file: cg_iric_read_grid_functional_integer_cell_withgridid_args.csv
   :header-rows: 1

