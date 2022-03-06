iRIClib とは
=============

iRIClib は、ソルバー、格子生成プログラムをiRICと連携させるためのライブラリです。

iRIC は、ソルバー、格子生成プログラムとの情報の入出力に使う計算データファイル、
格子生成データファイルに CGNS ファイルを利用しています。 CGNS ファイルの入出力関数群は
cgnslib というライブラリとしてオープンソースで公開されています
(:ref:`about_cgns` 参照)。
しかし、 cgnslib を直接利用して必要な入出力を記述すると、煩雑な処理を
記述する必要があります。

そこで、iRIC プロジェクトでは iRIC に対応するソルバーでよく利用する入出力処理を
簡便に記述するためのラッパー関数を提供するライブラリとして、iRIClib
を用意しています。
単一の構造格子を用いて計算を行うソルバーと、格子生成プログラムの入出力処理は、
iRIClibで用意された関数を利用することで簡単に記述できます。

なお、複数の格子や非構造格子を使うソルバーなどで必要な関数は iRIClib
では提供されません。そのようなソルバーでは、cgnslib
で用意された関数を直接利用する必要があります。

この文書では、iRIClibを構成する関数群と利用例及びコンパイル方法について説明します。

利用可能な言語
==============

iRIClib は、以下の言語から利用することができます。

* FORTRAN
* C/C++
* Python

マニュアルでは、FORTRAN から利用する場合の例を主に記載しています。

ここでは、FORTRAN, C/C++, Python から iRIClib を利用する方法の概要について
説明します。

なお、関数を呼び出す際の引数などは、言語によって異なります。言語ごとの関数の呼び出し方法については、
:ref:`iriclib_reference` の各関数の解説を参照してください。

FORTRAN
---------------

:numref:`iriclib_init_example_fortran` に示すように、ヘッダファイルを読み込んだ上で、
iRIClib の関数を呼び出します。

.. _iriclib_init_example_fortran:

.. code-block:: fortran
   :caption: FORTRAN から iRIClibを利用するための記述例
   :linenos:

   use iric

   call cg_iric_open(filename, mode, fid, ier)

C/C++
------------

:numref:`iriclib_init_example_c` に示すように、ヘッダファイルを読み込んだ上で、
iRIClib の関数を呼び出します。

.. _iriclib_init_example_c:

.. code-block:: c
   :caption: C/C++ から iRIClibを利用するための記述例
   :linenos:

   #include "iriclib.h"

   // (中略)
   ier = cg_iRIC_Open(filename, mode, &fid);

Python
------------

:numref:`iriclib_init_example_python` に示すように、iric モジュールから
関数を読み込んだ上で、iRIClib の関数を呼び出します。

.. _iriclib_init_example_python:

.. code-block:: python
   :caption: Python から iRIClibを利用するための記述例
   :linenos:

   from iric import *

   fid = cg_iRIC_Open(filename, mode)

この章の読み方
===============

:ref:`iriclib_overview` で、iRIC がソルバー、格子生成プログラムについて想定している入出力処理と、
その処理のために用意している関数についてを説明します。

まずは、:ref:`iriclib_overview` を読んで iRIClib の概要についてご理解ください。
概要を理解したら、関数の引数のリストなどの詳細な情報は :ref:`iriclib_reference`
を参照してください。

