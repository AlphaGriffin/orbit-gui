# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ag/orbit/gui/qt/cash/send.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Send(object):
    def setupUi(self, Send):
        Send.setObjectName("Send")
        Send.resize(581, 397)
        Send.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Send)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(Send)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(Send)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.address = QtWidgets.QLineEdit(self.groupBox)
        self.address.setObjectName("address")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.address)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.amount = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.amount.setProperty("showGroupSeparator", True)
        self.amount.setDecimals(8)
        self.amount.setMaximum(99999999999999.0)
        self.amount.setSingleStep(0.1)
        self.amount.setObjectName("amount")
        self.horizontalLayout_4.addWidget(self.amount)
        self.maximum = QtWidgets.QCheckBox(self.groupBox)
        self.maximum.setObjectName("maximum")
        self.horizontalLayout_4.addWidget(self.maximum)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox_2 = QtWidgets.QGroupBox(Send)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.fee = QtWidgets.QSpinBox(self.groupBox_2)
        self.fee.setProperty("showGroupSeparator", True)
        self.fee.setMinimum(1)
        self.fee.setMaximum(9999)
        self.fee.setObjectName("fee")
        self.horizontalLayout_3.addWidget(self.fee)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.sendButton = QtWidgets.QPushButton(Send)
        self.sendButton.setDefault(True)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout_2.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Send)
        QtCore.QMetaObject.connectSlotsByName(Send)
        Send.setTabOrder(self.address, self.amount)
        Send.setTabOrder(self.amount, self.maximum)
        Send.setTabOrder(self.maximum, self.fee)
        Send.setTabOrder(self.fee, self.sendButton)
        Send.setTabOrder(self.sendButton, self.cancelButton)

    def retranslateUi(self, Send):
        _translate = QtCore.QCoreApplication.translate
        Send.setWindowTitle(_translate("Send", "Send Bitcoin Cash"))
        self.cancelButton.setText(_translate("Send", "Cancel"))
        self.groupBox.setTitle(_translate("Send", "Send Bitcoin Cash"))
        self.label.setText(_translate("Send", "To Address:"))
        self.maximum.setText(_translate("Send", "Send Max"))
        self.label_2.setText(_translate("Send", "BCH Amount:"))
        self.groupBox_2.setTitle(_translate("Send", "Network Fee"))
        self.label_4.setText(_translate("Send", "Satoshi per byte:"))
        self.sendButton.setText(_translate("Send", "Send"))

