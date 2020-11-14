cg_iric_read_complex_real_f
===========================

複合型格子属性の、実数(倍精度)型の条件の値を読み込む。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_complex_real_f(type, num, name, value, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Complex_Real(type, num, name, &value);

形式 (Python)
---------------
.. code-block:: python

   value = cg_iRIC_Read_Complex_Real(type, num, name)

引数
----

.. csv-table:: cg_iric_read_complex_real_f の引数
   :file: cg_iric_read_complex_real_f_args.csv
   :header-rows: 1

