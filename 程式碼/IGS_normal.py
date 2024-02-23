## 讀取檔案並秀出
# from OCC.Display.SimpleGui import init_display
# from OCC.Extend.DataExchange import read_iges_file

# shapes = read_iges_file(r"C:\Users\Martin\IRTI-Project\my_box.igs")

# display, start_display, add_menu, add_function_to_menu = init_display()
# display.DisplayShape(shapes, update=True)
# start_display()


import os
from OCC.Core.IGESControl import IGESControl_Reader
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopoDS import topods_Face
from OCC.Core.BRepAdaptor import BRepAdaptor_Surface
from OCC.Core.BRepLProp import BRepLProp_SLProps
from OCC.Core.TopAbs import TopAbs_FACE
from OCC.Core.gp import gp_Pnt2d

# IGS檔案路徑
file_path = r"C:\Users\Martin\IRTI-Project\my_box.igs"

# 確認文件是否存在
if not os.path.exists(file_path):
    print("文件不存在，请检查路径")
else:
    # 讀取檔案
    reader = IGESControl_Reader()
    reader.ReadFile(file_path)
    reader.TransferRoots()
    shape = reader.Shape()

    # 找所有的面
    explorer = TopExp_Explorer(shape, TopAbs_FACE)
    while explorer.More():
        face = topods_Face(explorer.Current())
        adaptor_surface = BRepAdaptor_Surface(face, True)
        props = BRepLProp_SLProps(adaptor_surface, 2, 0.01)
        u_min, u_max, v_min, v_max = adaptor_surface.FirstUParameter(), adaptor_surface.LastUParameter(), adaptor_surface.FirstVParameter(), adaptor_surface.LastVParameter()
        u_mid = (u_min + u_max) / 2
        v_mid = (v_min + v_max) / 2
        props.SetParameters(u_mid, v_mid)
        if props.IsCurvatureDefined():
            normal = props.Normal()
            # 如果面朝向是反的，反轉法向量
            if face.Orientation() == TopAbs_FACE:
                normal.Reverse()
            print("法向量:", normal.X(), normal.Y(), normal.Z())
        explorer.Next()