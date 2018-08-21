# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ag/orbit/gui/qt/wallet/key.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShowKey(object):
    def setupUi(self, ShowKey):
        ShowKey.setObjectName("ShowKey")
        ShowKey.resize(471, 270)
        ShowKey.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShowKey)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QPushButton(ShowKey)
        self.closeButton.setDefault(True)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(ShowKey)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox = QtWidgets.QGroupBox(ShowKey)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wifButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.wifButton.setFont(font)
        self.wifButton.setAutoDefault(False)
        self.wifButton.setFlat(True)
        self.wifButton.setObjectName("wifButton")
        self.verticalLayout_2.addWidget(self.wifButton)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(ShowKey)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(ShowKey)
        QtCore.QMetaObject.connectSlotsByName(ShowKey)

    def retranslateUi(self, ShowKey):
        _translate = QtCore.QCoreApplication.translate
        ShowKey.setWindowTitle(_translate("ShowKey", "Private Key"))
        self.closeButton.setText(_translate("ShowKey", "Close"))
        self.label.setText(_translate("ShowKey", "Bitcoin Cash Private Key"))
        self.groupBox.setTitle(_translate("ShowKey", "WIF"))
        self.wifButton.setText(_translate("ShowKey", "(wif)"))
        self.label_3.setText(_translate("ShowKey", "Click on key to copy to clipboard"))

