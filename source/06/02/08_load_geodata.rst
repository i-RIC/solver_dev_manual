Reading geographic data
============================

Reads geographic data that was imported into project and used for grid generation.

This function is used when you want to read river survey data or
polygon data in solvers directly.
The procedure of reading geographic data is as follows:

1. Reads the number of geographic data, the file name of geographic data etc. from CGNS file.
2. Open geographic data file and read data from that.

.. list-table:: Subroutine to use
   :header-rows: 1

   * - Subroutine
     - Remarks

   * - cg_iric_read_geo_count_f
     - Reads the number of geographic data

   * - cg_iric_read_geo_filename_f
     - Reads the file name and data type of geographic data

   * - iric_geo_riversurvey_open_f
     - Opens the geographic data file that contains river survey data

   * - iric_geo_riversurvey_read_count_f
     - Reads the number of the crosssections in river survey data

   * - iric_geo_riversurvey_read_position_f
     - Reads the coordinates of the crosssection center point

   * - iric_geo_riversurvey_read_direction_f
     - Reads the direction of the crosssection as normalized vector

   * - iric_geo_riversurvey_read_name_f
     - Reads the name of the crosssection as string

   * - iric_geo_riversurvey_read_realname_f
     - Reads the name of the crosssection as real number

   * - iric_geo_riversurvey_read_leftshift_f
     - Reads the shift offset value of the crosssection

   * - iric_geo_riversurvey_read_altitudecount_f
     - Reads the number of altitude data of the crosssection

   * - iric_geo_riversurvey_read_altitudes_f
     - Reads the altitude data of the crosssection

   * - iric_geo_riversurvey_read_fixedpointl_f
     - Reads the data of left bank extension line of the crosssection

   * - iric_geo_riversurvey_read_fixedpointr_f
     - Reads the data of right bank extension line of the crosssection

   * - iric_geo_riversurvey_read_watersurfaceelevation_f
     - Reads the water elevation at the crosssection

   * - iric_geo_riversurvey_close_f
     - Closes the geographic data file

:numref:`example_load_riversurvey` shows an example of reading river survey data.

.. code-block:: fortran
   :caption: Example source code of reading river survey data
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
   
     ! Opens CGNS file
     call cg_iric_open("test.cgn", IRIC_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! Reads the number or geographic data
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
   
     ! Closes CGNS file
     call cg_iric_close(fin, ier)
     stop
   end program TestRiverSurvey
