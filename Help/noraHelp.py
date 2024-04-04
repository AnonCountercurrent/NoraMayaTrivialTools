from importlib import reload
from PySide2 import QtCore, QtGui, QtWidgets
from Help.UI import noraHelpWidget
from Help.UI.noraHelpWidget import Ui_noraHelpWidget
from General.noraUtilities import *
import webbrowser

reload(noraHelpWidget)


def get_title():
    return 'About'


def get_ui():
    return NoraHelp()


def get_width():
    return 460


def get_height():
    return 500


def get_use_custom_front_style():
    return True


def docs_link():
    webbrowser.open("http://www.baidu.com")


class NoraHelp(QtWidgets.QDialog, Ui_noraHelpWidget):
    def __init__(self):
        super(NoraHelp, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        self.gotoDocs.clicked.connect(docs_link)

        self.picture = QtGui.QPixmap()
        self.picture.load(get_icon_path("Nora_Valkyrie_Emblem_128.png"))
        self.IconLabel.setPixmap(self.picture)

