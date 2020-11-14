cg_iric_read_geo_filename_f
===========================

CGNSファイルから地形データのファイル名と種類を読み込みます。

形式 (FORTRAN)
---------------
.. code-block:: fortran

   call cg_iric_read_geo_filename_f(name, geoid, geofilename, geotype, ier)

形式 (C/C++)
---------------
.. code-block:: c

   ier = cg_iRIC_Read_Geo_Filename(name, geoid, geofilename, &geotype);

形式 (Python)
---------------

Python にはこの関数は存在しない

引数
----

.. csv-table:: cg_iric_read_geo_filename_f の引数
   :file: cg_iric_read_geo_filename_f_args.csv
   :header-rows: 1

備考
----

なお、geotype で読み込まれる地形データの種類は、
iriclib_f.hで定義された、 :numref:`cg_iric_read_geo_filename_f_geotypes`
に示す値のいずれかです。

.. _cg_iric_read_geo_filename_f_geotypes:

.. csv-table:: geotype で返される、地形データ種類を表す定数
   :file: cg_iric_read_geo_filename_f_geotypes.csv
   :header-rows: 1

