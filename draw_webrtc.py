# ----------------------------------------------------------------------------
# -                        Open3D: www.open3d.org                            -
# ----------------------------------------------------------------------------
# Copyright (c) 2018-2023 www.open3d.org
# SPDX-License-Identifier: MIT
# ----------------------------------------------------------------------------

import open3d as o3d

# if __name__ == "__main__":
#     o3d.visualization.webrtc_server.enable_webrtc()
#     cube_red = o3d.geometry.TriangleMesh.create_box(1, 2, 4)
#     cube_red.compute_vertex_normals()
#     cube_red.paint_uniform_color((1.0, 0.0, 0.0))
#     o3d.visualization.draw(cube_red)

# import open3d as o3d
# from open3d.web_visualizer import draw

# # 加载球体网格
# mesh = o3d.io.read_triangle_mesh("sphere.ply")

# # 显示球体网格在Web浏览器中
# draw([mesh])

# o3d.visualization.webrtc_server.enable_webrtc()
# cube_red = o3d.geometry.TriangleMesh.create_box(1, 2, 4)
# # cube_red = o3d.geometry.TriangleMesh.create_sphere()
# cube_red.compute_vertex_normals()
# cube_red.paint_uniform_color((1.0, 0.0, 0.0))
# o3d.visualization.draw(cube_red)

import open3d as o3d
import numpy as np
from open3d.visualization import web_visualizer

# 创建一个随机点云
num_points = 1000
points = np.random.rand(num_points, 3)

# 创建Open3D点云对象
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

# 保存点云为PLY文件
o3d.io.write_point_cloud("random_point_cloud.ply", point_cloud)

# 加载点云数据
point_cloud = o3d.io.read_point_cloud("random_point_cloud.ply")

# 显示点云数据在Web浏览器中
web_visualizer.draw([point_cloud], window_name="Point Cloud", width=800, height=600, left=50, top=50)

