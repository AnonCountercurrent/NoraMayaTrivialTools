# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraNormalMappingWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraNormalMappingWidget(object):
    def setupUi(self, noraNormalMappingWidget):
        if not noraNormalMappingWidget.objectName():
            noraNormalMappingWidget.setObjectName(u"noraNormalMappingWidget")
        noraNormalMappingWidget.resize(351, 359)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(noraNormalMappingWidget.sizePolicy().hasHeightForWidth())
        noraNormalMappingWidget.setSizePolicy(sizePolicy)
        noraNormalMappingWidget.setMinimumSize(QSize(60, 0))
        self.verticalLayout_2 = QVBoxLayout(noraNormalMappingWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(noraNormalMappingWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.meshDagPathSelectedLayout = QHBoxLayout()
        self.meshDagPathSelectedLayout.setObjectName(u"meshDagPathSelectedLayout")

        self.verticalLayout.addLayout(self.meshDagPathSelectedLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.vertexIndicesCountLineEdit = QLineEdit(self.groupBox)
        self.vertexIndicesCountLineEdit.setObjectName(u"vertexIndicesCountLineEdit")
        self.vertexIndicesCountLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.vertexIndicesCountLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.vertexIndicesCountLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.shellDagPathSelectedLayout = QHBoxLayout()
        self.shellDagPathSelectedLayout.setObjectName(u"shellDagPathSelectedLayout")

        self.verticalLayout.addLayout(self.shellDagPathSelectedLayout)

        self.curveDagPathSelectedLayout = QHBoxLayout()
        self.curveDagPathSelectedLayout.setObjectName(u"curveDagPathSelectedLayout")

        self.verticalLayout.addLayout(self.curveDagPathSelectedLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 315, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraNormalMappingWidget)

        QMetaObject.connectSlotsByName(noraNormalMappingWidget)
    # setupUi

    def retranslateUi(self, noraNormalMappingWidget):
        noraNormalMappingWidget.setWindowTitle(QCoreApplication.translate("noraNormalMappingWidget", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraNormalMappingWidget", u"Target", None))
        self.label.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Vertex indices count: ", None))
        self.vertexIndicesCountLineEdit.setText(QCoreApplication.translate("noraNormalMappingWidget", u"all", None))
        self.pushButton.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Cache selected vertices", None))
    # retranslateUi

