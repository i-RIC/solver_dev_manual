cg_iric_read_sol_jface_integer_f
====================================

整数のJ方向格子エッジごとに値を持つ計算結果の値を取得する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_jface_integer_f(step, label, val, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_JFace_Integer(step, label, val);

形式 (Python)
---------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_JFace_Integer(step, label)

引数
----

.. csv-table:: cg_iric_read_sol_jface_integer_f の引数
   :file: cg_iric_read_sol_jface_integer_f_args.csv
   :header-rows: 1
