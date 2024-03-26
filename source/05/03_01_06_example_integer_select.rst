.. _calccond_int_select_example:

整数 (選択式)
==============

定義方法
----------

.. code-block:: xml
   :caption: 整数 (選択式) の条件の定義例
   :name: widget_example_integer_select_def
   :linenos:

   <Item name="flowtype" caption="Flow type">
     <Definition valueType="integer" default="0">
       <Enumeration value="0" caption="Static Flow"/>
       <Enumeration value="1" caption="Dynamic Flow"/>
     </Definition>
   </Item>

条件の表示例
---------------

.. _widget_example_integer_select:

.. figure:: images/widget_example_combobox.png
   :width: 320pt

   整数 (選択式) の条件の表示例

読み込み処理の記述方法
---------------------------

計算条件・格子生成条件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 整数 (選択式) の条件を読み込むための処理の記述例 (計算条件・格子生成条件) FORTRAN
   :name: widget_example_integer_select_load_calccond_fortran
   :linenos:

   integer:: ier, flowtype

   call cg_iRIC_Read_Integer(fid, "flowtype", flowtype, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: 整数 (選択式) の条件を読み込むための処理の記述例 (計算条件・格子生成条件) C/C++
   :name: widget_example_integer_select_load_calccond_c
   :linenos:

   int ier, flowtype;

   ier = cg_iRIC_Read_Integer(fid, "flowtype", &flowtype)

Python
''''''''''

.. code-block:: python
   :caption: 整数 (選択式) の条件を読み込むための処理の記述例 (計算条件・格子生成条件) Python
   :name: widget_example_integer_select_load_calccond_python
   :linenos:

   flowtype = cg_iRIC_Read_Integer(fid, "flowtype")

境界条件
~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 整数 (選択式) の条件を読み込むための処理の記述例 (境界条件) FORTRAN
   :name: widget_example_integer_select_load_bcond_fortran
   :linenos:

   integer:: ier, flowtype

   call cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "flowtype", flowtype, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: 整数 (選択式) の条件を読み込むための処理の記述例 (境界条件) C/C++
   :name: widget_example_integer_select_load_bcond_c
   :linenos:

   int ier, flowtype;

   ier = cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "flowtype", &flowtype)

Python
''''''''''

.. code-block:: python
   :caption: 整数 (選択式) の条件を読み込むための処理の記述例 (境界条件) Python
   :name: widget_example_integer_select_load_bcond_python
   :linenos:

   flowtype = cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "flowtype")
