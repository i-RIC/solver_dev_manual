import re
import os
import pprint


def make_func_info(l):
    print(l)
    p = re.compile(r'([a-z]+) (.+)\((.*)\)')
    m = p.match(l)
    (ret_type, f_name, args_str) = m.groups()
    args = args_str.split(',')
    arg_infos = list()
    for a in args:
        a = a.strip()
        frags = a.split(' ')
        aname = frags.pop()
        atype = ' '.join(frags)
        info = dict(type=atype, name=aname)

        if aname == '':
            continue

        arg_infos.append(info)

    return dict(name=f_name, return_type=ret_type, args=arg_infos)


def load_func_definitions():
    ret = list()

    for fname in os.listdir('D:/iRIC/dev_vc2019_64/iriclib'):
        if not '.h' in fname or not 'iriclib_' in fname:
            continue

        if fname == 'iriclib_wrapper.h':
            continue

        with open(os.path.join('D:/iRIC/dev_vc2019_64/iriclib', fname), 'r', encoding='utf-8') as f:
            for l in f:
                # print(l)
                l = l.strip()
                l = l.replace(';', '')
                if not 'IRICLIBDLL' in l:
                    continue
                if '_WithBaseId' in l:
                    continue
                if '#' in l:
                    continue
                if 'class ' in l:
                    continue

                if 'cg_iRIC_Read_Grid_TriangleElementsSize2' in l:
                    continue
                if 'cg_iRIC_Read_BC_Indices2' in l:
                    continue
                if 'cg_iRIC_Read_BC_IndicesSize2' in l:
                    continue
                if 'FunctionalWithName_String' in l:
                    continue
                if 'cg_iRIC_Read_Grid3d' in l:
                    continue
                if 'cg_iRIC_Clear_BC' in l:
                    continue
                if 'cg_iRIC_Clear_Complex' in l:
                    continue
                if 'cg_iRIC_Combine_Solutions' in l:
                    continue
                if 'cg_iRIC_Write_BC_Indices2' in l:
                    continue

                l = l.replace('IRICLIBDLL ', '')
                info = make_func_info(l)
                ret.append(info)

    return ret


def build_fortran_format(f):
    args = list()
    for a in f['args']:
        args.append(a['name'])

    if f['name'] == 'iRIC_Check_Cancel':
        args.append('canceled')
    else:
        args.append('ier')

    return 'call {0}({1})'.format(f['name'], ', '.join(args))


def build_c_format(f):
    args = list()
    for a in f['args']:
        args.append(a['name'])

    if f['name'] == 'iRIC_Check_Cancel':
        retname = 'canceled'
    else:
        retname = 'ier'

    return '{0} = {1}({2})'.format(retname, f['name'], ', '.join(args))


def build_python_format(f):
    rets = list()
    args = list()

    for a in f['args']:
        if a['type'] != 'const char*' and '*' in a['type']:
            rets.append(a['name'])
        else:
            args.append(a['name'])

    if f['name'] == 'iRIC_Check_Cancel':
        rets.append('canceled')

    if rets:
        return '{0} = {1}({2})'.format(', '.join(rets), f['name'], ', '.join(args))
    else:
        return '{0}({1})'.format(f['name'], ', '.join(args))


