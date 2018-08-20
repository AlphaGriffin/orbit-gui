# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ag/orbit/gui/qt/wallet/unencrypted.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Unencrypted(object):
    def setupUi(self, Unencrypted):
        Unencrypted.setObjectName("Unencrypted")
        Unencrypted.setWindowModality(QtCore.Qt.WindowModal)
        Unencrypted.resize(418, 256)
        Unencrypted.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Unencrypted)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(Unencrypted)
        self.cancelButton.setDefault(True)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Unencrypted)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Unencrypted)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.acceptButton = QtWidgets.QPushButton(Unencrypted)
        self.acceptButton.setObjectName("acceptButton")
        self.horizontalLayout_2.addWidget(self.acceptButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Unencrypted)
        QtCore.QMetaObject.connectSlotsByName(Unencrypted)

    def retranslateUi(self, Unencrypted):
        _translate = QtCore.QCoreApplication.translate
        Unencrypted.setWindowTitle(_translate("Unencrypted", "No Encryption"))
        self.cancelButton.setText(_translate("Unencrypted", "Cancel"))
        self.label.setText(_translate("Unencrypted", "Warning!"))
        self.label_2.setText(_translate("Unencrypted", "You are about to save your wallet without encryption. This is not secure!"))
        self.acceptButton.setText(_translate("Unencrypted", "Accept"))

