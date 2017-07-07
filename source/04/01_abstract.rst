概要
====

格子生成プログラムは、格子生成条件に基づいて、格子を生成するプログラムです。
作成したプログラムは、iRIC 上から格子生成アルゴリズムの1つとして
利用できるようになります。

iRIC 上で動作する格子生成プログラムを開発するには、表 2 1 に示すようなファイルを作成、配置する必要があります。
表 2 1 に示した項目のうち、 “iRIC 2.0” フォルダと “gridcreators” フォルダは、iRIC をインストールすれば既に作成されています。ソルバー開発者は、 “gridcreators” フォルダの下に自分が開発する格子生成プログラム専用のフォルダを作成し、関連するファイルをその下に配置します。


ソルバーは、格子、計算条件などに基づいて河川シミュレーションを実行し、計算結果を出力するプログラムです。

iRIC 上で動作するソルバーを開発するには、:numref:`files_related_to_gridgen`
に示すようなファイルを作成、配置する必要があります。

:numref:`files_related_to_gridgen` に示したファイルは iRIC インストール先の下の "solvers" フォルダの下に
自分が開発するソルバー専用のフォルダを作成し、その下に配置します。

.. _files_related_to_gridgen:

.. csv-table:: 格子生成プログラム関連ファイル一覧
   :file: files_related_to_gridgen.csv
   :header-rows: 1


各ファイルの概要は以下の通りです。

definition.xml
--------------

格子生成プログラムに関する以下の情報を定義するファイルです。

- 基本情報
- 格子生成条件

iRIC は格子生成プログラム定義ファイルを読み込むことで、
格子生成条件を作成するためのインターフェースを提供し、
そのプログラム用の格子生成データファイルを生成します。
また、この格子生成プログラムが生成する格子に現在使っているソルバーが対応している時のみ、
この格子生成プログラムを使えるようにします。

格子生成プログラム定義ファイルは、すべて英語で記述します。

格子生成プログラム
------------------

格子を生成するプログラムです。iRICで作成した格子生成条件を読みこんで格子を生成し、
生成した格子を出力します。

格子生成条件、格子の入出力には、iRIC が生成する
格子生成データファイルを使用します。

FORTRAN, C言語、C++言語のいずれかの言語で開発します。この章では、
FORTRAN で開発する例を説明します。

translation\_ja\_JP.ts など
---------------------------

格子生成プログラム定義ファイルで用いられている文字列のうち、
ダイアログ上に表示される文字列を翻訳して表示するための辞書ファイルです。
日本語 (translation\_ja\_JP.ts)、韓国語 (translation\_ka\_KR.ts)
など言語ごとに別ファイルとして作成します。

README
------

格子生成プログラムに関する説明を記述するテキストファイルです。
iRICで格子生成アルゴリズムを選択する画面で、説明欄に表示されます。

iRIC、格子生成プログラム、関連ファイルの関係を
:numref:`relations_between_gridgen_and_files` に示します。

.. _relations_between_gridgen_and_files:

.. figure:: images/files_related_to_gridgenerator.png

   iRIC、格子生成プログラム、関連ファイルの関係図

この章では、この節で説明した各ファイルを作成する手順を、順番に説明します。