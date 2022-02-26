cg_iric_read_sol_iface_integer
================================

-  Reads the integer-type calculation result, having a value for each grid edge at i-direction.

Format (FORTRAN)
------------------
.. code-block:: fortran

   call cg_iric_read_sol_iface_integer(step, label, val, ier)

Format (C/C++)
----------------
.. code-block:: c

   ier = cg_iRIC_Read_Sol_IFace_Integer(step, label, val);

Format (Python)
----------------
.. code-block:: python

   val = cg_iRIC_Read_Sol_IFace_Integer(step, label)

Arguments
---------

.. csv-table:: Arguments of cg_iric_read_sol_iface_integer
   :file: cg_iric_read_sol_iface_integer_args.csv
   :header-rows: 1
