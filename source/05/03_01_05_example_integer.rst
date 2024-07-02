Integer
=========

Definition
-------------

.. code-block:: xml
   :caption: Example of a integer type condition definition
   :name: widget_example_integer_def
   :linenos:

   <Item name="numsteps" caption="The Number of steps to calculate">
     <Definition valueType="integer" default="20" min="1" max="200" />
   </Item>

Example of widget
------------------------

.. _widget_example_integer:

.. figure:: images/widget_example_integer.png
   :width: 340pt

   Widget example of a integer type condition

Example code to read data
------------------------------

Calculation condition, Grid generating condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
'''''''''''

.. code-block:: fortran
   :caption: Code example to load a integer type condition (for calculation conditions and grid generating conditions) FORTRAN
   :name: widget_example_integer_load_calccond_fortran
   :linenos:

   integer:: ier, numsteps

   call cg_iRIC_Read_Integer(fid, "numsteps", numsteps, ier)


C/C++
''''''''''

.. code-block:: c
   :caption: Code example to load a integer type condition (for calculation conditions and grid generating conditions) C/C++
   :name: widget_example_integer_load_calccond_c
   :linenos:

   int ier, numsteps;

   ier = cg_iRIC_Read_Integer(fid, "numsteps", &numsteps)

Python
''''''''''

.. code-block:: python
   :caption: Code example to load a integer type condition (for calculation conditions and grid generating conditions) Python
   :name: widget_example_integer_load_calccond_python
   :linenos:

   numsteps = cg_iRIC_Read_Integer(fid, "numsteps")

Boundary condition
~~~~~~~~~~~~~~~~~~~~~~~~

FORTRAN
''''''''''

.. code-block:: fortran
   :caption: Code example to load a integer type condition (for boundary conditions) FORTRAN
   :name: widget_example_integer_load_bcond_fortran
   :linenos:

   integer:: ier, numsteps

   call cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "numsteps", numsteps, ier)

C/C++
''''''''''

.. code-block:: c
   :caption: Code example to load a integer type condition (for boundary conditions) C/C++
   :name: widget_example_integer_load_bcond_c
   :linenos:

   int ier, numstep;

   ier = cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "numsteps", &numsteps)

Python
''''''''''

.. code-block:: python
   :caption: Code example to load a integer type condition (for boundary conditions) Python
   :name: widget_example_integer_load_bcond_python
   :linenos:

   numsteps = cg_iRIC_Read_BC_Integer(fid, "inflow", 1, "numsteps")
