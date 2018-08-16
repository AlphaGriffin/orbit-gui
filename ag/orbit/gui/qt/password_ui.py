# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ag/orbit/gui/qt/password.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Password(object):
    def setupUi(self, Password):
        Password.setObjectName("Password")
        Password.setWindowModality(QtCore.Qt.ApplicationModal)
        Password.resize(282, 131)
        Password.setSizeGripEnabled(True)
        Password.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Password)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Password)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.password = QtWidgets.QLineEdit(Password)
        self.password.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Password)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(Password)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Password)
        QtCore.QMetaObject.connectSlotsByName(Password)

    def retranslateUi(self, Password):
        _translate = QtCore.QCoreApplication.translate
        Password.setWindowTitle(_translate("Password", "Password Required"))
        self.label.setText(_translate("Password", "Please enter your password:"))
        self.pushButton_2.setText(_translate("Password", "Cancel"))
        self.pushButton.setText(_translate("Password", "Decrypt"))

