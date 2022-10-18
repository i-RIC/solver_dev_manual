CGNSファイル名 など
---------------------

CGNSファイル名と、CGNSファイル内の計算結果は組み合わせて使用します。

CGNSファイル名の入力欄は、 valueType に cgns_filename を指定することで作成できます。

CGNSファイル内の計算結果は、 valueType に result_gridNodeReal などを指定し、 cgnsFile に CGNSファイル名の入力欄に指定した name を指定することで作成できます。

.. code-block:: xml
   :caption: CGNSファイル名とCGNSファイル内の計算結果の条件の定義例
   :name: widget_example_cgns_def
   :linenos:

   <Item name="input_file" caption="CGNS file for input">
     <Definition valueType="cgns_filename" />
   </Item>
   <Item name="result_to_read" caption="Calculation result to read">
     <Definition valueType="result_gridNodeReal" cgnsFile="input_file" />
   </Item>

.. _widget_example_cgns:

.. figure:: images/widget_example_cgns.png
   :width: 350pt

   CGNSファイル名とCGNSファイル内の計算結果の条件の表示例

.. code-block:: fortran
   :caption: CGNSファイル名と計算結果の条件を読み込むための処理の記述例 (計算条件・格子生成条件)
   :name: widget_example_cgns_load_calccond
   :linenos:

   integer:: ier
   character(200):: cgnsName, resultName

   call cg_iric_read_string(fid, "input_file", cgnsName, ier)
   call cg_iric_read_string(fid, "result_to_read", resultName, ier)

.. code-block:: fortran
   :caption: CGNSファイル名と計算結果の条件を読み込むための処理の記述例 (境界条件)
   :name: widget_example_cgns_load_bcond
   :linenos:

   integer:: ier
   character(200):: cgnsName, resultName

   call cg_iric_read_bc_string(fid, "inflow", 1, "input_file", cgnsName, ier)
   call cg_iric_read_bc_string(fid, "inflow", 1, "result_to_read", resultName, ier)
