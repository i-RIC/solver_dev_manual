Definition (when used under the Output element)
===============================================================

This element contains definition information of the calculation result.

Example
-----------

.. code-block:: xml
   :caption: Example of Definition definition 1
   :name: ref_definition_output_example1
   :linenos:

   <Definition valueType="real" position="node" />

.. code-block:: xml
   :caption: Example of Definition definition 2
   :name: ref_definition_output_example2
   :linenos:

   <Definition valueType="integer" position="cell" >
     <Enumeration value="0" caption="Dry" />
     <Enumeration value="1" caption="Wet" />
   </Definition>

Please refer to :ref:`examples_of_output_at_grid` also.

Attributes
----------------

.. csv-table:: Attributes of Definition
   :file: definition_output_attributes.csv
   :header-rows: 1

.. csv-table:: valueType values
   :file: definition_output_att_valuetype.csv
   :header-rows: 1

.. csv-table:: position values
   :file: definition_output_att_position.csv
   :header-rows: 1

Child elements
------------------------

.. csv-table:: Child elements of Definition
   :file: definition_output_elements.csv
   :header-rows: 1

