整数
=====

定義方法
----------

.. code-block:: xml
   :caption: 整数の条件の定義例
   :name: widget_example_integer_def
   :linenos:

   <Item name="numsteps" caption="The Number of steps to calculate">
     <Definition valueType="integer" default="20" min="1" max="200" />
   </Item>

条件の表示例
---------------

.. _widget_example_integer:

.. figure:: images/widget_example_integer.png
   :width: 340pt

   整数の条件の表示例

読み込み処理の記述方法
---------------------------

計算条件・格子生成条件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 整数の条件を読み込むための処理の記述例 (計算条件・格子生成条件) FORTRAN
   :name: widget_example_integer_load_calccond_fortran
   :linenos:

   integer:: ier, numsteps

   call cg_iRIC_Read_Integer(fid, "numsteps", numsteps, ier)


C/C++
''''''''''

.. code-block:: c
   :caption: 整数の条件を読み込むための処理の記述例 (計算条件・格子生成条件) C/C++
   :name: widget_example_integer_load_calccond_c
   :linenos:

   int ier, numsteps;

   ier = cg_iRIC_Read_Integer(fid, "numsteps", &numsteps)

Python
''''''''''

.. code-block:: python
   :caption: 整数の条件を読み込むための処理の記述例 (計算条件・格子生成条件) Python
   :name: widget_example_integer_load_calccond_python
   :linenos:

   numsteps = cg_iRIC_Read_Integer(fid, "numsteps")

境界条件
~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: 整数の条件を読み込むための処理の記述例 (境界条件) FORTRAN
   :name: widget_example_integer_load_bcond_fortran
   :linenos:

   integer:: ier, numsteps

   call cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "numsteps", numsteps, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: 整数の条件を読み込むための処理の記述例 (境界条件) C/C++
   :name: widget_example_integer_load_bcond_c
   :linenos:

   int ier, numstep;

   ier = cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "numsteps", &numsteps)

Python
''''''''''

.. code-block:: python
   :caption: 整数の条件を読み込むための処理の記述例 (境界条件) Python
   :name: widget_example_integer_load_bcond_python
   :linenos:

   numsteps = cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "numsteps")
