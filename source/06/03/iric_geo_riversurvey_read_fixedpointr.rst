iric_geo_riversurvey_read_fixedpointr
=======================================

横断線の右岸延長線のデータを返す。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call iric_geo_riversurvey_read_fixedpointr(rid, pointid, set, directionx, directiony, index, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = iRIC_Geo_RiverSurvey_Read_FixedPointR(rid, pointid, &set, &directionx, &directiony, &index);

形式 (Python)
---------------

Python にはこの関数は存在しない

引数
----

.. csv-table:: iric_geo_riversurvey_read_fixedpointr の引数
   :file: iric_geo_riversurvey_read_fixedpointr_args.csv
   :header-rows: 1

