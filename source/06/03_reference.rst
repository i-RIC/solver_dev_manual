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
   03/cg_iric_open
   03/iric_initoption
   03/cg_iric_read_integer
   03/cg_iric_read_real
   03/cg_iric_read_realsingle
   03/cg_iric_read_string
   03/cg_iric_read_functionalsize
   03/cg_iric_read_functional
   03/cg_iric_read_functional_realsingle
   03/cg_iric_read_functionalwithname
   03/cg_iric_read_grid2d_str_size
   03/cg_iric_read_grid2d_coords
   03/cg_iric_read_grid_nodecount
   03/cg_iric_read_grid_cellcount
   03/cg_iric_read_grid_triangleelements
   03/cg_iric_read_grid_integer_node
   03/cg_iric_read_grid_real_node
   03/cg_iric_read_grid_integer_cell
   03/cg_iric_read_grid_real_cell
   03/cg_iric_read_complex_count
   03/cg_iric_read_complex_integer
   03/cg_iric_read_complex_real
   03/cg_iric_read_complex_realsingle
   03/cg_iric_read_complex_string
   03/cg_iric_read_complex_functionalsize
   03/cg_iric_read_complex_functional
   03/cg_iric_read_complex_functional_realsingle
   03/cg_iric_read_complex_functionalwithname
   03/cg_iric_read_grid_complex_node
   03/cg_iric_read_grid_complex_cell
   03/cg_iric_read_grid_functionaltimesize
   03/cg_iric_read_grid_functionaltime
   03/cg_iric_read_grid_functionaldimensionsize
   03/cg_iric_read_grid_functionaldimension_integer
   03/cg_iric_read_grid_functionaldimension_real
   03/cg_iric_read_grid_functional_integer_node
   03/cg_iric_read_grid_functional_real_node
   03/cg_iric_read_grid_functional_integer_cell
   03/cg_iric_read_grid_functional_real_cell
   03/cg_iric_read_bc_count
   03/cg_iric_read_bc_indicessize
   03/cg_iric_read_bc_indices
   03/cg_iric_read_bc_integer
   03/cg_iric_read_bc_real
   03/cg_iric_read_bc_realsingle
   03/cg_iric_read_bc_string
   03/cg_iric_read_bc_functionalsize
   03/cg_iric_read_bc_functional
   03/cg_iric_read_bc_functional_realsingle
   03/cg_iric_read_bc_functionalwithname
   03/cg_iric_read_geo_count
   03/cg_iric_read_geo_filename
   03/iric_geo_polygon_open
   03/iric_geo_polygon_read_integervalue
   03/iric_geo_polygon_read_realvalue
   03/iric_geo_polygon_read_pointcount
   03/iric_geo_polygon_read_points
   03/iric_geo_polygon_read_holecount
   03/iric_geo_polygon_read_holepointcount
   03/iric_geo_polygon_read_holepoints
   03/iric_geo_polygon_close
   03/iric_geo_riversurvey_open
   03/iric_geo_riversurvey_read_count
   03/iric_geo_riversurvey_read_position
   03/iric_geo_riversurvey_read_direction
   03/iric_geo_riversurvey_read_name
   03/iric_geo_riversurvey_read_realname
   03/iric_geo_riversurvey_read_leftshift
   03/iric_geo_riversurvey_read_altitudecount
   03/iric_geo_riversurvey_read_altitudes
   03/iric_geo_riversurvey_read_fixedpointl
   03/iric_geo_riversurvey_read_fixedpointr
   03/iric_geo_riversurvey_read_watersurfaceelevation
   03/iric_geo_riversurvey_close
   03/cg_iric_write_grid1d_coords
   03/cg_iric_write_grid2d_coords
   03/cg_iric_write_grid3d_coords
   03/cg_iric_write_grid_integer_node
   03/cg_iric_write_grid_real_node
   03/cg_iric_write_grid_integer_cell
   03/cg_iric_write_grid_real_cell
   03/cg_iric_write_sol_time
   03/cg_iric_write_sol_iteration
   03/cg_iric_write_sol_grid2d_coords
   03/cg_iric_write_sol_grid3d_coords
   03/cg_iric_write_sol_baseiterative_integer
   03/cg_iric_write_sol_baseiterative_real
   03/cg_iric_write_sol_baseiterative_string
   03/cg_iric_write_sol_node_integer
   03/cg_iric_write_sol_node_real
   03/cg_iric_write_sol_cell_integer
   03/cg_iric_write_sol_cell_real
   03/cg_iric_write_sol_iface_integer
   03/cg_iric_write_sol_iface_real
   03/cg_iric_write_sol_jface_integer
   03/cg_iric_write_sol_jface_real
   03/cg_iric_write_sol_particle_pos2d
   03/cg_iric_write_sol_particle_pos3d
   03/cg_iric_write_sol_particle_integer
   03/cg_iric_write_sol_particle_real
   03/cg_iric_write_sol_particlegroup_groupbegin
   03/cg_iric_write_sol_particlegroup_groupend
   03/cg_iric_write_sol_particlegroup_pos2d
   03/cg_iric_write_sol_particlegroup_pos3d
   03/cg_iric_write_sol_particlegroup_integer
   03/cg_iric_write_sol_particlegroup_real
   03/cg_iric_write_sol_polydata_groupbegin
   03/cg_iric_write_sol_polydata_groupend
   03/cg_iric_write_sol_polydata_polygon
   03/cg_iric_write_sol_polydata_polyline
   03/cg_iric_write_sol_polydata_integer
   03/cg_iric_write_sol_polydata_real
   03/iric_check_cancel
   03/iric_write_sol_start
   03/iric_write_sol_end
   03/cg_iric_flush
   03/cg_iric_read_sol_count
   03/cg_iric_read_sol_time
   03/cg_iric_read_sol_iteration
   03/cg_iric_read_sol_baseiterative_integer
   03/cg_iric_read_sol_baseiterative_real
   03/cg_iric_read_sol_baseiterative_string
   03/cg_iric_read_sol_grid2d_coords
   03/cg_iric_read_sol_grid3d_coords
   03/cg_iric_read_sol_node_integer
   03/cg_iric_read_sol_node_real
   03/cg_iric_read_sol_cell_integer
   03/cg_iric_read_sol_cell_real
   03/cg_iric_read_sol_iface_integer
   03/cg_iric_read_sol_iface_real
   03/cg_iric_read_sol_jface_integer
   03/cg_iric_read_sol_jface_real
   03/cg_iric_write_errorcode
   03/cg_iric_close
