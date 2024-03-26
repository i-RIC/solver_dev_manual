関数型 (複数の値)
===================

定義方法
----------

.. code-block:: xml
   :caption: 関数型 (複数の値) の条件の定義例
   :name: widget_example_func_multi_def
   :linenos:

   <Item name="discharge_and_elev" caption="Discharge and Water Elevation time series">
     <Definition valueType="functional" >
       <Parameter name="time" valueType="real" caption="Time" />
       <Value name="discharge" valueType="real" caption="Discharge" />
       <Value name="elevation" valueType="real" caption="Water Elevation" />
     </Definition>
   </Item>


条件の表示例
---------------

.. _widget_example_func_multi:

.. figure:: images/widget_example_func_multi.png
   :width: 450pt

   関数型 (複数の値) の条件の表示例

読み込み処理の記述方法
---------------------------

計算条件・格子生成条件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 関数型 (複数の値) の条件を読み込むための処理の記述例 (計算条件・格子生成条件) FORTRAN
   :name: widget_example_func_multi_load_calccond_fortran
   :linenos:

   integer:: ier, discharge_size
   double precision, dimension(:), allocatable:: time_value
   double precision, dimension(:), allocatable:: discharge_value, elevation_value

   ! サイズを調べる
   call cg_iRIC_Read_FunctionalSize(fid, "discharge", discharge_size, ier)
   ! メモリを確保
   allocate(time_value(discharge_size))
   allocate(discharge_value(discharge_size), elevation_value(discharge_size))
   ! 確保したメモリに値を読み込む
   call cg_iRIC_Read_FunctionalWithName(fid, "discharge", "time", time_value, ier)
   call cg_iRIC_Read_FunctionalWithName(fid, "discharge", "discharge", discharge_value, ier)
   call cg_iRIC_Read_FunctionalWithName(fid, "discharge", "elevation", elevation_value, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: 関数型 (複数の値) の条件を読み込むための処理の記述例 (計算条件・格子生成条件) C++
   :name: widget_example_func_multi_load_calccond_c
   :linenos:

   int ier, discharge_size;
   std::vector<double> time_value, discharge_value, elevation_value;

   // サイズを調べる
   ier = cg_iRIC_Read_FunctionalSize(fid, "discharge", &discharge_size);
   // メモリを確保
   time_value.assign(discharge_size, 0);
   discharge_value.assign(discharge_size, 0);
   elevation_value.assign(discharge_size, 0);
   // 確保したメモリに値を読み込む
   ier = cg_iRIC_Read_FunctionalWithName(fid, "discharge", "time", time_value);
   ier = cg_iRIC_Read_FunctionalWithName(fid, "discharge", "discharge", discharge_value);
   ier = cg_iRIC_Read_FunctionalWithName(fid, "discharge", "elevation", elevation_value);

Python
''''''''''

.. code-block:: python
   :caption: 関数型 (複数の値) の条件を読み込むための処理の記述例 (計算条件・格子生成条件) Python
   :name: widget_example_func_multi_load_calccond_python
   :linenos:

   time_value = cg_iRIC_Read_FunctionalWithName(fid, "discharge", "time")
   discharge_value = cg_iRIC_Read_FunctionalWithName(fid, "discharge", "discharge")
   elevation_value = cg_iRIC_Read_FunctionalWithName(fid, "discharge", "elevation")

境界条件
~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 関数型 (複数の値) の条件を読み込むための処理の記述例 (境界条件) FORTRAN
   :name: widget_example_func_multi_load_bcond_fortran
   :linenos:

   integer:: ier, discharge_size
   double precision, dimension(:), allocatable:: time_value
   double precision, dimension(:), allocatable:: discharge_value, elevation_value

   ! サイズを調べる
   call cg_iRIC_Read_BC_FunctionalSize(fid, "discharge", discharge_size, ier)
   ! メモリを確保
   allocate(time_value(discharge_size))
   allocate(discharge_value(discharge_size), elevation_value(discharge_size))
   ! 確保したメモリに値を読み込む
   call cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "time", time_value, ier)
   call cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "discharge", discharge_value, ier)
   call cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "elevation", elevation_value, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: 関数型 (複数の値) の条件を読み込むための処理の記述例 (境界条件) C/C++
   :name: widget_example_func_multi_load_bcond_c
   :linenos:

   int ier, discharge_size;
   std::vector<double> time_value, discharge_value, elevation_value;

   // サイズを調べる
   ier = cg_iRIC_Read_BC_FunctionalSize(fid, "discharge", &discharge_size)
   // メモリを確保
   time_value.assign(discharge_size, 0);
   discharge_value.assign(discharge_size, 0);
   elevation_value.assign(discharge_size, 0);
   // 確保したメモリに値を読み込む
   ier = cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "time", time_value.data());
   ier = cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "discharge", discharge_value.data());
   ier = cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "elevation", elevation_value.data());

Python
''''''''''

.. code-block:: python
   :caption: 関数型 (複数の値) の条件を読み込むための処理の記述例 (境界条件) Python
   :name: widget_example_func_multi_load_bcond_python
   :linenos:

   time_value = cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "time")
   discharge_value = cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "discharge")
   elevation_value = cg_iRIC_Read_BC_FunctionalWithName(fid, "discharge", "elevation")
