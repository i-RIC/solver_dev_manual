cg_iric_read_bc_indices
=========================

境界条件が設定された要素 (格子点もしくはセル)

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_bc_indices(type, num, indices, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_Indices(type, num, indices);

形式 (Python)
---------------
.. code-block:: python

   indices = cg_iRIC_Read_BC_Indices(type, num)

引数
----

.. csv-table:: cg_iric_read_bc_indices の引数
   :file: cg_iric_read_bc_indices_args.csv
   :header-rows: 1


備考
----

indices に返される値は、境界条件が設定される位置によって、
:numref:`cg_iric_read_bc_indices_vals` に示すように異なります。
格子点、セルでは、値2つで一つの要素を定義しているのに対し、
辺では値4つで1つの要素を定義している点にご注意下さい。

.. _cg_iric_read_bc_indices_vals:

.. list-table::  境界条件を設定された位置と indices に返される値の関係
   :header-rows: 1

   * - 境界条件を設定された位置
     - indicesに返される値
   * - 格子点 (node)
     - | (格子点1のI), (格子点1のJ)
       | ...,
       | (格子点NのI), (格子点NのJ)
   * - セル (cell)
     - | (セル1のI), (セル1のJ)
       | ...,
       | (セルNのI), (セルNのJ)
   * - 辺 (edge)
     - | (辺1の開始格子点のI), (辺1の開始格子点のJ),
       | (辺1の終了格子点のI), (辺1の終了格子点のJ),
       | ...,
       | (辺Nの開始格子点のI), (辺Nの開始格子点のJ),
       | (辺Nの終了格子点のI), (辺Nの終了格子点のJ)
