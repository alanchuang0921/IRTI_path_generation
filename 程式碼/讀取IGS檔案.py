import pyiges

# print(dir(pyiges))
# print(pyiges.__builtins__)

# 讀取檔案
iges = pyiges.Iges(r"C:\NTHU\IRTI-Project\shing_hong project EZsim\model\3075010.035-.042_3.IGS")
print(iges)

# 使用 bspline 的方式畫出來
# mesh = iges.bspline_surfaces(as_vtk=True, merge=True)
# mesh.plot()

# lines = iges.to_vtk(surfaces=False)
# print(lines)

mesh = iges.to_vtk(bsplines=False, surfaces=True, merge=True, delta=0.05)
mesh.plot(color='w', smooth_shading=True)

# point = iges.points(as_vtk=True, merge=True)
# print(type(point))
# print(point)