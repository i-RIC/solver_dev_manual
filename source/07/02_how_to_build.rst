.. _how_to_link:

Fortran 言語で iriclib とリンクしてビルドする方法
===================================================================

iRIC と連携して動作するソルバー、格子生成プログラムをコンパイルするには、
iriclib とリンクする必要があります。

ソースコードのファイルが solver.f90 の時のコンパイル手順について以下に示します。
ただし、コンパイラの設定 (pathの設定など) は完了しているものとします。

.. _linking_on_ifort:

Intel Fortran Compiler (Windows)
----------------------------------

solver.f90, iric.f90, iriclib.lib
を同じフォルダに置き、そこに移動して以下のコマンドを実行することで、
実行ファイル solver.exe が生成されます。

.. code-block:: batch

   ifort iric.f90 solver.f90 iriclib.lib /MD
