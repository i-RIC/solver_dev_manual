cg_iric_read_grid_functional_real_cell
========================================

次元「時刻」を持つ、セルで定義された倍精度実数の属性を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid_functional_real_cell(fid, label, dimid, values, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_F_functional_Real_Cell(fid, label, dimid, values);

形式 (Python)
---------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_F_functional_Real_Cell(fid, label, dimid)

引数
----

.. csv-table:: cg_iric_read_grid_functional_real_cell の引数
   :file: cg_iric_read_grid_functional_real_cell_args.csv
   :header-rows: 1

