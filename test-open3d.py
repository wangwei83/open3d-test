import open3d as o3d
print("Helloworld")
print(o3d.__version__)
mesh = o3d.geometry.TriangleMesh.create_sphere();
# 设置球体的颜色
mesh.paint_uniform_color([1, 0.706, 0])
# mesh.paint_uniform_color([0, 0, 1])
mesh.compute_vertex_normals();
o3d.visualization.draw(mesh)



# import open3d as o3d

# # 创建一个球形三角网格
# mesh = o3d.geometry.TriangleMesh.create_sphere()

# # 设置球体的颜色为蓝色
# mesh.paint_uniform_color([0, 0, 1])

# # 计算球体的法向量
# mesh.compute_vertex_normals()

# # 保存球体网格为一个PLY文件
# o3d.io.write_triangle_mesh("sphere.ply", mesh)
