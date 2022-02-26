cg_iric_read_grid_real_node
=============================

構造格子の格子点で定義された倍精度実数の属性を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_grid_real_node(fid, label, values, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Grid_Real_Node(fid, label, values);

形式 (Python)
---------------
.. code-block:: python

   values = cg_iRIC_Read_Grid_Real_Node(fid, label)

引数
----

.. csv-table:: cg_iric_read_grid_real_node の引数
   :file: cg_iric_read_grid_real_node_args.csv
   :header-rows: 1

