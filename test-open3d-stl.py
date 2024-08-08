import open3d as o3d
#模型路径，支持后缀：stl/ply/obj/off/gltf/glb
path_obj = 'Rmk3.obj'
#读入网格模型
mesh = o3d.io.read_triangle_mesh(path_obj)
#计算网格顶点
mesh.compute_vertex_normals()
#可视化网格模型
o3d.visualization.draw_geometries([mesh])
