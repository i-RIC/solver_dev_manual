iric_initoption
===================

ソルバーのオプションを指定する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call iric_initoption(optionval, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = iRIC_InitOption(optionval);

形式 (Python)
---------------
.. code-block:: python

   iRIC_InitOption(optionval)

引数
----

.. csv-table:: iric_initoption の引数
   :file: iric_initoption_args.csv
   :header-rows: 1


備考
----

.. csv-table:: optionval の値
   :file: iric_initoption_optionvals.csv
   :header-rows: 1

