# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraSelectByVertexInfoWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraSelectByVertexInfoWidget(object):
    def setupUi(self, noraSelectByVertexInfoWidget):
        if not noraSelectByVertexInfoWidget.objectName():
            noraSelectByVertexInfoWidget.setObjectName(u"noraSelectByVertexInfoWidget")
        noraSelectByVertexInfoWidget.resize(334, 300)
        self.verticalLayout_2 = QVBoxLayout(noraSelectByVertexInfoWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(noraSelectByVertexInfoWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.meshDagPathSelectedLayout = QHBoxLayout()
        self.meshDagPathSelectedLayout.setObjectName(u"meshDagPathSelectedLayout")

        self.horizontalLayout_4.addLayout(self.meshDagPathSelectedLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(noraSelectByVertexInfoWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.byDistanceCheckBox = QCheckBox(self.groupBox_2)
        self.byDistanceCheckBox.setObjectName(u"byDistanceCheckBox")
        self.byDistanceCheckBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.byDistanceCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.minDistanceSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.minDistanceSpinBox.setObjectName(u"minDistanceSpinBox")
        self.minDistanceSpinBox.setDecimals(6)
        self.minDistanceSpinBox.setValue(0.001000000000000)

        self.horizontalLayout.addWidget(self.minDistanceSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sameTriangleCheckBox = QCheckBox(self.groupBox_2)
        self.sameTriangleCheckBox.setObjectName(u"sameTriangleCheckBox")

        self.horizontalLayout_2.addWidget(self.sameTriangleCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(noraSelectByVertexInfoWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.selectVertButton = QPushButton(self.groupBox_3)
        self.selectVertButton.setObjectName(u"selectVertButton")

        self.horizontalLayout_5.addWidget(self.selectVertButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraSelectByVertexInfoWidget)

        QMetaObject.connectSlotsByName(noraSelectByVertexInfoWidget)
    # setupUi

    def retranslateUi(self, noraSelectByVertexInfoWidget):
        noraSelectByVertexInfoWidget.setWindowTitle(QCoreApplication.translate("noraSelectByVertexInfoWidget", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraSelectByVertexInfoWidget", u"Targets", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("noraSelectByVertexInfoWidget", u"Settings", None))
        self.byDistanceCheckBox.setText(QCoreApplication.translate("noraSelectByVertexInfoWidget", u"By distance", None))
        self.label.setText(QCoreApplication.translate("noraSelectByVertexInfoWidget", u"Max distance:", None))
        self.sameTriangleCheckBox.setText(QCoreApplication.translate("noraSelectByVertexInfoWidget", u"Within the same triangle", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("noraSelectByVertexInfoWidget", u"Actions", None))
        self.selectVertButton.setText(QCoreApplication.translate("noraSelectByVertexInfoWidget", u"Select vertices", None))
    # retranslateUi

