# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraRemoveScaleWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraRemoveScaleWidget(object):
    def setupUi(self, noraRemoveScaleWidget):
        if not noraRemoveScaleWidget.objectName():
            noraRemoveScaleWidget.setObjectName(u"noraRemoveScaleWidget")
        noraRemoveScaleWidget.resize(495, 383)
        self.verticalLayout_2 = QVBoxLayout(noraRemoveScaleWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(noraRemoveScaleWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.subobjectsCheckBox = QCheckBox(self.groupBox)
        self.subobjectsCheckBox.setObjectName(u"subobjectsCheckBox")
        self.subobjectsCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.subobjectsCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.maintainRotationCheckBox = QCheckBox(self.groupBox)
        self.maintainRotationCheckBox.setObjectName(u"maintainRotationCheckBox")
        self.maintainRotationCheckBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.maintainRotationCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.leftRange = QLineEdit(self.groupBox)
        self.leftRange.setObjectName(u"leftRange")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftRange.sizePolicy().hasHeightForWidth())
        self.leftRange.setSizePolicy(sizePolicy1)
        self.leftRange.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.leftRange)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.rightRange = QLineEdit(self.groupBox)
        self.rightRange.setObjectName(u"rightRange")
        sizePolicy1.setHeightForWidth(self.rightRange.sizePolicy().hasHeightForWidth())
        self.rightRange.setSizePolicy(sizePolicy1)
        self.rightRange.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.rightRange)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(noraRemoveScaleWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.removeScaleButton = QPushButton(self.groupBox_3)
        self.removeScaleButton.setObjectName(u"removeScaleButton")

        self.verticalLayout_4.addWidget(self.removeScaleButton)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraRemoveScaleWidget)

        QMetaObject.connectSlotsByName(noraRemoveScaleWidget)
    # setupUi

    def retranslateUi(self, noraRemoveScaleWidget):
        noraRemoveScaleWidget.setWindowTitle(QCoreApplication.translate("noraRemoveScaleWidget", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraRemoveScaleWidget", u"Settings", None))
        self.subobjectsCheckBox.setText(QCoreApplication.translate("noraRemoveScaleWidget", u"All sub objects", None))
        self.maintainRotationCheckBox.setText(QCoreApplication.translate("noraRemoveScaleWidget", u"Maintain rotation", None))
        self.label_3.setText(QCoreApplication.translate("noraRemoveScaleWidget", u"Frame range\uff1a", None))
        self.leftRange.setText(QCoreApplication.translate("noraRemoveScaleWidget", u"0", None))
        self.label_4.setText(QCoreApplication.translate("noraRemoveScaleWidget", u"-", None))
        self.rightRange.setText(QCoreApplication.translate("noraRemoveScaleWidget", u"10", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("noraRemoveScaleWidget", u"Actions", None))
        self.removeScaleButton.setText(QCoreApplication.translate("noraRemoveScaleWidget", u"Remove Scale", None))
    # retranslateUi

