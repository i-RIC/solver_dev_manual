地形データの読み込み
======================

プロジェクトでインポートして格子生成に利用した地形データを読み込みます。
ソルバーで、河川測量データやポリゴンを直接読み込んで解析に使用したい場合に行います。
地形データを読み込む場合の手順は、以下の通りになります。

1. CGNS ファイルから、プロジェクトで使用した地形データのファイル名などを読み込みます。
2. 地形データファイルを開き、地形データを読み込みます。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考

   * - cg_iric_read_geo_count
     - 地形データの数を返す

   * - cg_iric_read_geo_filename
     - 地形データのファイル名と種類を返す

   * - iric_geo_riversurvey_open
     - 河川測量データを開く

   * - iric_geo_riversurvey_read_count
     - 河川横断線の数を返す

   * - iric_geo_riversurvey_read_position
     - 横断線の中心点の座標を返す

   * - iric_geo_riversurvey_read_direction
     - 横断線の向きを返す

   * - iric_geo_riversurvey_read_name
     - 横断線の名前を文字列として返す

   * - iric_geo_riversurvey_read_realname
     - 横断線の名前を実数値として返す

   * - iric_geo_riversurvey_read_leftshift
     - 横断線の標高データのシフト量を返す

   * - iric_geo_riversurvey_read_altitudecount
     - 横断線の標高データの数を返す

   * - iric_geo_riversurvey_read_altitudes
     - 横断線の標高データを返す

   * - iric_geo_riversurvey_readixedpointl
     - 横断線の左岸延長線のデータを返す

   * - iric_geo_riversurvey_readixedpointr
     - 横断線の右岸延長線のデータを返す

   * - iric_geo_riversurvey_read_watersurfaceelevation
     - 横断線での水面標高のデータを返す

   * - iric_geo_riversurvey_close
     - 河川測量データを閉じる

地形データのうち、河川測量データを読み込む処理の記述例を :numref:`example_load_riversurvey`
に示します。

.. code-block:: fortran
   :caption: 河川測量データを読み込む処理の記述例
   :name: example_load_riversurvey
   :linenos:

   program TestRiverSurvey
     use iric
     implicit none

     integer:: fin, ier
     integer:: icount, istatus
   
     integer:: geoid
     integer:: elevation_geo_count
     character(len=1000):: filename
     integer:: geotype
     integer:: rsid
     integer:: xsec_count
     integer:: xsec_id
     character(len=20):: xsec_name
     double precision:: xsec_x
     double precision:: xsec_y
     integer:: xsec_set
     integer:: xsec_index
     double precision:: xsec_leftshift
     integer:: xsec_altid
     integer:: xsec_altcount
     double precision, dimension(:), allocatable:: xsec_altpos
     double precision, dimension(:), allocatable:: xsec_altheight
     integer, dimension(:), allocatable:: xsec_altactive
     double precision:: xsec_wse
   
     ! 計算データファイルを開く
     call cg_iric_open("test.cgn", IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! 地形データの数を取得
     call cg_iric_read_geo_count(fin, "Elevation", elevation_geo_count, ier)
   
     do geoid = 1, elevation_geo_count
       call cg_iric_read_geo_filename(fin, 'Elevation', geoid, &
         filename, geotype, ier)
       if (geotype .eq. iRIC_GEO_RIVERSURVEY) then
         call iric_geo_riversurvey_open(filename, rsid, ier)
         call iric_geo_riversurvey_read_count(rsid, xsec_count, ier)
         do xsec_id = 1, xsec_count
           call iric_geo_riversurvey_read_name(rsid, xsec_id, xsec_name, ier)
           print *, 'xsec ', xsec_name
           call iric_geo_riversurvey_read_position(rsid, xsec_id, xsec_x, xsec_y, ier)
           print *, 'position: ', xsec_x, xsec_y
           call iric_geo_riversurvey_read_direction(rsid, xsec_id, xsec_x, xsec_y, ier)
           print *, 'direction: ', xsec_x, xsec_y
           call iric_geo_riversurvey_read_leftshift(rsid, xsec_id, xsec_leftshift, ier)
           print *, 'leftshift: ', xsec_leftshift
           call iric_geo_riversurvey_read_altitudecount(rsid, xsec_id, xsec_altcount, ier)
           print *, 'altitude count: ', xsec_altcount
           allocate(xsec_altpos(xsec_altcount))
           allocate(xsec_altheight(xsec_altcount))
           allocate(xsec_altactive(xsec_altcount))
           call iric_geo_riversurvey_read_altitudes( &
             rsid, xsec_id, xsec_altpos, xsec_altheight, xsec_altactive, ier)
           do xsec_altid = 1, xsec_altcount
             print *, 'Altitude ', xsec_altid, ': ', &
               xsec_altpos(xsec_altid:xsec_altid), ', ', &
               xsec_altheight(xsec_altid:xsec_altid), ', ', &
               xsec_altactive(xsec_altid:xsec_altid)
           end do
           deallocate(xsec_altpos, xsec_altheight, xsec_altactive)
           call iric_geo_riversurvey_readixedpointl( &
             rsid, xsec_id, xsec_set, xsec_x, xsec_y, xsec_index, ier)
           print *, 'FixedPointL: ', xsec_set, xsec_x, xsec_y, xsec_index
           call iric_geo_riversurvey_readixedpointr( &
             rsid, xsec_id, xsec_set, xsec_x, xsec_y, xsec_index, ier)
           print *, 'FixedPointR: ', xsec_set, xsec_x, xsec_y, xsec_index
           call iric_geo_riversurvey_read_watersurfaceelevation( &
             rsid, xsec_id, xsec_set, xsec_wse, ier)
           print *, 'WaterSurfaceElevation: ', xsec_set, xsec_wse
         end do
         call iric_geo_riversurvey_close(rsid, ier)
       end if
     end do
   
     ! 計算データファイルを閉じる
     call cg_iric_close(fin, ier)
     stop
   end program TestRiverSurvey

