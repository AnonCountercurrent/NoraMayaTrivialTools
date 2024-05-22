from importlib import reload
from PySide2 import QtCore, QtWidgets, QtGui
from Mesh.UI import noraNormalMapWidget
from General import noraMDagObjectSelect
from General import noraUtilities
import maya.api.OpenMaya as om
import maya.cmds as cmds
import os

reload(noraNormalMapWidget)
reload(noraMDagObjectSelect)
reload(noraUtilities)


def get_title():
    return 'Normal Map'


def get_ui():
    return NoraNormalMap()


def get_width():
    return 460


def get_height():
    return 300


def get_use_custom_front_style():
    return False


class NoraNormalMap(QtWidgets.QDialog, noraNormalMapWidget.Ui_noraNormalMapWidget):
    def __init__(self):
        super(NoraNormalMap, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # data
        self.cached_bounding = None

        # events
        self.cacheOutlineButton.clicked.connect(self.cache_selected_model_outline)
        self.generateNormlaMapPushButton.clicked.connect(self.pannar_normal_generate)

    def cache_selected_model_outline(self):
        self.cached_bounding = None
        mesh = noraUtilities.get_selected_mesh()
        if mesh is None:
            print("mesh is None")
            return
        bounding = [1e20, -1e20, 1e20, -1e20, 1e20, -1e20] # min x, max x, min y, max y, min z, max z
        vertices = mesh.getPoints(om.MSpace.kWorld)
        for i in range(len(vertices)):
            x = vertices[i].x
            y = vertices[i].y
            z = vertices[i].z
            if x < bounding[0]:
                bounding[0] = x
            if x > bounding[1]:
                bounding[1] = x
            if y < bounding[2]:
                bounding[2] = y
            if y > bounding[3]:
                bounding[3] = y
            if z < bounding[4]:
                bounding[4] = z
            if z > bounding[5]:
                bounding[5] = z
        self.cached_bounding = bounding
        print(bounding)

    def pannar_normal_generate(self):
        if self.cached_bounding is None:
            print("self.cached_bounding is None")
            return

        shell_mfn = None
        dag_name = noraUtilities.get_selected_dag_name()
        if cmds.objExists(dag_name):
            dag_path = noraUtilities.get_dag_path_by_name(dag_name)
            mesh_node = noraUtilities.get_connect_object(dag_path, om.MFn.kMesh)
            surface_node = noraUtilities.get_connect_object(dag_path, om.MFn.kNurbsSurface)
            if mesh_node is not None:
                shell_mfn = om.MFnMesh(dag_path)
                print("Shell is mesh")
            elif surface_node is not None:
                shell_mfn = om.MFnNurbsSurface(dag_path)
                print("Shell is nurbs surface")
            else:
                print("\'Shell\' is not nurbs surface or mesh")
                return
        else:
            print("\'Shell\' not set")
            return

        file_name = cmds.file(q=True, ns=True) + "_N"
        current_path = __file__
        current_path = os.path.dirname(current_path)  # e.g. E:/MayaTools
        save_name_tuple = QtWidgets.QFileDialog.getSaveFileName(self, 'save tga file', current_path + '/{0}.tga'.format(file_name), 'Json Files (*.tga)')
        if '.tga' not in save_name_tuple[0]:
            return

        tex_size = self.resolutionSpinBox.value()
        ray_dir = None
        ray_start = None
        u_start = 0.0
        v_start = 0.0
        u_end = 0.0
        v_end = 0.0
        if self.xRadioButton.isChecked():
            u_start = self.cached_bounding[4]
            u_end = self.cached_bounding[5]
            v_start = self.cached_bounding[2]
            v_end = self.cached_bounding[3]
            ray_dir = om.MVector(-1, 0, 0)
            ray_start = om.MVector(self.cached_bounding[1], v_end, u_end)
        elif self.yRadioButton.isChecked():
            u_start = self.cached_bounding[0]
            u_end = self.cached_bounding[1]
            v_start = self.cached_bounding[4]
            v_end = self.cached_bounding[5]
            ray_dir = om.MVector(0, -1, 0)
            ray_start = om.MVector(u_start, self.cached_bounding[3], v_start)
        else:
            u_start = self.cached_bounding[0]
            u_end = self.cached_bounding[1]
            v_start = self.cached_bounding[2]
            v_end = self.cached_bounding[3]
            ray_dir = om.MVector(0, 0, -1)
            ray_start = om.MVector(u_start, v_end, self.cached_bounding[4])
        step_u = (u_end - u_start) / (tex_size - 1.0)
        step_v = (v_end - v_start) / (tex_size - 1.0)

        ray_miss_num = 0
        image = QtGui.QImage(QtCore.QSize(tex_size, tex_size), QtGui.QImage.Format_RGB888)
        image.fill(QtGui.QColor(0, 0, 0))
        for i in range(tex_size):
            for j in range(tex_size):
                point_pos = None
                if self.xRadioButton.isChecked():
                    point_pos = om.MPoint(0, -j * step_v, -i * step_u) + ray_start
                elif self.yRadioButton.isChecked():
                    point_pos = om.MPoint(i * step_u, 0, j * step_v) + ray_start
                else:
                    point_pos = om.MPoint(i * step_u, -j * step_v, 0) + ray_start

                normal = om.MVector(0, 0, 0)
                if shell_mfn.type() == om.MFn.kMesh:
                    normal = noraUtilities.get_intersect_normal_on_mesh_surface(shell_mfn, point_pos, point_pos + ray_dir, 1e-8, False, 1e20)
                else:
                    normal = noraUtilities.get_intersect_normal_on_nurbs_surface(shell_mfn, point_pos, point_pos + ray_dir, 1e-8, False, 1e20)
                if normal is None:
                    ray_miss_num += 1
                    normal = om.MVector(-1, -1, -1)

                normal = (normal + om.MVector(1.0, 1.0, 1.0)) * 0.5 * 255.0
                image.setPixelColor(i, j, QtGui.QColor(normal.x, normal.z, normal.y))
        image.save(save_name_tuple[0], "PNG")
        print("ray miss count: " + str(ray_miss_num))
        print("ray miss rate: " + str(ray_miss_num / (tex_size * tex_size)))
