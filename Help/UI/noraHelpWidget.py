# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraHelpWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraHelpWidget(object):
    def setupUi(self, noraHelpWidget):
        if not noraHelpWidget.objectName():
            noraHelpWidget.setObjectName(u"noraHelpWidget")
        noraHelpWidget.resize(460, 500)
        self.verticalLayout_2 = QVBoxLayout(noraHelpWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(noraHelpWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 200))
        self.IconLabel = QLabel(self.widget)
        self.IconLabel.setObjectName(u"IconLabel")
        self.IconLabel.setGeometry(QRect(10, 30, 128, 128))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 40, 251, 71))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText(u"Nora Trivial Tools")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 100, 431, 31))
        font1 = QFont()
        font1.setFamily(u"\u5e7c\u5706")
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setText(u"A collection of trivial tools")

        self.verticalLayout_2.addWidget(self.widget)

        self.label_6 = QLabel(noraHelpWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setFont(font1)
        self.label_6.setText(u"DocLinks:")

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(noraHelpWidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(30, 0))

        self.horizontalLayout.addWidget(self.widget_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gotoDocs = QCommandLinkButton(noraHelpWidget)
        self.gotoDocs.setObjectName(u"gotoDocs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gotoDocs.sizePolicy().hasHeightForWidth())
        self.gotoDocs.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        font2.setUnderline(True)
        self.gotoDocs.setFont(font2)
        self.gotoDocs.setCursor(QCursor(Qt.PointingHandCursor))
        self.gotoDocs.setText(u"Git URL")
        self.gotoDocs.setAutoDefault(True)

        self.verticalLayout.addWidget(self.gotoDocs)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraHelpWidget)

        QMetaObject.connectSlotsByName(noraHelpWidget)
    # setupUi

    def retranslateUi(self, noraHelpWidget):
        noraHelpWidget.setWindowTitle(QCoreApplication.translate("noraHelpWidget", u"Dialog", None))
        self.IconLabel.setText("")
    # retranslateUi

