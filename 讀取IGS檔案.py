# import open3d as o3d

# mesh = o3d.io.read_triangle_mesh("D0920.IGS")

# o3d.visualization.draw_geometries([mesh])

import pyiges

iges = pyiges.Iges(r"C:\NTHU\IRTI-Project\D0920.IGS")

print(iges)

mesh = iges.bspline_surfaces(as_vtk=True, merge=True)
mesh.plot()