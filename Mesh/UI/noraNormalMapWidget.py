# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraNormalMapWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraNormalMapWidget(object):
    def setupUi(self, noraNormalMapWidget):
        if not noraNormalMapWidget.objectName():
            noraNormalMapWidget.setObjectName(u"noraNormalMapWidget")
        noraNormalMapWidget.resize(434, 395)
        self.verticalLayout_3 = QVBoxLayout(noraNormalMapWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(noraNormalMapWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.xRadioButton = QRadioButton(self.groupBox)
        self.xRadioButton.setObjectName(u"xRadioButton")
        self.xRadioButton.setChecked(False)

        self.verticalLayout_2.addWidget(self.xRadioButton)

        self.yRadioButton = QRadioButton(self.groupBox)
        self.yRadioButton.setObjectName(u"yRadioButton")

        self.verticalLayout_2.addWidget(self.yRadioButton)

        self.zRadioButton = QRadioButton(self.groupBox)
        self.zRadioButton.setObjectName(u"zRadioButton")
        self.zRadioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.zRadioButton)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.resolutionSpinBox = QSpinBox(self.groupBox)
        self.resolutionSpinBox.setObjectName(u"resolutionSpinBox")
        self.resolutionSpinBox.setMinimum(4)
        self.resolutionSpinBox.setMaximum(4096)
        self.resolutionSpinBox.setSingleStep(4)
        self.resolutionSpinBox.setValue(256)

        self.horizontalLayout.addWidget(self.resolutionSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cacheOutlineButton = QPushButton(self.groupBox)
        self.cacheOutlineButton.setObjectName(u"cacheOutlineButton")

        self.horizontalLayout_2.addWidget(self.cacheOutlineButton)

        self.generateNormlaMapPushButton = QPushButton(self.groupBox)
        self.generateNormlaMapPushButton.setObjectName(u"generateNormlaMapPushButton")

        self.horizontalLayout_2.addWidget(self.generateNormlaMapPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 206, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(noraNormalMapWidget)

        QMetaObject.connectSlotsByName(noraNormalMapWidget)
    # setupUi

    def retranslateUi(self, noraNormalMapWidget):
        noraNormalMapWidget.setWindowTitle(QCoreApplication.translate("noraNormalMapWidget", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraNormalMapWidget", u"Planar intersection", None))
        self.xRadioButton.setText(QCoreApplication.translate("noraNormalMapWidget", u"X", None))
        self.yRadioButton.setText(QCoreApplication.translate("noraNormalMapWidget", u"Y", None))
        self.zRadioButton.setText(QCoreApplication.translate("noraNormalMapWidget", u"Z", None))
        self.label.setText(QCoreApplication.translate("noraNormalMapWidget", u"Resolution: ", None))
        self.cacheOutlineButton.setText(QCoreApplication.translate("noraNormalMapWidget", u"Cache selected mesh's outline", None))
        self.generateNormlaMapPushButton.setText(QCoreApplication.translate("noraNormalMapWidget", u"Generate normal map", None))
    # retranslateUi

