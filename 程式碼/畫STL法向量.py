import open3d as o3d
import numpy as np

# 讀取 STL 檔案
mesh = o3d.io.read_triangle_mesh(r"C:\NTHU\IRTI-Project\test.stl")

# 計算網格頂點的法向量
# mesh.compute_vertex_normals()

# 計算每個三角網格的法向量
mesh.compute_triangle_normals()  # TriangleMesh with 3512 points and 1224 triangles.
# 獲得每個三角形的三個點(這邊只按照順序標號 0-3511)
triangles = np.asarray(mesh.triangles)   # (1224, 3)
# 獲取每個點的位置
vertices = np.asarray(mesh.vertices)     # (3512, 3)
# 獲取每個三角網格的法向量
triangle_normals = np.asarray(mesh.triangle_normals)   # (1224, 3)
# 計算每個三角形的中心點 到時畫圖可化在此點上
triangle_centers = np.mean(vertices[triangles], axis=1)  # (1224, 3)
# 創建 list 以方便後面繪圖
lines = []
points = []
line_colors = []  

for i, center in enumerate(triangle_centers):  # enumerate 可加上編號 i
    # 將每一個三角網格中心點加入 points
    points.append(center)
    # 計算線段的終點，並且可自行調整長度，最後再加到 points 中
    end_point = center + triangle_normals[i] * 1  # 10 可調整
    points.append(end_point)
    # 增加線段的 index 前面為起點，後面為終點 --> line1 [0,1] line2 [2,3]...
    lines.append([2*i, 2*i + 1])
    # 設定線段顏色 (R,G,B)
    line_colors.append([255, 0, 0])  # 红色

# 創建一個 lineset ，此集合有所有三角網格法向量的資訊
line_set = o3d.geometry.LineSet(
    points=o3d.utility.Vector3dVector(points),
    lines=o3d.utility.Vector2iVector(lines)
)
line_set.colors = o3d.utility.Vector3dVector(line_colors)

# 將最後結果畫出來
o3d.visualization.draw_geometries([mesh, line_set])