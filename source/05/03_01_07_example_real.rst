Real number
==============

Definition
-------------

.. code-block:: xml
   :caption: Example of a real number type condition definition
   :name: widget_example_real_def
   :linenos:

   <Item name="g" caption="Gravity [m/s2]">
     <Definition valueType="real" default="9.8" />
   </Item>

Example of widget
------------------------

.. _widget_example_real_select:

.. figure:: images/widget_example_real.png
   :width: 320pt

   Widget example of a real number type condition

Example code to read data
------------------------------

Calculation condition, Grid generating condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
'''''''''''

.. code-block:: fortran
   :caption: Code example to load a real number type condition (for calculation conditions and grid generating conditions) FORTRAN
   :name: widget_example_real_load_calccond_fortran
   :linenos:

   integer:: ier
   double precision:: g

   call cg_iRIC_Read_Real(fid, "g", g, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: Code example to load a real number type condition (for calculation conditions and grid generating conditions) C/C++
   :name: widget_example_real_load_calccond_c
   :linenos:

   int ier;
   double g;

   ier = cg_iRIC_Read_Real(fid, "g", &g)

Python
''''''''''

.. code-block:: python
   :caption: Code example to load a real number type condition (for calculation conditions and grid generating conditions) Python
   :name: widget_example_real_load_calccond_python
   :linenos:

   g = cg_iRIC_Read_Real(fid, "g")

Boundary condition
~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: Code example to load a real number type condition (for boundary conditions) FORTRAN
   :name: widget_example_real_load_bcond_fortran
   :linenos:

   integer:: ier
   double precision:: g

   call cg_iRIC_Read_BC_Real(fid, "inflow", 1, "g", g, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: Code example to load a real number type condition (for boundary conditions) C/C++
   :name: widget_example_real_load_bcond_c
   :linenos:

   int ier;
   double g;

   ier = cg_iRIC_Read_BC_Real(fid, "inflow", 1, "g", &g)

Python
''''''''''

.. code-block:: python
   :caption: Code example to load a real number type condition (for boundary conditions) Python
   :name: widget_example_real_load_bcond_python
   :linenos:

   g = cg_iRIC_Read_BC_Real(fid, "inflow", 1, "g")
