Deleting calculation result
==============================

Delete old calculation result from CGNS file.

.. list-table:: Subroutines to use
   :header-rows: 1
   
   * - Subroutine
     - Remarks

   * - cg_iric_clear_sol
     - Delete calculation result

.. note::
   When you run the solver from iRIC GUI, iRIC GUI automatically deletes calculation result
   before launching the solver. So, in that case you do not need to call the subroutine necessarily.

   In case you launch the solver outside of iRIC GUI, and you continuously launch the solver with
   the same CGNS file as input, please do not forget to call the subroutine just after opening the
   CGNS file.
