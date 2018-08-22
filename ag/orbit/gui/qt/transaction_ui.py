# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ag/orbit/gui/qt/transaction.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Transaction(object):
    def setupUi(self, Transaction):
        Transaction.setObjectName("Transaction")
        Transaction.resize(579, 270)
        Transaction.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Transaction)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QPushButton(Transaction)
        self.closeButton.setDefault(True)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.groupBox = QtWidgets.QGroupBox(Transaction)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txidButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.txidButton.setFont(font)
        self.txidButton.setFlat(True)
        self.txidButton.setObjectName("txidButton")
        self.verticalLayout.addWidget(self.txidButton)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Transaction)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.retranslateUi(Transaction)
        QtCore.QMetaObject.connectSlotsByName(Transaction)

    def retranslateUi(self, Transaction):
        _translate = QtCore.QCoreApplication.translate
        Transaction.setWindowTitle(_translate("Transaction", "Transaction"))
        self.closeButton.setText(_translate("Transaction", "Close"))
        self.groupBox.setTitle(_translate("Transaction", "Transaction"))
        self.txidButton.setText(_translate("Transaction", "(txid)"))
        self.label.setText(_translate("Transaction", "Click on transaction to copy to clipboard"))

