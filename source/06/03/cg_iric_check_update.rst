cg_iric_check_update
========================

ユーザーが再読み込みの要求をしたか確認し、要求していた場合は計算結果を出力する。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_check_update(fid, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Check_Update(fid);

形式 (Python)
---------------

.. code-block:: python

   cg_iRIC_Check_Update(fid)

引数
----

.. csv-table:: cg_iric_check_update の引数
   :file: cg_iric_check_update_args.csv
   :header-rows: 1

