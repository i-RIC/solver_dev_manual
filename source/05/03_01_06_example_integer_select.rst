.. _calccond_int_select_example:

Integer (Choice)
====================

Definition
-------------

.. code-block:: xml
   :caption: Example of a integer (choise) type condition definition
   :name: widget_example_integer_select_def
   :linenos:

   <Item name="flowtype" caption="Flow type">
     <Definition valueType="integer" default="0">
       <Enumeration value="0" caption="Static Flow"/>
       <Enumeration value="1" caption="Dynamic Flow"/>
     </Definition>
   </Item>

Example of widget
------------------------

.. _widget_example_integer_select:

.. figure:: images/widget_example_combobox.png
   :width: 320pt

   Widget example of a integer (choice) type condition

Example code to read data
------------------------------

Calculation condition, Grid generating condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
'''''''''''

.. code-block:: fortran
   :caption: Code example to load a integer (choise) type condition (for calculation conditions and grid generating conditions) FORTRAN
   :name: widget_example_integer_select_load_calccond_fortran
   :linenos:

   integer:: ier, flowtype

   call cg_iRIC_Read_Integer(fid, "flowtype", flowtype, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: Code example to load a integer (choise) type condition (for calculation conditions and grid generating conditions) C/C++
   :name: widget_example_integer_select_load_calccond_c
   :linenos:

   int ier, flowtype;

   ier = cg_iRIC_Read_Integer(fid, "flowtype", &flowtype)

Python
''''''''''

.. code-block:: python
   :caption: Code example to load a integer (choise) type condition (for calculation conditions and grid generating conditions) Python
   :name: widget_example_integer_select_load_calccond_python
   :linenos:

   flowtype = cg_iRIC_Read_Integer(fid, "flowtype")

Boundary condition
~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: Code example to load a integer (choise) type condition (for boundary conditions) FORTRAN
   :name: widget_example_integer_select_load_bcond_fortran
   :linenos:

   integer:: ier, flowtype

   call cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "flowtype", flowtype, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: Code example to load a integer (choise) type condition (for boundary conditions) C/C++
   :name: widget_example_integer_select_load_bcond_c
   :linenos:

   int ier, flowtype;

   ier = cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "flowtype", &flowtype)

Python
''''''''''

.. code-block:: python
   :caption: Code example to load a integer (choise) type condition (for boundary conditions) Python
   :name: widget_example_integer_select_load_bcond_python
   :linenos:

   flowtype = cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "flowtype")
