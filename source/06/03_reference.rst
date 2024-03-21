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
   03/cg_iRIC_Check_Update
   03/cg_iRIC_Clear_Sol
   03/cg_iRIC_Close
   03/cg_iRIC_Copy_Grid
   03/cg_iRIC_Copy_Grid_WithGridId
   03/cg_iRIC_Open
   03/cg_iRIC_Read_BC_Count
   03/cg_iRIC_Read_BC_Count_WithGridId
   03/cg_iRIC_Read_BC_Functional
   03/cg_iRIC_Read_BC_FunctionalSize
   03/cg_iRIC_Read_BC_FunctionalSize_WithGridId
   03/cg_iRIC_Read_BC_FunctionalWithName
   03/cg_iRIC_Read_BC_FunctionalWithName_RealSingle
   03/cg_iRIC_Read_BC_FunctionalWithName_RealSingle_WithGridId
   03/cg_iRIC_Read_BC_FunctionalWithName_WithGridId
   03/cg_iRIC_Read_BC_Functional_RealSingle
   03/cg_iRIC_Read_BC_Functional_RealSingle_WithGridId
   03/cg_iRIC_Read_BC_Functional_WithGridId
   03/cg_iRIC_Read_BC_Indices
   03/cg_iRIC_Read_BC_IndicesSize
   03/cg_iRIC_Read_BC_IndicesSize_WithGridId
   03/cg_iRIC_Read_BC_Indices_WithGridId
   03/cg_iRIC_Read_BC_Integer
   03/cg_iRIC_Read_BC_Integer_WithGridId
   03/cg_iRIC_Read_BC_Real
   03/cg_iRIC_Read_BC_RealSingle
   03/cg_iRIC_Read_BC_RealSingle_WithGridId
   03/cg_iRIC_Read_BC_Real_WithGridId
   03/cg_iRIC_Read_BC_String
   03/cg_iRIC_Read_BC_StringLen
   03/cg_iRIC_Read_BC_StringLen_WithGridId
   03/cg_iRIC_Read_BC_String_WithGridId
   03/cg_iRIC_Read_Complex_Count
   03/cg_iRIC_Read_Complex_Functional
   03/cg_iRIC_Read_Complex_FunctionalSize
   03/cg_iRIC_Read_Complex_FunctionalWithName
   03/cg_iRIC_Read_Complex_FunctionalWithName_RealSingle
   03/cg_iRIC_Read_Complex_Functional_RealSingle
   03/cg_iRIC_Read_Complex_Integer
   03/cg_iRIC_Read_Complex_Real
   03/cg_iRIC_Read_Complex_RealSingle
   03/cg_iRIC_Read_Complex_String
   03/cg_iRIC_Read_Complex_StringLen
   03/cg_iRIC_Read_Functional
   03/cg_iRIC_Read_FunctionalSize
   03/cg_iRIC_Read_FunctionalWithName
   03/cg_iRIC_Read_FunctionalWithName_RealSingle
   03/cg_iRIC_Read_Functional_RealSingle
   03/cg_iRIC_Read_Geo_Count
   03/cg_iRIC_Read_Geo_Filename
   03/cg_iRIC_Read_Grid2d_CellArea
   03/cg_iRIC_Read_Grid2d_CellNodeCount
   03/cg_iRIC_Read_Grid2d_Close
   03/cg_iRIC_Read_Grid2d_Coords
   03/cg_iRIC_Read_Grid2d_Coords_WithGridId
   03/cg_iRIC_Read_Grid2d_FindCell
   03/cg_iRIC_Read_Grid2d_Interpolate
   03/cg_iRIC_Read_Grid2d_InterpolateWithCell
   03/cg_iRIC_Read_Grid2d_Open
   03/cg_iRIC_Read_Grid2d_Open_WithGridId
   03/cg_iRIC_Read_Grid2d_Str_Size
   03/cg_iRIC_Read_Grid2d_Str_Size_WithGridId
   03/cg_iRIC_Read_Grid_CellCount
   03/cg_iRIC_Read_Grid_CellCount_WithGridId
   03/cg_iRIC_Read_Grid_Complex_Cell
   03/cg_iRIC_Read_Grid_Complex_Cell_WithGridId
   03/cg_iRIC_Read_Grid_Complex_IFace
   03/cg_iRIC_Read_Grid_Complex_IFace_WithGridId
   03/cg_iRIC_Read_Grid_Complex_JFace
   03/cg_iRIC_Read_Grid_Complex_JFace_WithGridId
   03/cg_iRIC_Read_Grid_Complex_Node
   03/cg_iRIC_Read_Grid_Complex_Node_WithGridId
   03/cg_iRIC_Read_Grid_FunctionalDimensionSize
   03/cg_iRIC_Read_Grid_FunctionalDimensionSize_WithGridId
   03/cg_iRIC_Read_Grid_FunctionalDimension_Integer
   03/cg_iRIC_Read_Grid_FunctionalDimension_Integer_WithGridId
   03/cg_iRIC_Read_Grid_FunctionalDimension_Real
   03/cg_iRIC_Read_Grid_FunctionalDimension_Real_WithGridId
   03/cg_iRIC_Read_Grid_FunctionalTime
   03/cg_iRIC_Read_Grid_FunctionalTimeSize
   03/cg_iRIC_Read_Grid_FunctionalTimeSize_WithGridId
   03/cg_iRIC_Read_Grid_FunctionalTime_WithGridId
   03/cg_iRIC_Read_Grid_Functional_Integer_Cell
   03/cg_iRIC_Read_Grid_Functional_Integer_Cell_WithGridId
   03/cg_iRIC_Read_Grid_Functional_Integer_IFace
   03/cg_iRIC_Read_Grid_Functional_Integer_IFace_WithGridId
   03/cg_iRIC_Read_Grid_Functional_Integer_JFace
   03/cg_iRIC_Read_Grid_Functional_Integer_JFace_WithGridId
   03/cg_iRIC_Read_Grid_Functional_Integer_Node
   03/cg_iRIC_Read_Grid_Functional_Integer_Node_WithGridId
   03/cg_iRIC_Read_Grid_Functional_Real_Cell
   03/cg_iRIC_Read_Grid_Functional_Real_Cell_WithGridId
   03/cg_iRIC_Read_Grid_Functional_Real_IFace
   03/cg_iRIC_Read_Grid_Functional_Real_IFace_WithGridId
   03/cg_iRIC_Read_Grid_Functional_Real_JFace
   03/cg_iRIC_Read_Grid_Functional_Real_JFace_WithGridId
   03/cg_iRIC_Read_Grid_Functional_Real_Node
   03/cg_iRIC_Read_Grid_Functional_Real_Node_WithGridId
   03/cg_iRIC_Read_Grid_IFaceCount
   03/cg_iRIC_Read_Grid_IFaceCount_WithGridId
   03/cg_iRIC_Read_Grid_Integer_Cell
   03/cg_iRIC_Read_Grid_Integer_Cell_WithGridId
   03/cg_iRIC_Read_Grid_Integer_IFace
   03/cg_iRIC_Read_Grid_Integer_IFace_WithGridId
   03/cg_iRIC_Read_Grid_Integer_JFace
   03/cg_iRIC_Read_Grid_Integer_JFace_WithGridId
   03/cg_iRIC_Read_Grid_Integer_Node
   03/cg_iRIC_Read_Grid_Integer_Node_WithGridId
   03/cg_iRIC_Read_Grid_JFaceCount
   03/cg_iRIC_Read_Grid_JFaceCount_WithGridId
   03/cg_iRIC_Read_Grid_KFaceCount
   03/cg_iRIC_Read_Grid_KFaceCount_WithGridId
   03/cg_iRIC_Read_Grid_NodeCount
   03/cg_iRIC_Read_Grid_NodeCount_WithGridId
   03/cg_iRIC_Read_Grid_Real_Cell
   03/cg_iRIC_Read_Grid_Real_Cell_WithGridId
   03/cg_iRIC_Read_Grid_Real_IFace
   03/cg_iRIC_Read_Grid_Real_IFace_WithGridId
   03/cg_iRIC_Read_Grid_Real_JFace
   03/cg_iRIC_Read_Grid_Real_JFace_WithGridId
   03/cg_iRIC_Read_Grid_Real_Node
   03/cg_iRIC_Read_Grid_Real_Node_WithGridId
   03/cg_iRIC_Read_Grid_TriangleElements
   03/cg_iRIC_Read_Grid_TriangleElementsSize
   03/cg_iRIC_Read_Grid_TriangleElementsSize_WithGridId
   03/cg_iRIC_Read_Grid_TriangleElements_WithGridId
   03/cg_iRIC_Read_Integer
   03/cg_iRIC_Read_Real
   03/cg_iRIC_Read_RealSingle
   03/cg_iRIC_Read_Sol_BaseIterative_Integer
   03/cg_iRIC_Read_Sol_BaseIterative_Real
   03/cg_iRIC_Read_Sol_BaseIterative_String
   03/cg_iRIC_Read_Sol_BaseIterative_StringLen
   03/cg_iRIC_Read_Sol_Cell_Integer
   03/cg_iRIC_Read_Sol_Cell_Integer_WithGridId
   03/cg_iRIC_Read_Sol_Cell_Real
   03/cg_iRIC_Read_Sol_Cell_Real_WithGridId
   03/cg_iRIC_Read_Sol_Count
   03/cg_iRIC_Read_Sol_Grid2d_Coords
   03/cg_iRIC_Read_Sol_Grid2d_Coords_WithGridId
   03/cg_iRIC_Read_Sol_Grid2d_Open
   03/cg_iRIC_Read_Sol_Grid2d_Open_WithGridId
   03/cg_iRIC_Read_Sol_Grid3d_Coords
   03/cg_iRIC_Read_Sol_Grid3d_Coords_WithGridId
   03/cg_iRIC_Read_Sol_IFace_Integer
   03/cg_iRIC_Read_Sol_IFace_Integer_WithGridId
   03/cg_iRIC_Read_Sol_IFace_Real
   03/cg_iRIC_Read_Sol_IFace_Real_WithGridId
   03/cg_iRIC_Read_Sol_Iteration
   03/cg_iRIC_Read_Sol_JFace_Integer
   03/cg_iRIC_Read_Sol_JFace_Integer_WithGridId
   03/cg_iRIC_Read_Sol_JFace_Real
   03/cg_iRIC_Read_Sol_JFace_Real_WithGridId
   03/cg_iRIC_Read_Sol_KFace_Integer
   03/cg_iRIC_Read_Sol_KFace_Integer_WithGridId
   03/cg_iRIC_Read_Sol_KFace_Real
   03/cg_iRIC_Read_Sol_KFace_Real_WithGridId
   03/cg_iRIC_Read_Sol_Node_Integer
   03/cg_iRIC_Read_Sol_Node_Integer_WithGridId
   03/cg_iRIC_Read_Sol_Node_Real
   03/cg_iRIC_Read_Sol_Node_Real_WithGridId
   03/cg_iRIC_Read_Sol_ParticleGroupImage_Count
   03/cg_iRIC_Read_Sol_ParticleGroupImage_Count_WithGridId
   03/cg_iRIC_Read_Sol_ParticleGroupImage_Pos2d
   03/cg_iRIC_Read_Sol_ParticleGroupImage_Pos2d_WithGridId
   03/cg_iRIC_Read_Sol_ParticleGroup_Count
   03/cg_iRIC_Read_Sol_ParticleGroup_Count_WithGridId
   03/cg_iRIC_Read_Sol_ParticleGroup_Integer
   03/cg_iRIC_Read_Sol_ParticleGroup_Integer_WithGridId
   03/cg_iRIC_Read_Sol_ParticleGroup_Pos2d
   03/cg_iRIC_Read_Sol_ParticleGroup_Pos2d_WithGridId
   03/cg_iRIC_Read_Sol_ParticleGroup_Pos3d
   03/cg_iRIC_Read_Sol_ParticleGroup_Pos3d_WithGridId
   03/cg_iRIC_Read_Sol_ParticleGroup_Real
   03/cg_iRIC_Read_Sol_ParticleGroup_Real_WithGridId
   03/cg_iRIC_Read_Sol_Particle_Count
   03/cg_iRIC_Read_Sol_Particle_Count_WithGridId
   03/cg_iRIC_Read_Sol_Particle_Integer
   03/cg_iRIC_Read_Sol_Particle_Integer_WithGridId
   03/cg_iRIC_Read_Sol_Particle_Pos2d
   03/cg_iRIC_Read_Sol_Particle_Pos2d_WithGridId
   03/cg_iRIC_Read_Sol_Particle_Pos3d
   03/cg_iRIC_Read_Sol_Particle_Pos3d_WithGridId
   03/cg_iRIC_Read_Sol_Particle_Real
   03/cg_iRIC_Read_Sol_Particle_Real_WithGridId
   03/cg_iRIC_Read_Sol_PolyData_CoordinateCount
   03/cg_iRIC_Read_Sol_PolyData_CoordinateCount_WithGridId
   03/cg_iRIC_Read_Sol_PolyData_DataCount
   03/cg_iRIC_Read_Sol_PolyData_DataCount_WithGridId
   03/cg_iRIC_Read_Sol_PolyData_Integer
   03/cg_iRIC_Read_Sol_PolyData_Integer_WithGridId
   03/cg_iRIC_Read_Sol_PolyData_Pos2d
   03/cg_iRIC_Read_Sol_PolyData_Pos2d_WithGridId
   03/cg_iRIC_Read_Sol_PolyData_Real
   03/cg_iRIC_Read_Sol_PolyData_Real_WithGridId
   03/cg_iRIC_Read_Sol_PolyData_Type
   03/cg_iRIC_Read_Sol_PolyData_Type_WithGridId
   03/cg_iRIC_Read_Sol_Time
   03/cg_iRIC_Read_String
   03/cg_iRIC_Read_StringLen
   03/cg_iRIC_Write_BC_Functional
   03/cg_iRIC_Write_BC_FunctionalWithName
   03/cg_iRIC_Write_BC_FunctionalWithName_WithGridId
   03/cg_iRIC_Write_BC_Functional_WithGridId
   03/cg_iRIC_Write_BC_Indices
   03/cg_iRIC_Write_BC_Indices_WithGridId
   03/cg_iRIC_Write_BC_Integer
   03/cg_iRIC_Write_BC_Integer_WithGridId
   03/cg_iRIC_Write_BC_Real
   03/cg_iRIC_Write_BC_Real_WithGridId
   03/cg_iRIC_Write_BC_String
   03/cg_iRIC_Write_BC_String_WithGridId
   03/cg_iRIC_Write_Complex_Functional
   03/cg_iRIC_Write_Complex_FunctionalWithName
   03/cg_iRIC_Write_Complex_Integer
   03/cg_iRIC_Write_Complex_Real
   03/cg_iRIC_Write_Complex_String
   03/cg_iRIC_Write_ErrorCode
   03/cg_iRIC_Write_Functional
   03/cg_iRIC_Write_FunctionalWithName
   03/cg_iRIC_Write_Grid1d_Coords
   03/cg_iRIC_Write_Grid1d_Coords_WithGridId
   03/cg_iRIC_Write_Grid2d_Coords
   03/cg_iRIC_Write_Grid2d_Coords_WithGridId
   03/cg_iRIC_Write_Grid3d_Coords
   03/cg_iRIC_Write_Grid3d_Coords_WithGridId
   03/cg_iRIC_Write_Grid_Complex_Cell
   03/cg_iRIC_Write_Grid_Complex_Cell_WithGridId
   03/cg_iRIC_Write_Grid_Complex_IFace
   03/cg_iRIC_Write_Grid_Complex_IFace_WithGridId
   03/cg_iRIC_Write_Grid_Complex_JFace
   03/cg_iRIC_Write_Grid_Complex_JFace_WithGridId
   03/cg_iRIC_Write_Grid_Complex_Node
   03/cg_iRIC_Write_Grid_Complex_Node_WithGridId
   03/cg_iRIC_Write_Grid_Integer_Cell
   03/cg_iRIC_Write_Grid_Integer_Cell_WithGridId
   03/cg_iRIC_Write_Grid_Integer_IFace
   03/cg_iRIC_Write_Grid_Integer_IFace_WithGridId
   03/cg_iRIC_Write_Grid_Integer_JFace
   03/cg_iRIC_Write_Grid_Integer_JFace_WithGridId
   03/cg_iRIC_Write_Grid_Integer_Node
   03/cg_iRIC_Write_Grid_Integer_Node_WithGridId
   03/cg_iRIC_Write_Grid_Real_Cell
   03/cg_iRIC_Write_Grid_Real_Cell_WithGridId
   03/cg_iRIC_Write_Grid_Real_IFace
   03/cg_iRIC_Write_Grid_Real_IFace_WithGridId
   03/cg_iRIC_Write_Grid_Real_JFace
   03/cg_iRIC_Write_Grid_Real_JFace_WithGridId
   03/cg_iRIC_Write_Grid_Real_Node
   03/cg_iRIC_Write_Grid_Real_Node_WithGridId
   03/cg_iRIC_Write_Integer
   03/cg_iRIC_Write_NamedGrid1d_Coords
   03/cg_iRIC_Write_NamedGrid1d_Coords_WithGridId
   03/cg_iRIC_Write_NamedGrid2d_Coords
   03/cg_iRIC_Write_NamedGrid2d_Coords_WithGridId
   03/cg_iRIC_Write_NamedGrid3d_Coords
   03/cg_iRIC_Write_NamedGrid3d_Coords_WithGridId
   03/cg_iRIC_Write_Real
   03/cg_iRIC_Write_Sol_BaseIterative_Integer
   03/cg_iRIC_Write_Sol_BaseIterative_Real
   03/cg_iRIC_Write_Sol_BaseIterative_String
   03/cg_iRIC_Write_Sol_Cell_Integer
   03/cg_iRIC_Write_Sol_Cell_Integer_WithGridId
   03/cg_iRIC_Write_Sol_Cell_Real
   03/cg_iRIC_Write_Sol_Cell_Real_WithGridId
   03/cg_iRIC_Write_Sol_End
   03/cg_iRIC_Write_Sol_Grid2d_Coords
   03/cg_iRIC_Write_Sol_Grid2d_Coords_WithGridId
   03/cg_iRIC_Write_Sol_Grid3d_Coords
   03/cg_iRIC_Write_Sol_Grid3d_Coords_WithGridId
   03/cg_iRIC_Write_Sol_IFace_Integer
   03/cg_iRIC_Write_Sol_IFace_Integer_WithGridId
   03/cg_iRIC_Write_Sol_IFace_Real
   03/cg_iRIC_Write_Sol_IFace_Real_WithGridId
   03/cg_iRIC_Write_Sol_Iteration
   03/cg_iRIC_Write_Sol_JFace_Integer
   03/cg_iRIC_Write_Sol_JFace_Integer_WithGridId
   03/cg_iRIC_Write_Sol_JFace_Real
   03/cg_iRIC_Write_Sol_JFace_Real_WithGridId
   03/cg_iRIC_Write_Sol_KFace_Integer
   03/cg_iRIC_Write_Sol_KFace_Integer_WithGridId
   03/cg_iRIC_Write_Sol_KFace_Real
   03/cg_iRIC_Write_Sol_KFace_Real_WithGridId
   03/cg_iRIC_Write_Sol_Node_Integer
   03/cg_iRIC_Write_Sol_Node_Integer_WithGridId
   03/cg_iRIC_Write_Sol_Node_Real
   03/cg_iRIC_Write_Sol_Node_Real_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroupImage_GroupBegin
   03/cg_iRIC_Write_Sol_ParticleGroupImage_GroupBegin_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroupImage_GroupEnd
   03/cg_iRIC_Write_Sol_ParticleGroupImage_GroupEnd_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroupImage_Pos2d
   03/cg_iRIC_Write_Sol_ParticleGroupImage_Pos2d_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroup_GroupBegin
   03/cg_iRIC_Write_Sol_ParticleGroup_GroupBegin_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroup_GroupEnd
   03/cg_iRIC_Write_Sol_ParticleGroup_GroupEnd_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroup_Integer
   03/cg_iRIC_Write_Sol_ParticleGroup_Integer_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroup_Pos2d
   03/cg_iRIC_Write_Sol_ParticleGroup_Pos2d_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroup_Pos3d
   03/cg_iRIC_Write_Sol_ParticleGroup_Pos3d_WithGridId
   03/cg_iRIC_Write_Sol_ParticleGroup_Real
   03/cg_iRIC_Write_Sol_ParticleGroup_Real_WithGridId
   03/cg_iRIC_Write_Sol_Particle_Integer
   03/cg_iRIC_Write_Sol_Particle_Integer_WithGridId
   03/cg_iRIC_Write_Sol_Particle_Pos2d
   03/cg_iRIC_Write_Sol_Particle_Pos2d_WithGridId
   03/cg_iRIC_Write_Sol_Particle_Pos3d
   03/cg_iRIC_Write_Sol_Particle_Pos3d_WithGridId
   03/cg_iRIC_Write_Sol_Particle_Real
   03/cg_iRIC_Write_Sol_Particle_Real_WithGridId
   03/cg_iRIC_Write_Sol_PolyData_GroupBegin
   03/cg_iRIC_Write_Sol_PolyData_GroupBegin_WithGridId
   03/cg_iRIC_Write_Sol_PolyData_GroupEnd
   03/cg_iRIC_Write_Sol_PolyData_GroupEnd_WithGridId
   03/cg_iRIC_Write_Sol_PolyData_Integer
   03/cg_iRIC_Write_Sol_PolyData_Integer_WithGridId
   03/cg_iRIC_Write_Sol_PolyData_Polygon
   03/cg_iRIC_Write_Sol_PolyData_Polygon_WithGridId
   03/cg_iRIC_Write_Sol_PolyData_Polyline
   03/cg_iRIC_Write_Sol_PolyData_Polyline_WithGridId
   03/cg_iRIC_Write_Sol_PolyData_Real
   03/cg_iRIC_Write_Sol_PolyData_Real_WithGridId
   03/cg_iRIC_Write_Sol_Start
   03/cg_iRIC_Write_Sol_Time
   03/cg_iRIC_Write_String
   03/iRIC_Check_Cancel
   03/iRIC_Geo_Polygon_Close
   03/iRIC_Geo_Polygon_Open
   03/iRIC_Geo_Polygon_Read_HoleCount
   03/iRIC_Geo_Polygon_Read_HolePointCount
   03/iRIC_Geo_Polygon_Read_HolePoints
   03/iRIC_Geo_Polygon_Read_IntegerValue
   03/iRIC_Geo_Polygon_Read_PointCount
   03/iRIC_Geo_Polygon_Read_Points
   03/iRIC_Geo_Polygon_Read_RealValue
   03/iRIC_Geo_RiverSurvey_Close
   03/iRIC_Geo_RiverSurvey_Open
   03/iRIC_Geo_RiverSurvey_Read_AltitudeCount
   03/iRIC_Geo_RiverSurvey_Read_Altitudes
   03/iRIC_Geo_RiverSurvey_Read_Count
   03/iRIC_Geo_RiverSurvey_Read_Direction
   03/iRIC_Geo_RiverSurvey_Read_FixedPointL
   03/iRIC_Geo_RiverSurvey_Read_FixedPointR
   03/iRIC_Geo_RiverSurvey_Read_LeftShift
   03/iRIC_Geo_RiverSurvey_Read_Name
   03/iRIC_Geo_RiverSurvey_Read_Position
   03/iRIC_Geo_RiverSurvey_Read_RealName
   03/iRIC_Geo_RiverSurvey_Read_WaterSurfaceElevation
   03/iRIC_InitOption
