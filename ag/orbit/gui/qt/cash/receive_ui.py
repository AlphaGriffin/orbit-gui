# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ag/orbit/gui/qt/cash/receive.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Receive(object):
    def setupUi(self, Receive):
        Receive.setObjectName("Receive")
        Receive.resize(411, 467)
        Receive.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Receive)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QPushButton(Receive)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.qrcode = QtWidgets.QLabel(Receive)
        self.qrcode.setScaledContents(False)
        self.qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.qrcode.setObjectName("qrcode")
        self.verticalLayout.addWidget(self.qrcode)
        self.addressButton = QtWidgets.QPushButton(Receive)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.addressButton.setFont(font)
        self.addressButton.setFlat(True)
        self.addressButton.setObjectName("addressButton")
        self.verticalLayout.addWidget(self.addressButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Receive)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Receive)
        QtCore.QMetaObject.connectSlotsByName(Receive)

    def retranslateUi(self, Receive):
        _translate = QtCore.QCoreApplication.translate
        Receive.setWindowTitle(_translate("Receive", "Receive Bitcoin Cash"))
        self.closeButton.setText(_translate("Receive", "Close"))
        self.qrcode.setText(_translate("Receive", "(qrcode)"))
        self.addressButton.setText(_translate("Receive", "(address)"))
        self.label.setText(_translate("Receive", "Click on address to copy to clipboard"))

