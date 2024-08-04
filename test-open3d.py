import open3d as o3d
print("Helloworld")

mesh = o3d.geometry.TriangleMesh.create_sphere();
# 设置球体的颜色
# mesh.paint_uniform_color([1, 0.706, 0])
mesh.paint_uniform_color([0, 0, 1])
mesh.compute_vertex_normals();
o3d.visualization.draw(mesh)
print(o3d.__version__)