cg_iric_read_sol_baseiterative_real
=====================================

倍精度実数の計算結果の値を取得する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_sol_baseiterative_real(fid, step, label, val, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_BaseIterative_Real(fid, step, label, &val);

形式 (Python)
---------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_BaseIterative_Real(fid, step, label)

引数
----

.. csv-table:: cg_iric_read_sol_baseiterative_real の引数
   :file: cg_iric_read_sol_baseiterative_real_args.csv
   :header-rows: 1

