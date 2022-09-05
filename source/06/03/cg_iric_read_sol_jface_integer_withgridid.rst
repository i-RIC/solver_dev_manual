cg_iric_read_sol_jface_integer_withgridid
===========================================

Reads the integer-type calculation result defined at grid edge at j-direction.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_jface_integer_withgridid(fid, gid, step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_JFace_Integer_WithGridId(fid, gid, step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_JFace_Integer_WithGridId(fid, gid, step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_jface_integer_withgridid
   :file: cg_iric_read_sol_jface_integer_withgridid_args.csv
   :header-rows: 1
