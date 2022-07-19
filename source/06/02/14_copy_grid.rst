格子のコピー
========================

CGNS ファイルの間で、格子をコピーします。
同じ関数で、構造格子と非構造格子両方に対応しています。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_copy_grid
     - 格子をコピーする

格子が格納されている CGNS ファイル、格子が格納されていない CGNS ファイルを
開き、格子をコピーする処理の例を :numref:`example_copy_grid` に示します。


.. code-block:: fortran
   :caption: 格子をコピーする処理の記述例
   :name: example_copy_grid
   :linenos:

   program SampleX
     use iric
     implicit none

     integer:: fid_from, fid_to, ier

     ! CGNS ファイルのオープン
     call cg_iric_open('test1.cgn', IRIC_MODE_READ, fid_from, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     call cg_iric_open('test1.cgn', IRIC_MODE_MODIFY, fid_to, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! 格子のコピー
     call cg_iric_copy_grid(fid_from, fid_to, ier)

     ! CGNS ファイルのクローズ
     call cg_iric_close(fid_from, ier)
     call cg_iric_close(fid_to, ier)
     stop
   end program SampleX
