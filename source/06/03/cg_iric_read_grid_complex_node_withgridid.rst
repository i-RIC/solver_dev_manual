cg_iric_read_grid_complex_node_withgridid
===========================================

構造格子の格子点で定義された複合型の属性を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid_complex_node_withgridid(fid, gid, label, values, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_Complex_Node_WithGridId(fid, gid, label, values);

形式 (Python)
---------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_Complex_Node_WithGridId(fid, gid, label)

引数
----

.. csv-table:: cg_iric_read_grid_complex_node_withgridid の引数
   :file: cg_iric_read_grid_complex_node_withgridid_args.csv
   :header-rows: 1

