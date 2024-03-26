ファイル名 (読み込み用)
=========================

定義方法
----------

.. code-block:: xml
   :caption: ファイル名 (読み込み用) の条件の定義例
   :name: widget_example_filename_load_def
   :linenos:

   <Item name="flowdatafile" caption="Flow data file">
     <Definition valueType="filename" default="flow.dat" />
   </Item>

条件の表示例
---------------

.. _widget_example_filename_load:

.. figure:: images/widget_example_filename_load.png
   :width: 500pt

   ファイル名 (読み込み用) の条件の表示例

読み込み処理の記述方法
---------------------------

計算条件・格子生成条件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: ファイル名 (読み込み用)の条件を読み込むための処理の記述例 (計算条件・格子生成条件) FORTRAN
   :name: widget_example_filename_read_load_calccond_fortran
   :linenos:

   integer:: ier
   character(200):: flowdatafile

   call cg_iRIC_Read_String(fid, "flowdatafile", flowdatafile, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: ファイル名 (読み込み用)の条件を読み込むための処理の記述例 (計算条件・格子生成条件) C/C++
   :name: widget_example_filename_read_load_calccond_c
   :linenos:

   int ier;
   char flowdatafile[200];

   ier = cg_iRIC_Read_String(fid, "flowdatafile", flowdatafile)

Python
''''''''''

.. code-block:: python
   :caption: ファイル名 (読み込み用)の条件を読み込むための処理の記述例 (計算条件・格子生成条件) Python
   :name: widget_example_filename_read_load_calccond_python
   :linenos:

   flowdatafile = cg_iRIC_Read_String(fid, "flowdatafile")

境界条件
~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: ファイル名 (読み込み用) の条件を読み込むための処理の記述例 (境界条件) FORTRAN
   :name: widget_example_filename_read_load_bcond_fortran
   :linenos:

   integer:: ier
   character(200):: flowdatafile

   call cg_iRIC_Read_BC_String(fid, "inflow", 1, "flowdatafile", flowdatafile, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: ファイル名 (読み込み用) の条件を読み込むための処理の記述例 (境界条件) C/C++
   :name: widget_example_filename_read_load_bcond_c
   :linenos:

   int ier;
   char flowdatafile[200];

   ier = cg_iRIC_Read_BC_String(fid, "inflow", 1, "flowdatafile", flowdatafile)

Python
''''''''''

.. code-block:: python
   :caption: ファイル名 (読み込み用) の条件を読み込むための処理の記述例 (境界条件) Python
   :name: widget_example_filename_read_load_bcond_python
   :linenos:

   flowdatafile = cg_iRIC_Read_BC_String(fid, "inflow", 1, "flowdatafile")