def build_func_desc(func):
    fname = func['name']

    print('FNAME', fname)

    # read variables
    m = re.match(r'^cg_iRIC_Read_(BC_|Complex_|)(.+?)(_WithGridId|)$', fname)
    if m:
        (type, value, suffix) = m.groups()
        types = {
            '': 'calculation condition',
            'BC_': 'boundary condition',
            'Complex_': 'complex type grid attribute',
        }
        values = {
            'Integer': 'Reads the value of an integer {}.',
            'Real': 'Reads the value of a double-precision real {}.',
            'RealSingle': 'Reads the value of a single-precision real {}.',
            'String': 'Reads the value of a string {}.',
            'StringLen': 'Reads the length of a string {}.',
            'FunctionalSize': 'Reads the size of a functional {}.',
            'Functional': 'Reads the variable values (X, Y) of functional {}.',
            'Functional_RealSingle': 'Reads the variable values (X, Y) of functional {}, as single-precision real values.',
            'FunctionalWithName': 'Reads the variable values of functional {}. This should be used in case it has multiple values.',
            'FunctionalWithName_RealSingle': 'Reads the variable values of functional {}, as single-precision real values. This should be used in case it has multiple values.',
        }
        if type in types.keys() and value in values.keys():
            t = types[type]
            v = values[value]

            return v.format(t)

    # write variables
    m = re.match(r'^cg_iRIC_Write_(BC_|Complex_|)(.+?)(_WithGridId|)$', fname)
    if m:
        (type, value, suffix) = m.groups()
        types = {
            '': 'calculation condition',
            'BC_': 'boundary condition',
            'Complex_': 'complex type grid attribute',
        }
        values = {
            'Integer': 'Writes the value of an integer {}.',
            'Real': 'Writes the value of a double-precision real {}.',
            'RealSingle': 'Writes the value of a single-precision real {}.',
            'String': 'Writes the value of a string {}.',
            'StringLen': 'Writes the length of a string {}.',
            'FunctionalSize': 'Writes the size of a functional {}.',
            'Functional': 'Writes the variable values (X, Y) of functional {}.',
            'Functional_RealSingle': 'Writes the variable values (X, Y) of functional {}, as single-precision real values.',
            'FunctionalWithName': 'Writes the variable values of functional {}. This should be used in case it has multiple values.',
            'FunctionalWithName_RealSingle': 'Writes the variable values of functional {}, as single-precision real values. This should be used in case it has multiple values.',
        }
        if type in types.keys() and value in values.keys():
            t = types[type]
            v = values[value]

            return v.format(t)

    # read functional dimension size
    if 'cg_iRIC_Read_Grid_FunctionalDimensionSize' in fname or 'cg_iRIC_Read_Grid_FunctionalTimeSize' in fname:
        return "Reads the number of dimensions of grid attribute with time dimension."

    # read functional dimension values
    if 'cg_iRIC_Read_Grid_FunctionalTime' in fname:
        return "Reads the time values of grid attribute with time dimension."

    # read functional grid attribute
    m = re.match(r'^cg_iRIC_Read_Grid_Functional_(.+)_(Node|Cell|IFace|JFace|KFace)(_WithGridId|)$', fname)
    if m:
        (vt, nc, suffix) = m.groups()
        values = {
            'Integer': 'integer',
            'Real': 'double precision real',
        }
        positions = {
            'Node': 'nodes',
            'Cell': 'cells',
            'IFace': 'I-direction cell boudary faces (edges)',
            'JFace': 'J-direction cell boudary faces (edges)',
            'KFace': 'K-direction cell boudary faces (edges)',
        }

        if vt in values.keys() and nc in positions.keys():
            v = values[vt]
            p = positions[nc]

            return "Reads the {} values of grid attribute with time dimension defined at {}.".format(p, v)

    # read / write grid attribute
    m = re.match(r'^cg_iRIC_(Read|Write)_Grid_(.+)_(Node|Cell|IFace|JFace|KFace)(_WithGridId|)$', fname)
    if m:
        (rw, vt, nc, suffix) = m.groups()
        values = {
            'Integer': 'integer',
            'Real': 'double precision real',
            'Complex': 'complex type'
        }
        positions = {
            'Node': 'nodes',
            'Cell': 'cells',
            'IFace': 'I-direction cell boudary faces (edges)',
            'JFace': 'J-direction cell boudary faces (edges)',
            'KFace': 'K-direction cell boudary faces (edges)',
        }
        readwrite = {
            'Read': 'Reads',
            'Write': 'Writes',
        }

        if vt in values.keys() and nc in positions.keys() and rw in readwrite.keys():
            v = values[vt]
            p = positions[nc]
            w = readwrite[rw]

            return "{} the {} grid attribute values defined at {}.".format(p, v, w)

    # read grid
    m = re.match(r'^cg_iRIC_Read_Grid(2d|3d|)_(.+?)(_WithGridId|)$', fname)
    if m:
        (d, value, suffix) = m.groups()
        values = {
            'NodeCount': 'the number of nodes of the grid',
            'CellCount': 'the number of cells of the grid',
            'IFaceCount': 'the number of I-direction cell boudary faces (edges)',
            'JFaceCount': 'the number of J-direction cell boudary faces (edges)',
            'KFaceCount': 'the number of K-direction cell boudary faces (edges)',
            'Str_Size': 'the size of the structured grid (the number of nodes in I-direction and J-direction)',
            'Coords': 'coordinates of grid nodes',
            'TriangleElements': 'IDs of nodes constituting the triangles of the unstructured grid',
        }
        comms = {
            'TriangleElements': 'You should pass an array with size (numcells * 3) for id_arr. The returned values of ids will be the IDs of nodes for each triangles. 1st, 2nd, 3rd values will be the IDs of nodes of the 1st triangle, 4th, 5th, 6th values will be the IDs of nodes of the 2nd triangle, etc.',
        }
        if value in values.keys():
            v = values[value]
            c = ''
            if value in comms.keys():
                c = '\n\n' + comms[value]

            return "Reads {}. {}".format(v, c)

    # write grid
    m = re.match(r'^cg_iRIC_Write_(Named|)Grid(1d|2d|3d)_Coords(_WithGridId|)$', fname)
    if m:
        (_, dim, _) = m.groups()
        dims = {
            '1d': 'one',
            '2d': 'two',
            '3d': 'three',
        }

        return "Write the {} dimensional structured grid.".format(dims[dim])

    # read / write solution
    m = re.match(r'^cg_iRIC_(Read|Write)_Sol_(Node|Cell|IFace|JFace|KFace|Particle|ParticleGroup|PolyData)_(Integer|Real)(_WithGridId|)$', fname)
    if m:
        (rw, nc, vt, suffix) = m.groups()
        values = {
            'Integer': 'integer',
            'Real': 'double precision real',
            'Complex': 'complex type'
        }
        positions = {
            'Node': 'nodes',
            'Cell': 'cells',
            'IFace': 'I-direction cell boudary faces (edges)',
            'JFace': 'J-direction cell boudary faces (edges)',
            'KFace': 'K-direction cell boudary faces (edges)',
            'Particle': 'Particles',
            'ParticleGroup': 'Particles',
            'PolyData': 'polygons or poly lines',
        }
        readwrite = {
            'Read': 'Reads',
            'Write': 'Writes',
        }

        if vt in values.keys() and nc in positions.keys() and rw in readwrite.keys():
            v = values[vt]
            p = positions[nc]
            w = readwrite[rw]

            return "{} the {} calculation result defined at grid {}.".format(w, v, p)

    # read / write grid coords
    m = re.match(r'^cg_iRIC_(Read|Write)_Sol_Grid(2d|3d)_Coords(_WithGridId|)$', fname)
    if m:
        (rw, _, _) = m.groups()
        readwrite = {
            'Read': 'Reads',
            'Write': 'Writes',
        }

        if rw in readwrite.keys():
            w = readwrite[rw]

            return "{} the coordinates of nodes of the calculation result grid.".format(w)

    # read / write particle
    m = re.match(r'^cg_iRIC_(Read|Write)_Sol_(Particle|ParticleGroup|ParticleGroupImage)_Pos(2d|3d)(_WithGridId|)$', fname)
    if m:
        (rw, _, _, _) = m.groups()
        readwrite = {
            'Read': 'Reads',
            'Write': 'Writes',
        }

        if rw in readwrite.keys():
            w = readwrite[rw]

            return "{} the positions of particles.".format(w)

    # read particle count
    if re.match(r'^cg_iRIC_Read_Sol_(Particle|ParticleGroup|ParticleGroupImage)_Count(_WithGridId|)$', fname):
        return "Reads the number of particles."

    # write particle begin
    m = re.match(r'^cg_iRIC_Write_Sol_(ParticleGroup|ParticleGroupImage|PolyData)_GroupBegin(_WithGridId|)$', fname)
    if m:
        (type, _) = m.groups()
        types = {
            'ParticleGroup': 'particles',
            'ParticleGroupImage': 'particles',
            'PolyData': 'polygons or poly lines',
        }

        return "Starts outputting calculation result defined at {}.".format(types[type])

    # write particle end
    m = re.match(r'^cg_iRIC_Write_Sol_(ParticleGroup|ParticleGroupImage|PolyData)_GroupEnd(_WithGridId|)$', fname)
    if m:
        (type, _) = m.groups()
        types = {
            'ParticleGroup': 'particles',
            'ParticleGroupImage': 'particles',
            'PolyData': 'polygons or poly lines',
        }

        return "Finishes outputting calculatioin result defined at {}.".format(types[type])

    # read / write global solution
    m = re.match(r'^cg_iRIC_(Read|Write)_Sol_BaseIterative_(Integer|Real|String)$', fname)
    if m:
        (rw, vt) = m.groups()
        values = {
            'Integer': 'integer',
            'Real': 'double precision real',
            'String': 'complex type'
        }
        readwrite = {
            'Read': 'Reads',
            'Write': 'Writes',
        }

        if vt in values.keys() and rw in readwrite.keys():
            v = values[vt]
            w = readwrite[rw]

            return "{} the {} calculation result defined globally.".format(v, w)

    # read functional dimension data
    m = re.match(r'^cg_iRIC_Read_Grid_FunctionalDimension_(.+?)(_WithGridId|)$', fname)
    if m:
        (vt, suffix) = m.groups()
        values = {
            'Integer': 'integer',
            'Real': 'double precision real',
        }

        if vt in values.keys():
            v = values[vt]

            return "Reads the values of {} dimension for grid attribute with time dimension.".format(v)

    descs = {
        'cg_iRIC_Check_Update': 'Inform the GUI that the solver finished outputting result.',
        'cg_iRIC_Clear_Sol': 'Clears calculation result data.',
        'cg_iRIC_Close': 'Closes the CGNS file.',
        'cg_iRIC_Copy_Grid': 'Copy grid between two CGNS files.',
        'cg_iRIC_Open': 'Opens a CGNS file.',
        'cg_iRIC_Read_BC_Count': 'Reads the number of boundary condition.',
        'cg_iRIC_Read_BC_IndicesSize': 'Reads the number of elements (nodes, cells, or edges) where the boundary.',
        'cg_iRIC_Read_BC_Indices': 'Reads the elements (nodes, cells, or edges) where the boundary condition is defined.',
        'cg_iRIC_Write_BC_Indices': 'Writes the elements (nodes, cells, or edges) where the boundary condition is defined.',
        'cg_iRIC_Read_Complex_Count': 'Reads the number of groups of complex type grid attribute.',
        'cg_iRIC_Read_Geo_Count': 'Reads the number of geographic data.',
        'cg_iRIC_Read_Geo_Filename': 'Reads the file name and data type of geographic data.',
        'cg_iRIC_Read_Grid_TriangleElementsSize': 'Reads the size of array needed to load the IDs of nodes for each triangles in an unstructured grid.',
        'cg_iRIC_Read_Grid2d_CellArea': 'Calculates and returns the area of a cell in the grid.',
        'cg_iRIC_Read_Grid2d_CellNodeCount': 'Reads the number of nodes in the specified cell.',
        'cg_iRIC_Read_Grid2d_Close': 'Closes the grid opened with :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.',
        'cg_iRIC_Read_Grid2d_FindCell': 'Finds and returns the ID of the cell that includes the specified coordinates.',
        'cg_iRIC_Read_Grid2d_Interpolate': 'Returns the information to interpolate the value at the specified coordinates, with the values defined at grid nodes.',
        'cg_iRIC_Read_Grid2d_Open': 'Opens the grid.',
        'cg_iRIC_Read_Sol_BaseIterative_StringLen': 'Reads the length of string calculation result value defined globally.',
        'cg_iRIC_Read_Sol_Grid2d_Open': 'Opens the grid in calculation result. ',
        'cg_iRIC_Read_Sol_Iteration': 'Reads the loop iteration value.',
        'cg_iRIC_Read_Sol_Count': 'Reads the number of calculation result.',
        'cg_iRIC_Read_Sol_PolyData_CoordinateCount': 'Reads the sum of the number of nodes constituting polygons or poly lines',
        'cg_iRIC_Read_Sol_PolyData_DataCount': 'Reads the number of calculation results defined at polygons or poly lines.',
        'cg_iRIC_Read_Sol_PolyData_Pos2d': 'Reads the coordinates of vertices of the calculation result defined at polygons or poly lines.',
        'cg_iRIC_Read_Sol_PolyData_Type': 'Reads the types of calculation results defined at polygons or poly lines.',
        'cg_iRIC_Read_Sol_Time': 'Reads the time value.',
        'cg_iRIC_Write_ErrorCode': 'Writes error code.',
        'cg_iRIC_Write_Sol_PolyData_Polygon': 'Writes the polygon shape for the calculation result defined as polygons.',
        'cg_iRIC_Write_Sol_PolyData_Polyline': 'Writes the poly line shape for the calculation result defined as poly lines.',
        'cg_iRIC_Write_Sol_End': 'Inform the GUI that the solver finished outputting result.',
        'cg_iRIC_Write_Sol_Iteration': 'Writes iteration count.',
        'cg_iRIC_Write_Sol_Start': 'Inform the GUI that the solver started outputting result.',
        'cg_iRIC_Write_Sol_Time': 'Writes time.',
        'iRIC_Check_Cancel': 'Checks whether user canceled solver execution.',
        'iRIC_Geo_Polygon_Close': 'Closes the geographic data file.',
        'iRIC_Geo_Polygon_Open': 'Opens the geographic data file that contains polygon data.',
        'iRIC_Geo_Polygon_Read_HoleCount': 'Reads the number of holes in the polygon.',
        'iRIC_Geo_Polygon_Read_HolePointCount': 'Reads the number of vertices of hole polygon.',
        'iRIC_Geo_Polygon_Read_HolePoints': 'Reads the coordinates of hole polygon vertices.',
        'iRIC_Geo_Polygon_Read_IntegerValue': 'Reads the value of polygon data as integer.',
        'iRIC_Geo_Polygon_Read_HolePoints': 'Reads the coordinates of hole polygon vertices.',
        'iRIC_Geo_Polygon_Read_PointCount': 'Reads the number of polygon vertices.',
        'iRIC_Geo_Polygon_Read_Points': 'Reads the coorinates of polygon vertices.',
        'iRIC_Geo_Polygon_Read_RealValue': 'Reads the value of polygon datas double precision real.',
        'iRIC_Geo_RiverSurvey_Close': 'Closes the geographic data file.',
        'iRIC_Geo_RiverSurvey_Open': 'Opens the geographic data file that contains cross-section data.',
        'iRIC_Geo_RiverSurvey_Read_AltitudeCount': 'Reads the number of altitude data of the cross-section.',
        'iRIC_Geo_RiverSurvey_Read_Altitudes': 'Reads the altitude data of the cross-section.',
        'iRIC_Geo_RiverSurvey_Read_Count': 'Reads the number of the cross-sections in cross-section data.',
        'iRIC_Geo_RiverSurvey_Read_Direction': 'Reads the direction of the cross-section as a normalized vector.',
        'iRIC_Geo_RiverSurvey_Read_FixedPointL': 'Reads the data of left bank extension line of the cross-section.',
        'iRIC_Geo_RiverSurvey_Read_FixedPointR': 'Reads the data of right bank extension line of the cross-section.',
        'iRIC_Geo_RiverSurvey_Read_LeftShift': 'Reads the shift offset value of the cross-section.',
        'iRIC_Geo_RiverSurvey_Read_Name': 'Reads the name of the cross-section as string.',
        'iRIC_Geo_RiverSurvey_Read_Position': 'Reads the coordinates of the cross-section center point.',
        'iRIC_Geo_RiverSurvey_Read_RealName': 'Reads the name of the crosssection as real number.',
        'iRIC_Geo_RiverSurvey_Read_WaterSurfaceElevation': 'Reads the water elevation at the cross-section.',
        'iRIC_InitOption': 'Set up the options for the solver.',
    }

    comments = {
        'cg_iRIC_Read_Grid2d_CellArea': 'The value of g_handle that should be passed to this function, can be obtained by calling :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open` or :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.',
        'cg_iRIC_Read_Grid2d_CellNodeCount': 'The value of g_handle that should be passed to this function, can be obtained by calling :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open` or :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.',
        'cg_iRIC_Read_Grid2d_FindCell': 'The value of g_handle that should be passed to this function, can be obtained by calling :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open` or :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.',
        'cg_iRIC_Read_Grid2d_Interpolate': 'The value of g_handle that should be passed to this function, can be obtained by calling :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open` or :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open`.',
        'cg_iRIC_Read_Grid2d_Open': 'The grid opened with this function can be closed by calling :ref:`sec_ref_cg_iRIC_Read_Grid2d_Close`.',
        'cg_iRIC_Write_Sol_PolyData_Polygon': ':ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin or :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin_WithGridId` should be called before calling this function.',
        'cg_iRIC_Write_Sol_PolyData_Polyline': ':ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin or :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin_WithGridId` should be called before calling this function.',
    }

    for n, d in descs.items():
        if not n in fname:
            continue

        c = ''
        if n in comments.keys():
            c = '\n\n' + comments[n]

        return d + c

    if 'iRICMI_Read_Grid_FunctionalDimensionSize' in fname:
        return "Reads the size of dimension data of functional grid attribute from the CGNS file."
    if fname == 'iRICMI_Calc_Dump' or fname == 'iRICMI_Model_Dump':
        return 'Output calculation results to CGNS file.'
    if fname == 'iRICMI_Calc_Init' or fname == 'iRICMI_Model_Init':
        return 'Initializes iricmi library.'
    if fname == 'iRICMI_Calc_Terminate' or fname == 'iRICMI_Model_Terminate':
        return 'Finalize iricmi library.'
    if fname == 'iRICMI_Model_Sync':
        return 'Synchronize with server. send values to server, and the receive values from server.'
    if fname == 'iRICMI_Calc_Sync_Receive':
        return 'Synchronize and receive values from server.'
    if fname == 'iRICMI_Calc_Sync_Send':
        return 'Synchronize and send values to server.'
    if fname == 'iRICMI_Check_Cancel':
        return 'Check if user requested cancelling of the mode execution.'
    if fname == 'iRICMI_Check_Update':
        return 'Check if user requested flushing of the calculation result output.'
    if fname == 'iricmi_error_print_and_exit':
        return 'If error occured, print error and exit execution.'
    if fname == 'iricmi_error_print':
        return 'If error occured, print error.'
    if 'iRICMI_Read_BC_Count' in fname:
        return 'Reads the number of boundary conditions for the specified type.'
    if fname == 'iRICMI_Read_Complex_Count':
        return 'Reads the number of complex type grid attribute for the specified type.'
    if 'iRICMI_Read_BC_IndicesSize' in fname:
        return 'Reads the size of indices of the boundary condition.'
    if 'iRICMI_Read_Grid_CellCount' in fname:
        return 'Reads the number of cells of the grid.'
    if 'iRICMI_Read_Grid_NodeCount' in fname:
        return 'Reads the number of nodes of the grid.'
    if 'iRICMI_Read_BC_Indices' in fname:
        return 'Reads the indices of the boundary condition.'  # Need more detailed description.

    return '@TODO write description'


