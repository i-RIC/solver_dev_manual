cg_iric_write_sol_jface_real
===============================

倍精度実数のJ方向格子エッジごとに値を持つ計算結果を出力する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_sol_jface_real(label, val, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_JFace_Real(label, val);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_Write_Sol_JFace_Real(label, val)

引数
----

.. csv-table:: cg_iric_write_sol_jface_real の引数
   :file: cg_iric_write_sol_jface_real_args.csv
   :header-rows: 1
