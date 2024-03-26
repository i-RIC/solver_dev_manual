実数
========

定義方法
----------

.. code-block:: xml
   :caption: 実数の条件の定義例
   :name: widget_example_real_def
   :linenos:

   <Item name="g" caption="Gravity [m/s2]">
     <Definition valueType="real" default="9.8" />
   </Item>

条件の表示例
---------------

.. _widget_example_real_select:

.. figure:: images/widget_example_real.png
   :width: 320pt

   実数の条件の表示例

読み込み処理の記述方法
---------------------------

計算条件・格子生成条件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 実数の条件を読み込むための処理の記述例 (計算条件・格子生成条件) FORTRAN
   :name: widget_example_real_load_calccond_fortran
   :linenos:

   integer:: ier
   double precision:: g

   call cg_iRIC_Read_Real(fid, "g", g, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: 実数の条件を読み込むための処理の記述例 (計算条件・格子生成条件) C/C++
   :name: widget_example_real_load_calccond_c
   :linenos:

   int ier;
   double g;

   ier = cg_iRIC_Read_Real(fid, "g", &g)

Python
''''''''''

.. code-block:: python
   :caption: 実数の条件を読み込むための処理の記述例 (計算条件・格子生成条件) Python
   :name: widget_example_real_load_calccond_python
   :linenos:

   g = cg_iRIC_Read_Real(fid, "g")

境界条件
~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 実数の条件を読み込むための処理の記述例 (境界条件) FORTRAN
   :name: widget_example_real_load_bcond_fortran
   :linenos:

   integer:: ier
   double precision:: g

   call cg_iRIC_Read_BC_Real(fid, "inflow", 1, "g", g, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: 実数の条件を読み込むための処理の記述例 (境界条件) C/C++
   :name: widget_example_real_load_bcond_c
   :linenos:

   int ier;
   double g;

   ier = cg_iRIC_Read_BC_Real(fid, "inflow", 1, "g", &g)

Python
''''''''''

.. code-block:: python
   :caption: 実数の条件を読み込むための処理の記述例 (境界条件) Python
   :name: widget_example_real_load_bcond_python
   :linenos:

   g = cg_iRIC_Read_BC_Real(fid, "inflow", 1, "g")
