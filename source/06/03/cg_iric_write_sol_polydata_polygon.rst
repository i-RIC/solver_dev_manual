cg_iric_write_sol_polydata_polygon
==========================================

計算結果としてポリゴンの形状を出力する

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_write_sol_polydata_polygon(fid, numpoints, x, y, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Write_Sol_PolyData_Polygon(fid, numpoints, x, y);

形式 (Python)
---------------
.. code-block:: python

   cg_iRIC_Write_Sol_PolyData_Polygon(fid, x, y)

引数
----

.. csv-table:: cg_iric_write_sol_polydata_polygon の引数
  :file: cg_iric_write_sol_polydata_polygon_args.csv
  :header-rows: 1
