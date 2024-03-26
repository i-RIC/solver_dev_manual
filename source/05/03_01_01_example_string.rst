文字列
===========

定義方法
----------

.. code-block:: xml
   :caption: 文字列の条件の定義例
   :name: widget_example_string_def
   :linenos:

   <Item name="sampleitem" caption="Sample Item">
     <Definition valueType="string" />
   </Item>

条件の表示例
---------------

.. _widget_example_string:

.. figure:: images/widget_example_string.png
   :width: 320pt

   文字列の条件の表示例

読み込み処理の記述方法
---------------------------

計算条件・格子生成条件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 文字列の条件を読み込むための処理の記述例 (計算条件・格子生成条件) FORTRAN
   :name: widget_example_string_load_calccond_fortran
   :linenos:

   integer:: ier
   character(200):: sampleitem

   call cg_iRIC_Read_String(fid, "sampleitem", sampleitem, ier)


C/C++
'''''''

.. code-block:: c
   :caption: 文字列の条件を読み込むための処理の記述例 (計算条件・格子生成条件) C/C++
   :name: widget_example_string_load_calccond_c
   :linenos:

   int ier;
   char sampleitem[200];

   ier = cg_iRIC_Read_String(fid, "sampleitem", sampleitem)

Python
'''''''

.. code-block:: python
   :caption: 文字列の条件を読み込むための処理の記述例 (計算条件・格子生成条件) Python
   :name: widget_example_string_load_calccond_python
   :linenos:

   sampleitem = cg_iRIC_Read_String(fid, "sampleitem")

境界条件
~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 文字列の条件を読み込むための処理の記述例 (境界条件) FORTRAN
   :name: widget_example_string_load_bcond_fortran
   :linenos:

   integer:: ier
   character(200):: sampleitem

   call cg_iRIC_Read_BC_String(fid, "inflow", 1, "sampleitem", sampleitem, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: 文字列の条件を読み込むための処理の記述例 (境界条件) C/C++
   :name: widget_example_string_load_bcond_c
   :linenos:

   int ier;
   char sampleitem[200];

   ier = cg_iRIC_Read_BC_String(fid, "inflow", 1, "sampleitem", sampleitem)

Python
''''''''''

.. code-block:: python
   :caption: 文字列の条件を読み込むための処理の記述例 (境界条件) Python
   :name: widget_example_string_load_bcond_python
   :linenos:

   sampleitem = cg_iRIC_Read_BC_String(fid, "inflow", 1, "sampleitem")
