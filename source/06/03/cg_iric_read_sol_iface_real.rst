cg_iric_read_sol_iface_real
===============================

倍精度実数のI方向格子エッジごとに値を持つ計算結果の値を取得する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_iface_real(step, label, val, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_IFace_Real(step, label, val);

形式 (Python)
---------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_IFace_Real(step, label)

引数
----

.. csv-table:: cg_iric_read_sol_iface_real の引数
   :file: cg_iric_read_sol_iface_real_args.csv
   :header-rows: 1
