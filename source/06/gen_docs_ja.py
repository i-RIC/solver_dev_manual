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
            '': '計算条件',
            'BC_': '境界条件',
            'Complex_': '複合型格子属性',
        }
        values = {
            'Integer': '整数型の{}の値を読み込む。',
            'Real': '倍精度実数型の{}の値を読み込む。',
            'RealSingle': '単精度実数型の{}の値を読み込む。',
            'String': '文字列型の{}の値を読み込む。',
            'StringLen': '文字列型の{}の長さを読み込む。',
            'FunctionalSize': '関数型の{}の変数のサイズを読み込む。',
            'Functional': '倍精度関数型の{}の変数の値 (X, Y) を読み込む。',
            'Functional_RealSingle': '単精度関数型の{}の変数の値 (X, Y) を読み込む。',
            'FunctionalWithName': '倍精度関数型の{}の変数の値を読み込む。変数が1つ、値が複数の関数型の読み込みに利用する。',
            'FunctionalWithName_RealSingle': '単精度関数型の{}の変数の値を読み込む。変数が1つ、値が複数の関数型の読み込みに利用する。',
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
            '': '計算条件',
            'BC_': '境界条件',
            'Complex_': '複合型格子属性',
        }
        values = {
            'Integer': '整数型の{}の値を書き込む。',
            'Real': '倍精度実数型の{}の値を書き込む。',
            'RealSingle': '単精度実数型の{}の値を書き込む。',
            'String': '文字列型の{}の値を書き込む。',
            'StringLen': '文字列型の{}の長さを書き込む。',
            'FunctionalSize': '関数型の{}の変数のサイズを書き込む。',
            'Functional': '倍精度関数型の{}の変数の値 (X, Y) を書き込む。',
            'Functional_RealSingle': '単精度関数型の{}の変数の値 (X, Y) を書き込む。',
            'FunctionalWithName': '倍精度関数型の{}の変数の値を書き込む。変数が1つ、値が複数の関数型の読み込みに利用する。',
            'FunctionalWithName_RealSingle': '単精度関数型の{}の変数の値を書き込む。変数が1つ、値が複数の関数型の読み込みに利用する。',
        }
        if type in types.keys() and value in values.keys():
            t = types[type]
            v = values[value]

            return v.format(t)

    # read functional dimension size
    if 'cg_iRIC_Read_Grid_FunctionalDimensionSize' in fname or 'cg_iRIC_Read_Grid_FunctionalTimeSize' in fname:
        return "次元「時刻」を持つ格子の属性の次元の数を読み込む。"

    # read functional dimension values
    if 'cg_iRIC_Read_Grid_FunctionalTime' in fname:
        return "次元「時刻」を持つ格子の属性の時刻を読み込む。"

    # read functional grid attribute
    m = re.match(r'^cg_iRIC_Read_Grid_Functional_(.+)_(Node|Cell|IFace|JFace|KFace)(_WithGridId|)$', fname)
    if m:
        (vt, nc, suffix) = m.groups()
        values = {
            'Integer': '整数型',
            'Real': '倍精度実数型',
        }
        positions = {
            'Node': '格子点',
            'Cell': 'セル',
            'IFace': 'I方向のセル境界面 (エッジ) ',
            'JFace': 'J方向のセル境界面 (エッジ) ',
            'KFace': 'K方向のセル境界面 (エッジ) ',
        }

        if vt in values.keys() and nc in positions.keys():
            v = values[vt]
            p = positions[nc]

            return "次元「時刻」を持つ、格子の{}で定義された{}の属性を読み込む。".format(p, v)

    # read / write grid attribute
    m = re.match(r'^cg_iRIC_(Read|Write)_Grid_(.+)_(Node|Cell|IFace|JFace|KFace)(_WithGridId|)$', fname)
    if m:
        (rw, vt, nc, suffix) = m.groups()
        values = {
            'Integer': '整数型',
            'Real': '倍精度実数型',
            'Complex': '複合型'
        }
        positions = {
            'Node': '格子点',
            'Cell': 'セル',
            'IFace': 'I方向のセル境界面 (エッジ) ',
            'JFace': 'J方向のセル境界面 (エッジ) ',
            'KFace': 'K方向のセル境界面 (エッジ) ',
        }
        readwrite = {
            'Read': '読み込む',
            'Write': '書き込む',
        }

        if vt in values.keys() and nc in positions.keys() and rw in readwrite.keys():
            v = values[vt]
            p = positions[nc]
            w = readwrite[rw]

            return "格子の{}で定義された{}の属性を{}。".format(p, v, w)

    # read grid
    m = re.match(r'^cg_iRIC_Read_Grid(2d|3d|)_(.+?)(_WithGridId|)$', fname)
    if m:
        (d, value, suffix) = m.groups()
        values = {
            'NodeCount': '格子の格子点の数',
            'CellCount': '格子のセルの数',
            'IFaceCount': '格子のI方向のセル境界面 (エッジ) の数',
            'JFaceCount': '格子のJ方向のセル境界面 (エッジ) の数',
            'KFaceCount': '格子のK方向のセル境界面 (エッジ) の数',
            'Str_Size': '構造格子のサイズ (格子のI方向とJ方向の格子点数)',
            'Coords': '格子の格子点の座標',
            'TriangleElements': '非構造格子の三角形を構成する頂点IDの配列',
        }
        comms = {
            'TriangleElements':
                'id_arr に、セルの数 x 3 のサイズの配列を渡すと、 1, 2, 3 番目, 4, 5, 6 番目, ... にそれぞれ 1番目, 2番目の三角形を構成する頂点の ID が返される。\n\n' +
                '配列 id_arr を作成するために、先に cg_iRIC_Read_CellCount で三角形の数を調べる。',
        }
        if value in values.keys():
            v = values[value]
            c = ''
            if value in comms.keys():
                c = '\n\n' + comms[value]

            return "{}を読み込む。{}".format(v, c)

    # write grid
    m = re.match(r'^cg_iRIC_Write_(Named|)Grid(1d|2d|3d)_Coords(_WithGridId|)$', fname)
    if m:
        (_, dim, _) = m.groups()
        dims = {
            '1d': '1',
            '2d': '2',
            '3d': '3',
        }

        return "{}次元構造格子を出力する。".format(dims[dim])

    # read / write solution
    m = re.match(r'^cg_iRIC_(Read|Write)_Sol_(Node|Cell|IFace|JFace|KFace|Particle|ParticleGroup|PolyData)_(Integer|Real)(_WithGridId|)$', fname)
    if m:
        (rw, nc, vt, suffix) = m.groups()
        values = {
            'Integer': '整数型',
            'Real': '倍精度実数型',
            'Complex': '複合型'
        }
        positions = {
            'Node': '格子点',
            'Cell': 'セル',
            'IFace': 'I方向のセル境界面 (エッジ) ',
            'JFace': 'J方向のセル境界面 (エッジ) ',
            'KFace': 'K方向のセル境界面 (エッジ) ',
            'Particle': 'パーティクル',
            'ParticleGroup': 'パーティクル',
            'PolyData': 'ポリゴンもしくは折れ線',
        }
        readwrite = {
            'Read': '読み込む',
            'Write': '書き込む',
        }

        if vt in values.keys() and nc in positions.keys() and rw in readwrite.keys():
            v = values[vt]
            p = positions[nc]
            w = readwrite[rw]

            return "格子の{}で定義された{}の計算結果を{}。".format(p, v, w)

    # read / write grid coords
    m = re.match(r'^cg_iRIC_(Read|Write)_Sol_Grid(2d|3d)_Coords(_WithGridId|)$', fname)
    if m:
        (rw, _, _) = m.groups()
        readwrite = {
            'Read': '読み込む',
            'Write': '書き込む',
        }

        if rw in readwrite.keys():
            w = readwrite[rw]

            return "計算結果の格子の格子点座標を{}。".format(w)

    # read / write particle
    m = re.match(r'^cg_iRIC_(Read|Write)_Sol_(Particle|ParticleGroup|ParticleGroupImage)_Pos(2d|3d)(_WithGridId|)$', fname)
    if m:
        (rw, _, _, _) = m.groups()
        readwrite = {
            'Read': '読み込む',
            'Write': '書き込む',
        }

        if rw in readwrite.keys():
            w = readwrite[rw]

            return "パーティクルの位置を{}。".format(w)

    # read particle count
    if re.match(r'^cg_iRIC_Read_Sol_(Particle|ParticleGroup|ParticleGroupImage)_Count(_WithGridId|)$', fname):
        return "パーティクルの数を読み込む。"

    # write particle begin
    m = re.match(r'^cg_iRIC_Write_Sol_(ParticleGroup|ParticleGroupImage|PolyData)_GroupBegin(_WithGridId|)$', fname)
    if m:
        (type, _) = m.groups()
        types = {
            'ParticleGroup': 'パーティクル',
            'ParticleGroupImage': 'パーティクル',
            'PolyData': 'ポリゴンもしくは折れ線',
        }

        return "{}で定義された計算結果の出力を開始する。".format(types[type])

    # write particle end
    m = re.match(r'^cg_iRIC_Write_Sol_(ParticleGroup|ParticleGroupImage|PolyData)_GroupEnd(_WithGridId|)$', fname)
    if m:
        (type, _) = m.groups()
        types = {
            'ParticleGroup': 'パーティクル',
            'ParticleGroupImage': 'パーティクル',
            'PolyData': 'ポリゴンもしくは折れ線',
        }

        return "{}で定義された計算結果の出力を終了する。".format(types[type])

    # read / write global solution
    m = re.match(r'^cg_iRIC_(Read|Write)_Sol_BaseIterative_(Integer|Real|String)$', fname)
    if m:
        (rw, vt) = m.groups()
        values = {
            'Integer': '整数型',
            'Real': '倍精度実数型',
            'String': '文字列型'
        }
        readwrite = {
            'Read': '読み込む',
            'Write': '書き込む',
        }

        if vt in values.keys() and rw in readwrite.keys():
            v = values[vt]
            w = readwrite[rw]

            return "グローバルに定義された{}の計算結果を{}。".format(v, w)

    # read functional dimension data
    m = re.match(r'^cg_iRIC_Read_Grid_FunctionalDimension_(.+?)(_WithGridId|)$', fname)
    if m:
        (vt, suffix) = m.groups()
        values = {
            'Integer': '整数型',
            'Real': '倍精度実数型',
        }

        if vt in values.keys():
            v = values[vt]

            return "次元「時刻」を持つ格子の{}の次元の値を読み込む。".format(v)

    descs = {
        'cg_iRIC_Check_Update': 'ユーザーが再読み込みの要求をしたか確認し、要求していた場合は計算結果を出力する。',
        'cg_iRIC_Clear_Sol': '計算結果を削除する。',
        'cg_iRIC_Close': 'CGNS ファイルを閉じる。',
        'cg_iRIC_Copy_Grid': 'CGNSファイルの間で格子をコピーする。',
        'cg_iRIC_Open': 'CGNS ファイルを開く。',
        'cg_iRIC_Read_BC_Count': '境界条件の数を読み込む。',
        'cg_iRIC_Read_BC_IndicesSize': '境界条件が設定された要素（格子点・セル・エッジ）の数を読み込む。',
        'cg_iRIC_Read_BC_Indices': '境界条件が設定された要素（格子点・セル・エッジ）のインデックスのリストを読み込む。',
        'cg_iRIC_Write_BC_Indices': '境界条件が設定された要素（格子点・セル・エッジ）のインデックスのリストを書き込む。',
        'cg_iRIC_Read_Complex_Count': '複合型格子属性のグループの数を読み込む。',
        'cg_iRIC_Read_Geo_Count': '地理情報の数を読み込む。',
        'cg_iRIC_Read_Geo_Filename': '地理情報のファイル名と種類を読み込む。',
        'cg_iRIC_Read_Grid_TriangleElementsSize': '非構造格子の三角形を構成する頂点IDの配列に必要なサイズを読み込む。',
        'cg_iRIC_Read_Grid2d_CellArea': '格子のセルの面積を計算して返す。',
        'cg_iRIC_Read_Grid2d_CellNodeCount': '指定したセルを構成する頂点の数を返す。',
        'cg_iRIC_Read_Grid2d_Close': ':ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open` で開いた格子を閉じる。',
        'cg_iRIC_Read_Grid2d_FindCell': '指定した座標を含むセルのIDを返す。',
        'cg_iRIC_Read_Grid2d_Interpolate': '指定した位置での値を、格子での値を使って補間して計算するための情報を返す。',
        'cg_iRIC_Read_Grid2d_Open': '格子を開く。',
        'cg_iRIC_Read_Sol_BaseIterative_StringLen': 'グローバルに定義された文字列型の計算結果の文字列の長さを読み込む。',
        'cg_iRIC_Read_Sol_Grid2d_Open': '計算結果の格子を開く。',
        'cg_iRIC_Read_Sol_Iteration': '計算結果のループ回数の値を読み込む。',
        'cg_iRIC_Read_Sol_Count': '計算結果の数を読み込む。',
        'cg_iRIC_Read_Sol_PolyData_CoordinateCount': 'ポリゴンもしくは折れ線で定義された計算結果の頂点数の合計を読み込む。',
        'cg_iRIC_Read_Sol_PolyData_DataCount': 'ポリゴンもしくは折れ線で定義された計算結果の数を読み込む。',
        'cg_iRIC_Read_Sol_PolyData_Pos2d': 'ポリゴンもしくは折れ線で定義された計算結果の頂点の座標を読み込む。',
        'cg_iRIC_Read_Sol_PolyData_Type': 'ポリゴンもしくは折れ線で定義された計算結果の種類を読み込む。',
        'cg_iRIC_Read_Sol_Time': '計算結果の時刻の値を読み込む。',
        'cg_iRIC_Write_ErrorCode': 'エラーコードを書き込む。',
        'cg_iRIC_Write_Sol_PolyData_Polygon': '計算結果としてポリゴンの形状を出力する',
        'cg_iRIC_Write_Sol_PolyData_Polyline': '計算結果として折れ線の形状を出力する',
        'cg_iRIC_Write_Sol_End': '計算結果の出力終了をGUIに通知する。',
        'cg_iRIC_Write_Sol_Iteration': 'ループ回数を書き込む。',
        'cg_iRIC_Write_Sol_Start': '計算結果の出力開始をGUIに通知する。',
        'cg_iRIC_Write_Sol_Time': '時刻を書き込む。',
        'iRIC_Check_Cancel': 'ユーザがソルバの実行をキャンセルしたか確認する。',
        'iRIC_Geo_Polygon_Close': 'ポリゴンファイルを閉じる。',
        'iRIC_Geo_Polygon_Open': 'ポリゴンファイルを開く。',
        'iRIC_Geo_Polygon_Read_HoleCount': 'ポリゴンに開いた穴の数を読み込む。',
        'iRIC_Geo_Polygon_Read_HolePointCount': 'ポリゴンの穴の頂点の数を読み込む。',
        'iRIC_Geo_Polygon_Read_HolePoints': 'ポリゴンの穴の頂点の座標を読み込む。',
        'iRIC_Geo_Polygon_Read_IntegerValue': 'ポリゴンの値を整数で読み込む。',
        'iRIC_Geo_Polygon_Read_HolePoints': 'ポリゴンの穴の頂点の座標を読み込む。',
        'iRIC_Geo_Polygon_Read_PointCount': 'ポリゴンの頂点の数を読み込む。',
        'iRIC_Geo_Polygon_Read_Points': 'ポリゴンの頂点の座標を読み込む。',
        'iRIC_Geo_Polygon_Read_RealValue': 'ポリゴンの値を倍精度実数で読み込む。',
        'iRIC_Geo_RiverSurvey_Close': '横断測量データファイルを閉じる。',
        'iRIC_Geo_RiverSurvey_Open': '横断測量データファイルを開く。',
        'iRIC_Geo_RiverSurvey_Read_AltitudeCount': '横断線の標高データの数を読み込む。',
        'iRIC_Geo_RiverSurvey_Read_Altitudes': '横断線の横断形状を読み込む。',
        'iRIC_Geo_RiverSurvey_Read_Count': '横断線の数を読み込む。',
        'iRIC_Geo_RiverSurvey_Read_Direction': '横断線の向きを読み込む。',
        'iRIC_Geo_RiverSurvey_Read_FixedPointL': '横断線の左岸延長線のデータを読み込む。',
        'iRIC_Geo_RiverSurvey_Read_FixedPointR': '横断線の右岸延長線のデータを読み込む。',
        'iRIC_Geo_RiverSurvey_Read_LeftShift': '横断線の標高データのシフト量を読み込む。',
        'iRIC_Geo_RiverSurvey_Read_Name': '横断線の名前を文字列として読み込む。',
        'iRIC_Geo_RiverSurvey_Read_Position': '横断線の中心点の座標を読み込む。',
        'iRIC_Geo_RiverSurvey_Read_RealName': '横断線の名前を実数値として読み込む。',
        'iRIC_Geo_RiverSurvey_Read_WaterSurfaceElevation': '横断線での水面標高を読み込む。',
        'iRIC_InitOption': 'ソルバーのオプションを指定する。',
    }

    comments = {
        'cg_iRIC_Read_Grid2d_CellArea': 'この関数に渡す g_handle は :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open` を使って取得する。',
        'cg_iRIC_Read_Grid2d_CellNodeCount': 'この関数に渡す g_handle は :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open` を使って取得する。',
        'cg_iRIC_Read_Grid2d_FindCell': 'この関数に渡す g_handle は :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open` を使って取得する。',
        'cg_iRIC_Read_Grid2d_Interpolate': 'この関数に渡す g_handle は :ref:`sec_ref_cg_iRIC_Read_Grid2d_Open`, :ref:`sec_ref_cg_iRIC_Read_Sol_Grid2d_Open` を使って取得する。',
        'cg_iRIC_Read_Grid2d_Open': 'この関数で開いた格子は、 :ref:`sec_ref_cg_iRIC_Read_Grid2d_Close` を使用して閉じる。',
        'cg_iRIC_Write_Sol_PolyData_Polygon': 'この関数を呼び出す前に :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin`, :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin_WithGridId` を呼び出す必要がある。',
        'cg_iRIC_Write_Sol_PolyData_Polyline': 'この関数を呼び出す前に :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin`, :ref:`sec_ref_cg_iRIC_Write_Sol_PolyData_GroupBegin_WithGridId` を呼び出す必要がある。',
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

    r = '備考\n'
    r += '----\n'
    r += '\n'
    with open(fname, 'r', encoding='utf-8') as f:
        r += f.read()

    return r


def build_arg_desc(func, arg):
    # print(func['name'], arg['name'])

    fname = func['name']
    aname = arg['name']

    if aname == 'fid':
        return 'ファイルID'
    if aname == 'fid_from':
        return 'コピー元ファイルID'
    if aname == 'fid_to':
        return 'コピー先ファイルID'
    if aname == 'gid':
        return '格子ID (1から開始)'
    if aname == 'isize':
        return 'I方向の格子点数'
    if aname == 'jsize':
        return 'J方向の格子点数'
    if aname == 'ksize':
        return 'K方向の格子点数'
    if aname == 'tsize':
        return '三角形の数'
    if aname == 'geoid':
        return '地理情報データの番号 (1から開始)'
    if aname == 'geo_handle':
        return '地理情報のハンドル'
    if aname == 'filename':
        return 'ファイル名'
    if aname == 'csid':
        return '横断線ID (1から開始)'
    if aname == 'size':
        if 'FunctionalSize' in fname:
            return '関数型条件の値の数'
        if 'IndicesSize' in fname:
            return 'インデックスの値の数'
        if 'ParticleGroupImage' in fname:
            return 'サイズの値'
    if aname == 'angle':
        return '角度'
    if aname == 'holeid':
        return 'ポリゴンの穴のID (1から開始)'
    if aname == 'count':
        if 'cg_iRIC_Read_Grid_CellCount' in fname:
            return '格子のセルの数'
        if 'cg_iRIC_Read_Grid_NodeCount' in fname:
            return '格子の格子点の数'
        if 'cg_iRIC_Read_Grid_IFaceCount' in fname:
            return 'I方向のセル境界面 (エッジ) の数'
        if 'cg_iRIC_Read_Grid_JFaceCount' in fname:
            return 'J方向のセル境界面 (エッジ) の数'
        if 'cg_iRIC_Read_Grid_KFaceCount' in fname:
            return 'K方向のセル境界面 (エッジ) の数'
    if aname == 'canceled':
        return 'キャンセルされていたら1, そうでなければ0'
    if aname == 'x_arr':
        if 'Functional' in fname:
            return 'Xの値の配列'
        else:
            return 'X座標の配列'
    if aname == 'y_arr':
        if 'Functional' in fname:
            return 'Yの値の配列'
        else:
            return 'Y座標の配列'
    if aname == 'z_arr':
        return 'Z座標の配列'
    if aname == 'v_arr':
        if 'Functional' in fname:
            return '条件の値の配列'
        if re.match(r'^cg_iRIC_(Read|Write)_Sol_(BaseIterative|Node|Cell|IFace|JFace|KFace|Particle|ParticleGroup|PolyData)_(Integer|Real|String).*$', fname):
            return '計算結果の値の配列'
        if re.match(r'^cg_iRIC_(Read|Write)_Grid_.*(Node|Cell|IFace|JFace|KFace).*$', fname):
            return '格子属性の値の配列'
        if re.match(r'^cg_iRIC_(Read|Write)_Grid_.*Functional(Dimension|Time).*$', fname):
            return '格子属性の定義された時刻の値の配列'
        if '_Sol_PolyData_Type' in fname:
            return '種類の値の配列 (1 = ポリゴン, 2 = 折れ線)'
    if aname == 'size_arr':
        return 'サイズの値の配列'
    if aname == 'angle_arr':
        return '角度の値の配列'
    if aname == 'time_arr':
        return '時刻の値の配列'
    if aname == 'idx_arr':
        return 'インデックスの値の配列'
    if aname == 'id_arr':
        return '三角形を構成する頂点IDの配列 (1から開始)'
    if aname == 'weights_arr':
        return '三角形を構成する頂点の値から内挿する際の重み係数の配列'
    if aname == 'nodeids_arr':
        return 'セルを構成する格子点のIDの配列 (1から開始)'
    if aname == 'position_arr':
        return '標高データの位置 (0より小さい = 左岸側, 0 より大きい = 右岸側)'
    if aname == 'height_arr':
        return '標高データの高さ'
    if aname == 'active_arr':
        return '標高データの有効/無効 (1: 有効, 0: 無効)'
    if aname == 'x':
        return 'X座標'
    if aname == 'y':
        return 'Y座標'
    if aname == 'dirx':
        return '向きのX成分'
    if aname == 'diry':
        return '向きのY成分'
    if aname == 'z':
        return 'Z座標'
    if aname == 'time':
        return '時刻'
    if aname == 'area':
        return '面積'
    if aname == 'index':
        if fname == 'iRIC_Geo_RiverSurvey_Read_FixedPointL':
            return '左岸延長線の開始位置の標高データの番号'
        elif fname == 'iRIC_Geo_RiverSurvey_Read_FixedPointR':
            return '右岸延長線の開始位置の標高データの番号'
    if aname == 'set':
        if fname == 'iRIC_Geo_RiverSurvey_Read_FixedPointL':
            return '左岸延長線が登録されていたら1, そうでなければ0'
        elif fname == 'iRIC_Geo_RiverSurvey_Read_FixedPointR':
            return '右岸延長線が登録されていたら1, そうでなければ0'
        elif fname == 'iRIC_Geo_RiverSurvey_Read_WaterSurfaceElevation':
            return '水面標高が登録されていたら1, そうでなければ0'
    if aname == 'shift':
        return 'シフト量'
    if aname == 'option':
        return '指定するオプションの値'
    if aname == 'ok':
        if fname == 'cg_iRIC_Read_Grid2d_Interpolate':
            return '指定した座標を含むセルが見つかった場合は1, そうでなければ0'
    if aname == 'numPoints':
        return 'ポリゴンもしくは折れ線を構成する頂点の数'
    if aname == 'value' or aname == 'strvalue':
        if '_Sol_' in fname:
            return '計算結果の値'
        elif '_Filename' in fname:
            return 'ファイル名'
        elif fname == 'iRIC_Geo_RiverSurvey_Read_Name':
            return '断面の名前'
        else:
            return '条件の値'
    if aname == 'progress':
        return '進捗 (0 ～ 100)'

    if '_BC_' in fname:
        if aname == 'num':
            return '境界条件の番号'

    if aname == 'type':
        if '_BC_' in fname:
            return '境界条件の名前'
        if fname == 'cg_iRIC_Read_Geo_Filename':
            return '地理情報の種類 (1 = ポリゴン, 2 = 横断測量データ)'

    if aname == 'num':
        if '_Complex_' in fname:
            return '複合型条件のグループ番号'

    if aname == 'groupname':
        if '_Complex_' in fname:
            return '複合型条件の名前'
        if re.search('_ParticleGroup(Image|)_', fname):
            return 'パーティクルグループの名前'
        if re.search('_PolyData_', fname):
            return 'ポリゴンもしくは折れ線のグループの名前'

    if aname == 'name':
        if 'Geo_' in fname:
            return '地理情報の名前'
        if re.match(r'^cg_iRIC_(Read|Write)_(BC_|Complex_|BaseIterative|)(Integer|Real|String|Functional).*$', fname):
            return '変数の名前'
        if re.match(r'^cg_iRIC_(Read|Write)_Sol_(BaseIterative|Node|Cell|IFace|JFace|KFace)_(Integer|Real|String).*$', fname):
            return '計算結果の名前'
        if re.match(r'^cg_iRIC_(Read|Write)_Sol_(Particle|PolyData)', fname):
            return '計算結果の名前'
        if re.match(r'^cg_iRIC_(Read|Write)_Grid_.*(Node|Cell|IFace|JFace|KFace|Functional(Dimension|Time)).*$', fname):
            return '格子属性の名前'
        if 'NamedGrid' in fname:
            return '格子の名前'

    if aname == 'paramname':
        if 'Functional' in fname:
            return '値の名前'
    if aname == 'step':
        if '_Sol_' in fname:
            return 'ステップ数'
    if aname == 'length':
        if 'StringLen' in fname:
            return '文字列の長さ'
        if 'Functional' in fname:
            return '条件の値の数'
        if 'Indices' in fname:
            return 'インデックスの数'
    if aname == 'dimid':
        if 'Grid_Functional' in fname:
            return '時刻のID (1 ～ 時刻の数)'
    if aname == 'dimname':
        if 'Grid_Functional' in fname:
            return '次元の名前'
    if aname == 'grid_handle':
        if 'cg_iRIC_Read_Grid2d' in fname or 'cg_iRIC_Read_Sol_Grid2d' in fname:
            return '格子のハンドル'
    if aname == 'cellId':
        return 'セルID (1から開始)'
    if aname == 'count':
        if 'FunctionalTimeSize' in fname:
            return '時刻の数'
        if 'FunctionalDimensionSize' in fname:
            return '次元の数'
        elif 'Particle' in fname:
            return 'パーティクルの数'
        elif fname == 'cg_iRIC_Read_Sol_Count':
            return '計算結果の数'
        elif fname == 'cg_iRIC_Read_Geo_Count':
            return '地理情報の数'
        elif fname == 'cg_iRIC_Read_Grid2d_CellNodeCount':
            return 'セルを構成する頂点の数'
        elif 'cg_iRIC_Read_Sol_PolyData_CoordinateCount' in fname:
            return 'ポリゴンもしくは折れ線を構成する頂点の数の合計値'
        elif 'cg_iRIC_Read_Sol_PolyData_DataCount' in fname:
            return 'ポリゴンもしくは折れ線の数'
        elif 'iRIC_Geo_Polygon_Read_HoleCount' in fname:
            return '穴の数'
        elif 'iRIC_Geo_Polygon_Read_HolePointCount' in fname:
            return '穴ポリゴンを構成する頂点の数'
        elif 'cg_iRIC_Read_Grid2d_Interpolate' in fname:
            return '指定した座標を含むセルを構成する頂点の数'
        elif 'iRIC_Geo_Polygon_Read_PointCount' in fname:
            return 'ポリゴンを構成する頂点の数'
        else:
            return '値の数'
    if aname == 'mode':
        if 'cg_iRIC_Open':
            return 'モード (IRIC_MODE_READ, IRIC_MODE_WRITE, IRIC_MODE_MODIFY のいずれか)'
    if aname == 'iteration':
        return 'ループ回数'
    if aname == 'errorcode':
        return 'エラーコード'

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
    lines.append('形式 (FORTRAN)')
    lines.append('-----------------')
    lines.append('')
    lines.append('.. code-block:: fortran')
    lines.append('')
    lines.append('   ' + build_fortran_format(f))
    lines.append('')
    lines.append('形式 (C/C++)')
    lines.append('-----------------')
    lines.append('')
    lines.append('.. code-block:: c')
    lines.append('')
    lines.append('   ' + build_c_format(f))
    lines.append('')
    lines.append('形式 (Python)')
    lines.append('-----------------')
    lines.append('')
    if '_RealSingle' in f['name']:
        lines.append('Python では定義されていません')
    else:
        lines.append('.. code-block:: python')
        lines.append('')
        lines.append('   ' + build_python_format(f))
    lines.append('')
    lines.append('引数と戻り値')
    lines.append('----------------------------')
    lines.append('')

    for a in f['args']:
        lines.append(a['name'])
        lines.append(''.join(['~'] * len(a['name'])))
        lines.append('')
        lines.append('.. list-table:: {0} の説明'.format(a['name']))
        lines.append('   :header-rows: 1')
        lines.append('')
        lines.append('   * - 項目')
        lines.append('     - 値')

        lines.append('   * - 名前')
        lines.append('     - {0}'.format(a['name']))

        lines.append('   * - 入力/出力')
        io = '入力'
        if a['type'] != 'const char*' and '*' in a['type']:
            io = '出力'
        lines.append('     - {0}'.format(io))
        lines.append('')

        lines.append('   * - 説明')
        lines.append('     - {0}'.format(build_arg_desc(f, a)))

        lines.append('   * - データ型 (FORTRAN)')
        lines.append('     - {0}'.format(build_arg_type_fortran(f, a)))
        lines.append('   * - データ型 (C/C++)')
        lines.append('     - {0}'.format(build_arg_type_c(f, a)))

        if not '_RealSingle' in f['name']:
            lines.append('   * - データ型 (Python)')
            lines.append('     - {0}'.format(build_arg_type_python(f, a)))
        lines.append('')

    if f['return_type'] == 'int':
        rname = 'ier'
        rdesc = 'エラーコード。0なら成功、エラーが起きるとそれ以外。'
        python_type = '(定義なし)'
        if f['name'] == 'iRIC_Check_Cancel':
            rname = 'canceled'
            rdesc = 'キャンセルされていたら1、そうでなければ0。'
            python_type = 'int'

        lines.append(rname)
        lines.append(''.join(['~'] * len(rname)))
        lines.append('')

        lines.append('.. list-table:: ' + rname + ' の説明')
        lines.append('   :header-rows: 1')
        lines.append('')
        lines.append('   * - 項目')
        lines.append('     - 値')

        lines.append('   * - 名前')
        lines.append('     - ' + rname)

        lines.append('   * - 入力/出力')
        lines.append('     - 出力')
        lines.append('')

        lines.append('   * - 説明')
        lines.append('     - ' + rdesc)

        lines.append('   * - データ型 (FORTRAN)')
        lines.append('     - integer')
        lines.append('   * - データ型 (C/C++)')
        lines.append('     - int')
        lines.append('   * - データ型 (Python)')
        lines.append('     - ' + python_type)
        lines.append('')

    if len(f['args']) == 0 and f['return_type'] != 'int':
        lines.append('引数がありません。')
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