def build_func_remarks(func: str) -> str:
    fname = os.path.join('remarks_jp', func)
    if not os.path.exists(fname):
        return ''

    r = 'Remarks\n'
    r += '-------\n'
    r += '\n'
    with open(fname, 'r', encoding='utf-8') as f:
        r += f.read()

    return r


def build_arg_desc(func, arg):
    # print(func['name'], arg['name'])

    fname = func['name']
    aname = arg['name']

    if aname == 'fid':
        return 'File ID'
    if aname == 'fid_from':
        return 'File ID of copy source'
    if aname == 'fid_to':
        return 'File ID of copy target'
    if aname == 'gid':
        return 'Grid ID (Start from 1)'
    if aname == 'isize':
        return 'The number of grid nodes in I-direction'
    if aname == 'jsize':
        return 'The number of grid nodes in J-direction'
    if aname == 'ksize':
        return 'The number of grid nodes in K-direction'
    if aname == 'tsize':
        return 'The number of triangles'
    if aname == 'geoid':
        return 'ID of geographic data (Start from 1)'
    if aname == 'geo_handle':
        return 'Handle of geographic data'
    if aname == 'filename':
        return 'File name'
    if aname == 'csid':
        return 'Cross-Section ID (Start from 1)'
    if aname == 'size':
        if 'FunctionalSize' in fname:
            return 'The number of values for the functional consition'
        if 'IndicesSize' in fname:
            return 'The number of elements (nodes or cells) where the boundary condition is set.'
        if 'ParticleGroupImage' in fname:
            return 'The value of size'
    if aname == 'angle':
        return 'The value of angle'
    if aname == 'holeid':
        return 'Polygon hole ID (Start from 1)'
    if aname == 'count':
        if 'cg_iRIC_Read_Grid_CellCount' in fname:
            return 'The number of cells of the grid'
        if 'cg_iRIC_Read_Grid_NodeCount' in fname:
            return 'The number of nodes of the grid'
        if 'cg_iRIC_Read_Grid_IFaceCount' in fname:
            return 'The number of I-direction cell boudary faces (edges)'
        if 'cg_iRIC_Read_Grid_JFaceCount' in fname:
            return 'The number of J-direction cell boudary faces (edges)'
        if 'cg_iRIC_Read_Grid_KFaceCount' in fname:
            return 'The number of K-direction cell boudary faces (edges)'
    if aname == 'canceled':
        return 'If canceled 1, otherwise 0'
    if aname == 'x_arr':
        if 'Functional' in fname:
            return 'The array of X values'
        else:
            return 'The array of coordinate X values'
    if aname == 'y_arr':
        if 'Functional' in fname:
            return 'The array of Y values'
        else:
            return 'The array of coordinate Y values'
    if aname == 'z_arr':
        return 'The array of coordinate Z values'
    if aname == 'v_arr':
        if 'Functional' in fname:
            return 'The array of the values'
        if re.match(r'^cg_iRIC_(Read|Write)_Sol_(BaseIterative|Node|Cell|IFace|JFace|KFace|Particle|ParticleGroup|PolyData)_(Integer|Real|String).*$', fname):
            return 'The array of calculation result values'
        if re.match(r'^cg_iRIC_(Read|Write)_Grid_.*(Node|Cell|IFace|JFace|KFace).*$', fname):
            return 'The array of grid attribute values'
        if re.match(r'^cg_iRIC_(Read|Write)_Grid_.*Functional(Dimension|Time).*$', fname):
            return 'The values of dimension (time)'
        if '_Sol_PolyData_Type' in fname:
            return 'The array of data types (1: polygon, 2: poly line)'
    if aname == 'size_arr':
        return 'The array of size values'
    if aname == 'angle_arr':
        return 'The array of angle values'
    if aname == 'time_arr':
        return 'The array of time values'
    if aname == 'idx_arr':
        return 'The array of index values'
    if aname == 'id_arr':
        return 'The array of IDs constituting the triangles (start from 1)'
    if aname == 'weights_arr':
        return 'The array of weight values to interpolate the value at the coordinates from the those defined at cell vertices'
    if aname == 'nodeids_arr':
        return 'The array of IDs of grid nodes constituting the cell (start from 1)'
    if aname == 'position_arr':
        return 'Altitude position (less than 0: left bank side, grater than 0: right bank side) values'
    if aname == 'height_arr':
        return 'Altitude height (elevation) values'
    if aname == 'active_arr':
        return 'Altitude data active/inactive (1: active, 0: inactive)'
    if aname == 'x':
        return 'X coordinate value'
    if aname == 'y':
        return 'Y coordinate value'
    if aname == 'dirx':
        return 'X component of direction vector'
    if aname == 'diry':
        return 'Y component of direction vector'
    if aname == 'z':
        return 'Z coordinate value'
    if aname == 'time':
        return 'Time'
    if aname == 'area':
        return 'Area'
    if aname == 'index':
        if fname == 'iRIC_Geo_RiverSurvey_Read_FixedPointL':
            return 'The ID of the altitude data where the left bank extension line starts'
        elif fname == 'iRIC_Geo_RiverSurvey_Read_FixedPointR':
            return 'The ID of the altitude data where the right bank extension line starts'
    if aname == 'set':
        if fname == 'iRIC_Geo_RiverSurvey_Read_FixedPointL':
            return 'If defined, the value is 1, otherwise 0'
        elif fname == 'iRIC_Geo_RiverSurvey_Read_FixedPointR':
            return 'If defined, the value is 1, otherwise 0'
        elif fname == 'iRIC_Geo_RiverSurvey_Read_WaterSurfaceElevation':
            return 'If defined, the value is 1, otherwise 0'
    if aname == 'shift':
        return 'The amount of left shift'
    if aname == 'option':
        return 'The value that corresponds to an option'
    if aname == 'ok':
        if fname == 'cg_iRIC_Read_Grid2d_Interpolate':
            return '1 if a cell is found, 0 if not'
    if aname == 'numPoints':
        return 'The number of vertices in the polygon of polyline'
    if aname == 'value' or aname == 'strvalue':
        if '_Sol_' in fname:
            return 'The value of the calculation result'
        elif '_Filename' in fname:
            return 'File name'
        elif fname == 'iRIC_Geo_RiverSurvey_Read_Name':
            return 'The name of the cross-section'
        else:
            return 'The value of the condition'
    if aname == 'progress':
        return 'Progress (0 to 100)'

    if '_BC_' in fname:
        if aname == 'num':
            return 'Boundary condition number'

    if aname == 'type':
        if '_BC_' in fname:
            return 'The name of the boundary condition'
        if fname == 'cg_iRIC_Read_Geo_Filename':
            return 'Type of geographic data (1: polygon, 2 = cross-section data)'

    if aname == 'num':
        if '_Complex_' in fname:
            return 'Group number'

    if aname == 'groupname':
        if '_Complex_' in fname:
            return 'The name of the complex condition'
        if re.search('_ParticleGroup(Image|)_', fname):
            return 'The name of the particle group'
        if re.search('_PolyData_', fname):
            return 'The name of the polygon (or polyline) group'

    if aname == 'name':
        if 'Geo_' in fname:
            return 'The name of the geographic data'
        if re.match(r'^cg_iRIC_(Read|Write)_(BC_|Complex_|BaseIterative|)(Integer|Real|String|Functional).*$', fname):
            return 'The name of the variable'
        if re.match(r'^cg_iRIC_(Read|Write)_Sol_(BaseIterative|Node|Cell|IFace|JFace|KFace)_(Integer|Real|String).*$', fname):
            return 'The name of the calculation result'
        if re.match(r'^cg_iRIC_(Read|Write)_Sol_(Particle|PolyData)', fname):
            return 'The name of the calculation result'
        if re.match(r'^cg_iRIC_(Read|Write)_Grid_.*(Node|Cell|IFace|JFace|KFace|Functional(Dimension|Time)).*$', fname):
            return 'The name of the grid attribute'
        if 'NamedGrid' in fname:
            return 'The name of the grid'

    if aname == 'paramname':
        if 'Functional' in fname:
            return 'The name of the value'
    if aname == 'step':
        if '_Sol_' in fname:
            return 'The result step number'
    if aname == 'length':
        if 'StringLen' in fname:
            return 'The length of the string'
        if 'Functional' in fname:
            return 'The number of the valus of the condition'
        if 'Indices' in fname:
            return 'THe number of indices'
    if aname == 'dimid':
        if 'Grid_Functional' in fname:
            return 'The ID of time (Start from 1)'
    if aname == 'dimname':
        if 'Grid_Functional' in fname:
            return 'The name of the dimension'
    if aname == 'grid_handle':
        if 'cg_iRIC_Read_Grid2d' in fname or 'cg_iRIC_Read_Sol_Grid2d' in fname:
            return 'The handle of the grid'
    if aname == 'cellId':
        return 'Cell ID (Start from 1)'
    if aname == 'count':
        if 'FunctionalTimeSize' in fname:
            return 'The number of time values'
        if 'FunctionalDimensionSize' in fname:
            return 'The number of dimensions'
        elif 'Particle' in fname:
            return 'The number of particles'
        elif fname == 'cg_iRIC_Read_Sol_Count':
            return 'The number of calculation results'
        elif fname == 'cg_iRIC_Read_Geo_Count':
            return 'The number of geographic data'
        elif fname == 'cg_iRIC_Read_Grid2d_CellNodeCount':
            return 'The number of nodes constituting a cell'
        elif 'cg_iRIC_Read_Sol_PolyData_CoordinateCount' in fname:
            return 'The sum of number of vertices constituting the polygons (or the poly lines)'
        elif 'cg_iRIC_Read_Sol_PolyData_DataCount' in fname:
            return 'The number of polygons (or poly lines)'
        elif 'iRIC_Geo_Polygon_Read_HoleCount' in fname:
            return 'The number of holes'
        elif 'iRIC_Geo_Polygon_Read_HolePointCount' in fname:
            return 'The number of vertices constituting the hole polygon'
        elif 'cg_iRIC_Read_Grid2d_Interpolate' in fname:
            return 'The number of nodes of the cell that contains the specified point'
        elif 'iRIC_Geo_Polygon_Read_PointCount' in fname:
            return 'The number of vertices constituting the polygon'
        else:
            return 'The number of values'
    if aname == 'mode':
        if 'cg_iRIC_Open':
            return 'Mode (IRIC_MODE_READ, IRIC_MODE_WRITE or IRIC_MODE_MODIFY)'
    if aname == 'iteration':
        return 'Iteration count'
    if aname == 'errorcode':
        return 'Error code'

    """
    m = re.match(r'^iRICMI_Read_(BC_|Complex_|)(.+)$', fname)
    if m:
        (t, v) = m.groups()
        if aname == 'type':
            if t == 'BC_':
                return 'The type name of the boundary condition'

        if aname == 'groupname':
            if t == 'Complex_':
                return 'The group name of the complex type grid attribute'

        if aname == 'num':
            if t == 'BC_':
                return 'The id (starts from 1) of the boundary condition'
            elif t == 'Complex_':
                return 'The id (starts from 1) of the complex type grid attribute'

        if aname == 'dimid':
            return 'The id (starts from 1) of the dimension of the grid attribute'

        if aname == 'name':
            if 'Grid' in v:
                return 'The name of the grid attribute'
            elif 'Geo_' in v:
                return 'The name of the geographic data group'
            else:
                return 'The name of the variable'

        if aname == 'val' or aname == 'value':
            if 'Functional' in v:
                return 'The values of the variable'
            else:
                return 'The value of the variable'

        if aname == 'v_arr':
            if 'Grid_FunctionalDimension' in v:
                return 'The values of the dimension'
            elif 'Grid' in v:
                return 'The values of the grid attribute'
            else:
                return 'The values of the variable'

        if aname == 'strvalue':
            if 'Geo_Filename' in v:
                return 'The name of the file'
            else:
                return 'The value of the variable'

        if aname == 'len' or aname == 'length':
            return 'The length of the string variable'

        if aname == 'x':
            if 'Functional' in v:
                return 'The values of the parameter'
            if 'FindCell' in v or 'Interpolate' in v:
                return 'The value of x coordinate'
            else:
                return 'The values of the x coordinates'

        if aname == 'y':
            if 'Functional' in v:
                return 'The values of the value'
            if 'FindCell' in v or 'Interpolate' in v:
                return 'The value of y coordinate'
            else:
                return 'The values of the y coordinates'

        if aname == 'x_arr':
            if 'Functional' in v:
                return 'The values of the parameter'
            else:
                return 'The values of the x coordinates'

        if aname == 'y_arr':
            if 'Functional' in v:
                return 'The values of the value'
            else:
                return 'The values of the y coordinates'

        if aname == 'z_arr':
            return 'The values of the z coordinates'

        if aname == 'size':
            if 'IndicesSize' in fname:
                return 'The number of values of the indices'
            elif 'TriangleElementsSize' in fname:
                return 'The number of triangle cells'
            else:
                return 'The number of values of the functional variable'

        if aname == 'paramname':
            return 'The name of the parameter'

        if aname == 'idx_arr':
            return 'The values of the grid node (or cell or edge) indices'

        if aname == 'dimname':
            return 'The name of the dimension'

    # rin/rout of variables, grid attributes
    m = re.match(r'^iRICMI_(RIn|ROut)_(BC_|Complex_|)(.+)$', fname)
    if m:
        (io, t, v) = m.groups()
        if io == 'RIn':
            op = 'receive'
        else:
            op = 'send'

        if aname == 'type':
            if t == 'BC_':
                return 'The type name of the boundary condition'

        if aname == 'groupname':
            if t == 'Complex_':
                return 'The group name of the complex type grid attribute'

        if aname == 'num':
            if t == 'BC_':
                return 'The id (starts from 1) of the boundary condition'
            elif t == 'Complex_':
                return 'The id (starts from 1) of the complex type grid attribute'

        if aname == 'name':
            if 'grid2d' in v:
                return 'The name of the grid attribute'
            else:
                return 'The name of the variable'

        if aname == 'val':
            return 'The variable to register the memory address, to {0} value'.format(op)

        if aname == 'vals':
            return 'The variable to register the memory address, to {0} values'.format(op)

        if aname == 'x_arr':
            return 'The variable to register the memory address for x coordinates, to {0} value'.format(op)

        if aname == 'y_arr':
            return 'The variable to register the memory address for x coordinates, to {0} value'.format(op)

        if aname == 'z_arr':
            return 'The variable to register the memory address for x coordinates, to {0} value'.format(op)

        if aname == 'v_arr':
            return 'The variable to register the memory address, to {0} values'.format(op)

    if 'Write' in fname and 'Coords' in fname:
        if aname == 'name':
            return 'The name of the grid'

        if aname == 'x_arr':
            return 'The values of the x coordinates'

        if aname == 'y_arr':
            return 'The values of the y coordinates'

        if aname == 'z_arr':
            return 'The values of the z coordinates'


    if aname == 'groupname':
        return 'The group name of the complex type grid attribute'
    if aname == 't':
        return 'The variable to register the memory address, to {0} value of time'.format(op)
    if aname == 'interval':
        return 'The variable to register the memory address, to {0} value of interval'.format(op)
    """

    """
    # read grid
    m = re.match(r'^iricmi_read_grid(2d|)_(.+)$', fname)
    if m:
        (d, value) = m.groups()
        values = {
            'node_count': 'number of nodes of the grid',
            'cell_count': 'number of cells of the grid',
            'str_size': 'size of a structured grid (the number of nodes in I direction and J direction)',
            'unstr_size': 'size of a unstructured grid (the number of nodes)',
            'unstr_cellsize': 'number of cells of a unstructured grid',
            'unstr_cells': 'cells of a unstructured grid',
            'coords': 'values of x and y coordinates of the grid',
        }
        comms = {
            'unstr_cells': 'Currently iRIC supports only unstructured grids with triangles. The returned values are the ids of nodes, that consists the cells.',
        }
        if value in values.keys():
            v = values[value]
            c = ''
            if value in comms.keys():
                c = '\n\n' + comms[value]

            return "Reads the {0} from the CGNS file.{1}".format(v, c)
    """

    return '@TODO write description'


