CGNSファイル名 など
---------------------

概要
~~~~~~

CGNSファイル名と、CGNSファイル内の計算結果は組み合わせて使用します。

CGNSファイル名の入力欄は、 valueType に cgns_filename を指定することで作成できます。

CGNSファイル内の計算結果は、 valueType に result_gridNodeReal などを指定し、 cgnsFile に CGNSファイル名の入力欄に指定した name を指定することで作成できます。

CGNS ファイルの入力欄と、その CGNSファイル内で、格子点で出力された実数値の計算結果を選択するコンボボックスを
表示するための定義例を :numref:`widget_example_cgns_def` に、定義に基づいて画面に表示される入力欄を
:numref:`widget_example_cgns` に示します。

この入力欄によるユーザの入力内容を読み取るための FORTRAN のプログラムの記述例を
:numref:`widget_example_cgns_load_calccond` と :numref:`widget_example_cgns_load_bcond`
に示します。

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

計算結果の種類ごとの valueType の値の一覧
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

計算結果の種類ごとの valueType の値の一覧を :numref:`cgns_resulttype_table` に示します。

.. list-table:: 計算結果の種類ごとの valueType 一覧
   :name: cgns_resulttype_table
   :header-rows: 1
   
   * - 定義位置
     - 値の型
     - valueType

   * - グローバル
     - 実数
     - result_baseIterativeReal

   * - グローバル
     - 整数
     - result_baseIterativeInteger

   * - 格子点
     - 実数
     - result_gridNodeReal

   * - 格子点
     - 整数
     - result_gridNodeInteger

   * - セル
     - 実数
     - result_gridCellReal

   * - セル
     - 整数
     - result_gridCellInteger

   * - 格子の辺 (I方向)
     - 実数
     - result_gridEdgeIReal

   * - 格子の辺 (I方向)
     - 整数
     - result_gridEdgeIInteger

   * - 格子の辺 (J方向)
     - 実数
     - result_gridEdgeJReal

   * - 格子の辺 (J方向)
     - 整数
     - result_gridEdgeJInteger
