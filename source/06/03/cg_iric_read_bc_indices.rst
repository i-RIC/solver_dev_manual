cg_iric_read_bc_indices
=========================

-  Reads the elements (nodes or cells) where the boundary condition is

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_bc_indices(fid, type, num, indices, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_BC_Indices(fid, type, num, indices);

Format (Python)
----------------
.. code-block:: python

   indices = cg_iRIC_Read_BC_Indices(fid, type, num)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_bc_indices
   :file: cg_iric_read_bc_indices_args.csv
   :header-rows: 1

Note
-----

Values returned to indices depends on the position where boundary condition
is defined, like shown in :numref:`cg_iric_read_bc_indices_vals`.

Please note that when the boundary condition is defined at nodes or cells, it outputs two values 
for each element, and when defined at edges, it outputs four values
for each element.

.. _cg_iric_read_bc_indices_vals:

.. list-table:: Relationship between the position where boundary condition is defined and the values of indices
   :header-rows: 1

   * - Position where boundary condition is defined
     - Values of indices
   * - Nodes
     - | I of grid node 1, J of grid node 1
       | ...,
       | I of grid node N, J of grid node N
   * - Cells
     - | I of grid cell 1, J of grid cell 1
       | ...,
       | I of grid cell N, J of grid cell N
   * - Edges
     - | I of start position of edge 1, J of start position of edge 1,
       | I of end position of edge 1, J of end position of edge 1
       | ...,
       | I of start position of edge N, J of start position of edge N,
       | I of end position of edge N, J of end position of edge N
