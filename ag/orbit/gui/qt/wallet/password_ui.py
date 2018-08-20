# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ag/orbit/gui/qt/wallet/password.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Password(object):
    def setupUi(self, Password):
        Password.setObjectName("Password")
        Password.setWindowModality(QtCore.Qt.WindowModal)
        Password.resize(282, 196)
        Password.setSizeGripEnabled(True)
        Password.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Password)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancelButton = QtWidgets.QPushButton(Password)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Password)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.password = QtWidgets.QLineEdit(Password)
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.decryptButton = QtWidgets.QPushButton(Password)
        self.decryptButton.setDefault(True)
        self.decryptButton.setObjectName("decryptButton")
        self.horizontalLayout.addWidget(self.decryptButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Password)
        QtCore.QMetaObject.connectSlotsByName(Password)
        Password.setTabOrder(self.password, self.decryptButton)
        Password.setTabOrder(self.decryptButton, self.cancelButton)

    def retranslateUi(self, Password):
        _translate = QtCore.QCoreApplication.translate
        Password.setWindowTitle(_translate("Password", "Password Required"))
        self.cancelButton.setText(_translate("Password", "Cancel"))
        self.label.setText(_translate("Password", "Please enter your password:"))
        self.decryptButton.setText(_translate("Password", "Decrypt"))

