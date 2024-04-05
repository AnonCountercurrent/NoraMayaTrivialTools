from importlib import reload
from PySide2 import QtCore, QtWidgets
from Select.UI import noraSelectByVertexInfoWidget
from General import noraMDagObjectSelect
import maya.api.OpenMaya as om
import maya.cmds as cmds

reload(noraSelectByVertexInfoWidget)
reload(noraMDagObjectSelect)


def get_title():
    return 'By Vertex Info'


def get_ui():
    return NoraSelectByVertexInfo()


def get_width():
    return 460


def get_height():
    return 600


def get_use_custom_front_style():
    return False


class NoraSelectByVertexInfo(QtWidgets.QDialog, noraSelectByVertexInfoWidget.Ui_noraSelectByVertexInfoWidget):
    def __init__(self):
        super(NoraSelectByVertexInfo, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # ui
        self.model_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.model_select_widget.set_label_text("Mesh: ")
        self.meshDagPathSelectedLayout.addWidget(self.model_select_widget)

        # bind
        self.selectVertButton.clicked.connect(self.select_vertices)

    def select_vertices(self):
        dag_path_list = None
        dag_path = self.model_select_widget.dag_name
        if cmds.objExists(dag_path):
            cmds.select(dag_path)
            dag_path_list = om.MGlobal.getActiveSelectionList()
        else:
            dag_path_list = om.MGlobal.getActiveSelectionList()

        by_distance = self.byDistanceCheckBox.isChecked()
        min_dist = self.minDistanceSpinBox.value()
        same_triangle_only = self.sameTriangleCheckBox.isChecked()

        vertex_select_list = []
        for i in range(dag_path_list.length()):
            dag_path = dag_path_list.getDagPath(i)
            mesh = om.MFnMesh(dag_path)
            if mesh is not None:
                mesh = om.MFnMesh(dag_path)
                vertices = mesh.getPoints(om.MSpace.kWorld)
                indices = mesh.getTriangles()[1]

                vertex_to_selection = []
                if by_distance:
                    if same_triangle_only:
                        for j in range(0, len(indices), 3):
                            d01 = vertices[indices[j]].distanceTo(vertices[indices[j + 1]])
                            d02 = vertices[indices[j]].distanceTo(vertices[indices[j + 2]])
                            d12 = vertices[indices[j + 1]].distanceTo(vertices[indices[j + 2]])
                            if d01 < min_dist or d02 < min_dist or d12 < min_dist:
                                if indices[j] not in vertex_to_selection:
                                    vertex_to_selection.append(indices[j])
                                if indices[j + 1] not in vertex_to_selection:
                                    vertex_to_selection.append(indices[j + 1])
                                if indices[j + 2] not in vertex_to_selection:
                                    vertex_to_selection.append(indices[j + 2])
                    else:
                        for j in range(0, len(vertices)):
                            for k in range(j + 1, len(vertices)):
                                p0 = vertices[j]
                                p1 = vertices[k]
                                if p0.distanceTo(p1) < min_dist:
                                    if j not in vertex_to_selection:
                                        vertex_to_selection.append(j)
                                    if k not in vertex_to_selection:
                                        vertex_to_selection.append(k)
                    for j in range(len(vertex_to_selection)):
                        vertex_select_list.append("{0}.vtx[{1}]".format(mesh.name(), vertex_to_selection[j]))

        if len(vertex_select_list) > 1:
            cmds.select(vertex_select_list)




