from importlib import reload
from PySide2 import QtCore, QtWidgets
from Mesh.UI import noraNormalMappingWidget
from General import noraMDagObjectSelect
from General import noraUtilities
import maya.api.OpenMaya as om
import maya.cmds as cmds

reload(noraNormalMappingWidget)
reload(noraMDagObjectSelect)
reload(noraUtilities)


def get_title():
    return 'Normal Mapping'


def get_ui():
    return NoraNormalMapping()


def get_width():
    return 460


def get_height():
    return 600


def get_use_custom_front_style():
    return False


class NoraNormalMapping(QtWidgets.QDialog, noraNormalMappingWidget.Ui_noraNormalMappingWidget):
    def __init__(self):
        super(NoraNormalMapping, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # ui
        self.model_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.model_select_widget.set_label_text("Mesh: ")
        self.meshDagPathSelectedLayout.addWidget(self.model_select_widget)
        self.curve_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.curve_select_widget.set_label_text("Curve/Center: ")
        self.curveDagPathSelectedLayout.addWidget(self.curve_select_widget)
        self.shell_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.shell_select_widget.set_label_text("Shell: ")
        self.shellDagPathSelectedLayout.addWidget(self.shell_select_widget)



