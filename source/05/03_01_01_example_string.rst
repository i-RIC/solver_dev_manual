String
===========

Definition
-------------

.. code-block:: xml
   :caption: Example of a string type condition definition
   :name: widget_example_string_def
   :linenos:

   <Item name="sampleitem" caption="Sample Item">
     <Definition valueType="string" />
   </Item>

Example of widget
------------------------

.. _widget_example_string:

.. figure:: images/widget_example_string.png
   :width: 320pt

   Widget example of a string type condition

Example code to read data
------------------------------

Calculation condition, Grid generating condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
'''''''''''

.. code-block:: fortran
   :caption: Code example to load a string type condition (for calculation conditions and grid generating conditions) FORTRAN
   :name: widget_example_string_load_calccond_fortran
   :linenos:

   call cg_iRIC_Read_String(fid, "sampleitem", sampleitem, ier)


C/C++
'''''''

.. code-block:: c
   :caption: Code example to load a string type condition (for calculation conditions and grid generating conditions) C/C++
   :name: widget_example_string_load_calccond_c
   :linenos:

   int ier;
   char sampleitem[200];

   ier = cg_iRIC_Read_String(fid, "sampleitem", sampleitem)

Python
'''''''

.. code-block:: python
   :caption: Code example to load a string type condition (for calculation conditions and grid generating conditions) Python
   :name: widget_example_string_load_calccond_python
   :linenos:

   sampleitem = cg_iRIC_Read_String(fid, "sampleitem")

Boundary condition
~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: Code example to load a string type condition (for boundary conditions) FORTRAN
   :name: widget_example_string_load_bcond_fortran
   :linenos:

   integer:: ier
   character(200):: sampleitem

   call cg_iRIC_Read_BC_String(fid, "inflow", 1, "sampleitem", sampleitem, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: Code example to load a string type condition (for boundary conditions) C/C++
   :name: widget_example_string_load_bcond_c
   :linenos:

   int ier;
   char sampleitem[200];

   ier = cg_iRIC_Read_BC_String(fid, "inflow", 1, "sampleitem", sampleitem)

Python
''''''''''

.. code-block:: python
   :caption: Code example to load a string type condition (for boundary conditions) Python
   :name: widget_example_string_load_bcond_python
   :linenos:

   sampleitem = cg_iRIC_Read_BC_String(fid, "inflow", 1, "sampleitem")
