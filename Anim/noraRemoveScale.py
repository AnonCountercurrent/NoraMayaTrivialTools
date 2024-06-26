from importlib import reload
from PySide2 import QtCore, QtWidgets, QtGui
from UI import noraRemoveScaleWidget
from General import noraMDagObjectSelect
from General import noraUtilities
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds
import os

reload(noraRemoveScaleWidget)
reload(noraMDagObjectSelect)
reload(noraUtilities)


def get_title():
    return 'Remove Scale'


def get_ui():
    return NoraNormalMap()


def get_width():
    return 460


def get_height():
    return 300


def get_use_custom_front_style():
    return False


class NoraNormalMap(QtWidgets.QDialog, noraRemoveScaleWidget.Ui_noraRemoveScaleWidget):
    def __init__(self):
        super(NoraNormalMap, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        # events
        self.removeScaleButton.clicked.connect(self.remove_scale)

    def remove_scale(self):
        collect_sub_objects = self.subobjectsCheckBox.isChecked()
        start_frame = int(self.leftRange.text())
        end_frame = int(self.rightRange.text())

        selection_ls = om.MGlobal.getActiveSelectionList()
        if selection_ls.isEmpty():
            print("nora: selection_ls.isEmpty()")
            pass

        if end_frame - start_frame < 0:
            print("end_frame - start_frame < 0")
            pass

        dag_paths = []
        for i in range(selection_ls.length()):
            dag_path = selection_ls.getDagPath(i)
            if collect_sub_objects:
                new_dag_paths = [dag_path]
                new_parent_list = [-1]
                noraUtilities.collect_sub_dag_paths(dag_path, 0, new_dag_paths, new_parent_list)
                for new_dag_path in new_dag_paths:
                    if new_dag_path not in dag_paths:
                        dag_paths.append(new_dag_path)
            else:
                dag_paths.append(dag_path)

        # [[MMatrix]]
        matrices = noraUtilities.collect_dag_path_matrices(dag_paths, start_frame, end_frame + 1)

        # remove scale
        for dag_path in dag_paths:
            full_path_name = dag_path.fullPathName()
            sel_list = om.MSelectionList()
            sel_list.add("{0}.{1}".format(full_path_name, "scaleX"))
            sel_list.add("{0}.{1}".format(full_path_name, "scaleY"))
            sel_list.add("{0}.{1}".format(full_path_name, "scaleZ"))
            for i in range(0, 3):
                mplug = sel_list.getPlug(i)
                connected_plugs = mplug.connectedTo(True, False)
                for conn in connected_plugs:
                    conn_node = conn.node()
                    if conn_node.hasFn(om.MFn.kAnimCurve):
                        curve_node = oma.MFnAnimCurve(conn_node)
                        while curve_node.numKeys != 0:
                            curve_node.remove(curve_node.numKeys - 1)
            for i in range(0, 3):
                mplug = sel_list.getPlug(i)
                connected_plugs = mplug.connectedTo(True, False)
                for conn in connected_plugs:
                    conn_node = conn.node()
                    if conn_node.hasFn(om.MFn.kAnimCurve):
                        curve_node = oma.MFnAnimCurve(conn_node)
                        curve_node.addKey(om.MTime(start_frame, om.MTime.uiUnit()), 1.0, oma.MFnAnimCurve.kTangentStep, oma.MFnAnimCurve.kTangentStep)

        # set rotation
        if self.maintainRotationCheckBox.isChecked():
            key_times = om.MTimeArray()
            for i in range(start_frame, end_frame + 1):
                key_times.append(om.MTime(i, om.MTime.uiUnit()))
            for i in range(len(dag_paths)):
                full_path_name = dag_paths[i].fullPathName()
                rotation_x = []
                rotation_y = []
                rotation_z = []
                for j in range(start_frame, end_frame + 1):
                    ts = om.MTransformationMatrix(matrices[j][i])
                    euler_rotation = ts.rotation(False)
                    rotation_x.append(euler_rotation.x * 180.0 / 3.14)
                    rotation_y.append(euler_rotation.y * 180.0 / 3.14)
                    rotation_z.append(euler_rotation.z * 180.0 / 3.14)
                noraUtilities.set_keyframes(full_path_name, "rotateX", key_times, rotation_x)
                noraUtilities.set_keyframes(full_path_name, "rotateY", key_times, rotation_y)
                noraUtilities.set_keyframes(full_path_name, "rotateZ", key_times, rotation_z)