def build_arg_type_fortran(func, arg):
    if 'char' in arg['type']:
        return 'character(*)'
    elif 'int' in arg['type']:
        if '_arr' in arg['name']:
            return 'integer, dimension(:)'
        else:
            return 'integer'
    elif 'double' in arg['type']:
        if '_arr' in arg['name']:
            return 'double precision, dimension(:)'
        else:
            return 'double precision'
    elif 'float' in arg['type']:
        if '_arr' in arg['name']:
            return 'real, dimension(:)'
        else:
            return 'real'

    return '@todo implement this'


def build_arg_type_c(func, arg):
    return arg['type']


def build_arg_type_python(func, arg):
    if '_arr' in arg['name']:
        return 'numpy.array'
    if 'char' in arg['type']:
        return 'str'
    elif 'int' in arg['type']:
        return 'int'
    elif 'double' in arg['type']:
        return 'float'
    elif 'float' in arg['type']:
        return 'float'

    return '@todo implement this'


funcs = sorted(load_func_definitions(), key=lambda d: d['name'])
for f in funcs:
    lines = list()
    lines.append('.. _sec_ref_' + f['name'] + ':')
    lines.append('')
    lines.append(f['name'])
    lines.append(''.join(['='] * len(f['name'])))
    lines.append('')
    lines.append(build_func_desc(f))
    lines.append('')
    lines.append('Format (FORTRAN)')
    lines.append('-----------------')
    lines.append('')
    lines.append('.. code-block:: fortran')
    lines.append('')
    lines.append('   ' + build_fortran_format(f))
    lines.append('')
    lines.append('Format (C/C++)')
    lines.append('-----------------')
    lines.append('')
    lines.append('.. code-block:: c')
    lines.append('')
    lines.append('   ' + build_c_format(f))
    lines.append('')
    lines.append('Format (Python)')
    lines.append('-----------------')
    lines.append('')
    if '_RealSingle' in f['name']:
        lines.append('Not Defined for Python')
    else:
        lines.append('.. code-block:: python')
        lines.append('')
        lines.append('   ' + build_python_format(f))
    lines.append('')
    lines.append('Arguments and returned value')
    lines.append('-------------------------------')
    lines.append('')

    for a in f['args']:
        lines.append(a['name'])
        lines.append(''.join(['~'] * len(a['name'])))
        lines.append('')
        lines.append('.. list-table:: Description of ' + a['name'])
        lines.append('   :header-rows: 1')
        lines.append('')
        lines.append('   * - Item')
        lines.append('     - Value')

        lines.append('   * - Name')
        lines.append('     - {0}'.format(a['name']))

        lines.append('   * - Input/Output')
        io = 'Input'
        if a['type'] != 'const char*' and '*' in a['type']:
            io = 'Output'
        lines.append('     - {0}'.format(io))
        lines.append('')

        lines.append('   * - Description')
        lines.append('     - {0}'.format(build_arg_desc(f, a)))

        lines.append('   * - Data type (FORTRAN)')
        lines.append('     - {0}'.format(build_arg_type_fortran(f, a)))
        lines.append('   * - Data type (C/C++)')
        lines.append('     - {0}'.format(build_arg_type_c(f, a)))

        if not '_RealSingle' in f['name']:
            lines.append('   * - Data type (Python)')
            lines.append('     - {0}'.format(build_arg_type_python(f, a)))
        lines.append('')

    if f['return_type'] == 'int':
        rname = 'ier'
        rdesc = 'Error code. 0 means success, other values mean error.'
        python_type = '(Not defined)'
        if f['name'] == 'iRIC_Check_Cancel':
            rname = 'canceled'
            rdesc = 'If canceled 1 is returned, if not, 0 is returned.'
            python_type = 'int'

        lines.append(rname)
        lines.append(''.join(['~'] * len(rname)))
        lines.append('')

        lines.append('.. list-table:: Description of ' + rname)
        lines.append('   :header-rows: 1')
        lines.append('')
        lines.append('   * - Item')
        lines.append('     - Value')

        lines.append('   * - Name')
        lines.append('     - ' + rname)

        lines.append('   * - Input/Output')
        lines.append('     - Output')
        lines.append('')

        lines.append('   * - Description')
        lines.append('     - ' + rdesc)

        lines.append('   * - Data type (FORTRAN)')
        lines.append('     - integer')
        lines.append('   * - Data type (C/C++)')
        lines.append('     - int')
        lines.append('   * - Data type (Python)')
        lines.append('     - ' + python_type)
        lines.append('')

    if len(f['args']) == 0 and f['return_type'] != 'int':
        lines.append('No argument is defined.')
    lines.append('')

    r = build_func_remarks(f['name'])
    if r != '':
        lines.append(r)

    content = '\n'.join(lines)
    with open('03/{0}.rst'.format(f['name']), 'w', encoding='utf-8') as file:
        file.write(content)


with open('ref.txt', 'w') as f:
    for func in funcs:
        f.write('03/' + func['name'] + '\n')
