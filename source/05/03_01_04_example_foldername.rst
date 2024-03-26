フォルダ名
===============

定義方法
----------

.. code-block:: xml
   :caption: フォルダ名の条件の定義例
   :name: widget_example_foldername_def
   :linenos:

   <Item name="flowdatafolder" caption="Flow data folder">
     <Definition valueType="foldername" />
   </Item>

条件の表示例
---------------

.. _widget_example_folder:

.. figure:: images/widget_example_folder.png
   :width: 500pt

   フォルダ名の条件の表示例

読み込み処理の記述方法
---------------------------

計算条件・格子生成条件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: フォルダ名の条件を読み込むための処理の記述例 (計算条件・格子生成条件) FORTRAN
   :name: widget_example_foldername_load_calccond_fortran
   :linenos:

   integer:: ier
   character(200):: flowdatafolder

   call cg_iRIC_Read_String(fid, "flowdatafolder", flowdatafolder, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: フォルダ名の条件を読み込むための処理の記述例 (計算条件・格子生成条件) C/C++
   :name: widget_example_foldername_load_calccond_c
   :linenos:

   int ier
   char flowdatafolder[200];

   ier = cg_iRIC_Read_String(fid, "flowdatafolder", flowdatafolder)

Python
''''''''''

.. code-block:: python
   :caption: フォルダ名の条件を読み込むための処理の記述例 (計算条件・格子生成条件) Python
   :name: widget_example_foldername_load_calccond_python
   :linenos:

   flowdatafolder = cg_iRIC_Read_String(fid, "flowdatafolder")

境界条件
~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: フォルダ名の条件を読み込むための処理の記述例 (境界条件) FORTRAN
   :name: widget_example_foldername_load_bcond_fortran
   :linenos:

   integer:: ier
   character(200):: flowdatafolder

   call cg_iRIC_Read_BC_String(fid, "inflow", 1, "flowdatafolder", flowdatafolder, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: フォルダ名の条件を読み込むための処理の記述例 (境界条件) C/C++
   :name: widget_example_foldername_load_bcond_c
   :linenos:

   int ier
   char flowdatafolder[200];

   ier = cg_iRIC_Read_BC_String(fid, "inflow", 1, "flowdatafolder", flowdatafolder)

Python
''''''''''

.. code-block:: python
   :caption: フォルダ名の条件を読み込むための処理の記述例 (境界条件) Python
   :name: widget_example_foldername_load_bcond_python
   :linenos:

   flowdatafolder = cg_iRIC_Read_BC_String(fid, "inflow", 1, "flowdatafolder")
