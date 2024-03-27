Definition (計算結果の定義)
===============================================================

計算結果の定義情報を保持します。

例
----

.. code-block:: xml
   :caption: Definition の定義例1
   :name: ref_definition_output_example1
   :linenos:

   <Definition valueType="real" position="node" />

.. code-block:: xml
   :caption: Definition の定義例2
   :name: ref_definition_output_example2
   :linenos:

   <Definition valueType="integer" position="cell" >
     <Enumeration value="0" caption="Dry" />
     <Enumeration value="1" caption="Wet" />
   </Definition>

例は :ref:`examples_of_output_at_grid` も参照して下さい。

属性
-----

.. csv-table:: Definition の属性
   :file: definition_output_attributes.csv
   :header-rows: 1

.. csv-table:: valueType の値
   :file: definition_output_att_valuetype.csv
   :header-rows: 1

.. csv-table:: position の値
   :file: definition_output_att_position.csv
   :header-rows: 1

子要素
--------

.. csv-table:: Definition の子要素
   :file: definition_output_elements.csv
   :header-rows: 1

