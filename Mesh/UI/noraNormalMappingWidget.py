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
        noraNormalMappingWidget.resize(351, 454)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(noraNormalMappingWidget.sizePolicy().hasHeightForWidth())
        noraNormalMappingWidget.setSizePolicy(sizePolicy)
        noraNormalMappingWidget.setMinimumSize(QSize(60, 0))
        self.verticalLayout_5 = QVBoxLayout(noraNormalMappingWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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
        self.cacheSelectedVerticesButton = QPushButton(self.groupBox)
        self.cacheSelectedVerticesButton.setObjectName(u"cacheSelectedVerticesButton")

        self.horizontalLayout_2.addWidget(self.cacheSelectedVerticesButton)


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


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(noraNormalMappingWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.centerRadioButton = QRadioButton(self.groupBox_2)
        self.centerRadioButton.setObjectName(u"centerRadioButton")
        self.centerRadioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.centerRadioButton)

        self.curveRadioButton = QRadioButton(self.groupBox_2)
        self.curveRadioButton.setObjectName(u"curveRadioButton")

        self.verticalLayout_2.addWidget(self.curveRadioButton)

        self.closestRadioButton = QRadioButton(self.groupBox_2)
        self.closestRadioButton.setObjectName(u"closestRadioButton")

        self.verticalLayout_2.addWidget(self.closestRadioButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.tolSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.tolSpinBox.setObjectName(u"tolSpinBox")
        self.tolSpinBox.setDecimals(6)
        self.tolSpinBox.setMinimum(0.000001000000000)
        self.tolSpinBox.setMaximum(1.000000000000000)
        self.tolSpinBox.setSingleStep(0.001000000000000)
        self.tolSpinBox.setValue(0.000100000000000)

        self.horizontalLayout_3.addWidget(self.tolSpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.twoWayCheckBox = QCheckBox(self.groupBox_2)
        self.twoWayCheckBox.setObjectName(u"twoWayCheckBox")
        self.twoWayCheckBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.twoWayCheckBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.maxRadiusSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.maxRadiusSpinBox.setObjectName(u"maxRadiusSpinBox")
        self.maxRadiusSpinBox.setDecimals(6)
        self.maxRadiusSpinBox.setMinimum(0.000001000000000)
        self.maxRadiusSpinBox.setMaximum(1000.000000000000000)
        self.maxRadiusSpinBox.setValue(100.000000000000000)

        self.horizontalLayout_5.addWidget(self.maxRadiusSpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(noraNormalMappingWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.normalMappingButton = QPushButton(self.groupBox_3)
        self.normalMappingButton.setObjectName(u"normalMappingButton")

        self.verticalLayout_4.addWidget(self.normalMappingButton)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 315, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.retranslateUi(noraNormalMappingWidget)

        QMetaObject.connectSlotsByName(noraNormalMappingWidget)
    # setupUi

    def retranslateUi(self, noraNormalMappingWidget):
        noraNormalMappingWidget.setWindowTitle(QCoreApplication.translate("noraNormalMappingWidget", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraNormalMappingWidget", u"Targets", None))
        self.label.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Vertex indices count: ", None))
        self.vertexIndicesCountLineEdit.setText(QCoreApplication.translate("noraNormalMappingWidget", u"all", None))
        self.cacheSelectedVerticesButton.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Cache selected vertices", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("noraNormalMappingWidget", u"Settings", None))
        self.centerRadioButton.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Center Mode", None))
        self.curveRadioButton.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Curve Mode", None))
        self.closestRadioButton.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Closest Mode", None))
        self.label_2.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Intersect tolerance: ", None))
        self.twoWayCheckBox.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Bidirectional detection", None))
        self.label_3.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Max radius: ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("noraNormalMappingWidget", u"Actions", None))
        self.normalMappingButton.setText(QCoreApplication.translate("noraNormalMappingWidget", u"Normal Mapping", None))
    # retranslateUi

