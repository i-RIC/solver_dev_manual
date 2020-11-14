.. _iriclib_reference:

リファレンス
============

リファレンスでは、各関数の機能、呼び出す際の形式、引数について解説します。

リファレンスの各関数のページでは、引数の型は FORTRAN の場合について解説しています。
C/C++, Python から呼び出す際の引数の型については、:numref:`ref_arg_types` を参照して
読み替えてください。

Python では、エラーコードを格納する ier は出力されず、エラーが発生した場合は
例外が発生します。エラー処理を行う場合は、try, except を利用してください。

.. _ref_arg_types:

.. list-table:: 引数の型の対応関係
   :header-rows: 1

   * - FORTRAN
     - C/C++
     - Python
   * - integer
     - int (出力の場合 int*)
     - int
   * - double precision
     - double (出力の場合 double*)
     - float
   * - real
     - float (出力の場合 float*)
     - (なし)
   * - character(*)
     - char*
     - str
   * - integer, dimension(:), allocatable
     - int*
     - numpy.ndarray(dtype=int32)
   * - double precision, dimension(:), allocatable
     - double*
     - numpy.ndarray(dtype=float64)
   * - real, dimension(:), allocatable
     - float*
     - (なし)

.. toctree::
   :maxdepth: 1

   03/functionlist
   03/cg_open_f
   03/cg_iric_init_f
   03/cg_iric_initread_f
   03/iric_initoption_f
   03/cg_iric_read_integer_f
   03/cg_iric_read_real_f
   03/cg_iric_read_realsingle_f
   03/cg_iric_read_string_f
   03/cg_iric_read_functionalsize_f
   03/cg_iric_read_functional_f
   03/cg_iric_read_functional_realsingle_f
   03/cg_iric_read_functionalwithname_f
   03/cg_iric_gotogridcoord2d_f
   03/cg_iric_gotogridcoord3d_f
   03/cg_iric_getgridcoord2d_f
   03/cg_iric_getgridcoord3d_f
   03/cg_iric_read_grid_integer_node_f
   03/cg_iric_read_grid_real_node_f
   03/cg_iric_read_grid_integer_cell_f
   03/cg_iric_read_grid_real_cell_f
   03/cg_iric_read_complex_count_f
   03/cg_iric_read_complex_integer_f
   03/cg_iric_read_complex_real_f
   03/cg_iric_read_complex_realsingle_f
   03/cg_iric_read_complex_string_f
   03/cg_iric_read_complex_functionalsize_f
   03/cg_iric_read_complex_functional_f
   03/cg_iric_read_complex_functional_realsingle_f
   03/cg_iric_read_complex_functionalwithname_f
   03/cg_iric_read_grid_complex_node_f
   03/cg_iric_read_grid_complex_cell_f
   03/cg_iric_read_grid_functionaltimesize_f
   03/cg_iric_read_grid_functionaltime_f
   03/cg_iric_read_grid_functionaldimensionsize_f
   03/cg_iric_read_grid_functionaldimension_integer_f
   03/cg_iric_read_grid_functionaldimension_real_f
   03/cg_iric_read_grid_functional_integer_node_f
   03/cg_iric_read_grid_functional_real_node_f
   03/cg_iric_read_grid_functional_integer_cell_f
   03/cg_iric_read_grid_functional_real_cell_f
   03/cg_iric_read_bc_count_f
   03/cg_iric_read_bc_indicessize_f
   03/cg_iric_read_bc_indices_f
   03/cg_iric_read_bc_integer_f
   03/cg_iric_read_bc_real_f
   03/cg_iric_read_bc_realsingle_f
   03/cg_iric_read_bc_string_f
   03/cg_iric_read_bc_functionalsize_f
   03/cg_iric_read_bc_functional_f
   03/cg_iric_read_bc_functional_realsingle_f
   03/cg_iric_read_bc_functionalwithname_f
   03/cg_iric_read_geo_count_f
   03/cg_iric_read_geo_filename_f
   03/iric_geo_polygon_open_f
   03/iric_geo_polygon_read_integervalue_f
   03/iric_geo_polygon_read_realvalue_f
   03/iric_geo_polygon_read_pointcount_f
   03/iric_geo_polygon_read_points_f
   03/iric_geo_polygon_read_holecount_f
   03/iric_geo_polygon_read_holepointcount_f
   03/iric_geo_polygon_read_holepoints_f
   03/iric_geo_polygon_close_f
   03/iric_geo_riversurvey_open_f
   03/iric_geo_riversurvey_read_count_f
   03/iric_geo_riversurvey_read_position_f
   03/iric_geo_riversurvey_read_direction_f
   03/iric_geo_riversurvey_read_name_f
   03/iric_geo_riversurvey_read_realname_f
   03/iric_geo_riversurvey_read_leftshift_f
   03/iric_geo_riversurvey_read_altitudecount_f
   03/iric_geo_riversurvey_read_altitudes_f
   03/iric_geo_riversurvey_read_fixedpointl_f
   03/iric_geo_riversurvey_read_fixedpointr_f
   03/iric_geo_riversurvey_read_watersurfaceelevation_f
   03/iric_geo_riversurvey_close_f
   03/cg_iric_writegridcoord1d_f
   03/cg_iric_writegridcoord2d_f
   03/cg_iric_writegridcoord3d_f
   03/cg_iric_write_grid_integer_node_f
   03/cg_iric_write_grid_real_node_f
   03/cg_iric_write_grid_integer_cell_f
   03/cg_iric_write_grid_real_cell_f
   03/cg_iric_write_sol_time_f
   03/cg_iric_write_sol_iteration_f
   03/cg_iric_write_sol_gridcoord2d_f
   03/cg_iric_write_sol_gridcoord3d_f
   03/cg_iric_write_sol_baseiterative_integer_f
   03/cg_iric_write_sol_baseiterative_real_f
   03/cg_iric_write_sol_baseiterative_string_f
   03/cg_iric_write_sol_integer_f
   03/cg_iric_write_sol_real_f
   03/cg_iric_write_sol_cell_integer_f
   03/cg_iric_write_sol_cell_real_f
   03/cg_iric_write_sol_iface_integer_f
   03/cg_iric_write_sol_iface_real_f
   03/cg_iric_write_sol_jface_integer_f
   03/cg_iric_write_sol_jface_real_f
   03/cg_iric_write_sol_particle_pos2d_f
   03/cg_iric_write_sol_particle_pos3d_f
   03/cg_iric_write_sol_particle_integer_f
   03/cg_iric_write_sol_particle_real_f
   03/cg_iric_write_sol_particlegroup_groupbegin_f
   03/cg_iric_write_sol_particlegroup_groupend_f
   03/cg_iric_write_sol_particlegroup_pos2d_f
   03/cg_iric_write_sol_particlegroup_pos3d_f
   03/cg_iric_write_sol_particlegroup_integer_f
   03/cg_iric_write_sol_particlegroup_real_f
   03/cg_iric_write_sol_polydata_groupbegin_f
   03/cg_iric_write_sol_polydata_groupend_f
   03/cg_iric_write_sol_polydata_polygon_f
   03/cg_iric_write_sol_polydata_polyline_f
   03/cg_iric_write_sol_polydata_integer_f
   03/cg_iric_write_sol_polydata_real_f
   03/iric_check_cancel_f
   03/iric_check_lock_f
   03/iric_write_sol_start_f
   03/iric_write_sol_end_f
   03/cg_iric_flush_f
   03/cg_iric_read_sol_count_f
   03/cg_iric_read_sol_time_f
   03/cg_iric_read_sol_iteration_f
   03/cg_iric_read_sol_baseiterative_integer_f
   03/cg_iric_read_sol_baseiterative_real_f
   03/cg_iric_read_sol_baseiterative_string_f
   03/cg_iric_read_sol_gridcoord2d_f
   03/cg_iric_read_sol_gridcoord3d_f
   03/cg_iric_read_sol_integer_f
   03/cg_iric_read_sol_real_f
   03/cg_iric_read_sol_cell_integer_f
   03/cg_iric_read_sol_cell_real_f
   03/cg_iric_read_sol_iface_integer_f
   03/cg_iric_read_sol_iface_real_f
   03/cg_iric_read_sol_jface_integer_f
   03/cg_iric_read_sol_jface_real_f
   03/cg_iric_write_errorcode_f
   03/cg_close_f
