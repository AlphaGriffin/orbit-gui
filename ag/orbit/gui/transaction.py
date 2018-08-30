# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.gui.qt.transaction_ui import Ui_Transaction

from PyQt5.Qt import QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog


class Transaction(QDialog, Ui_Transaction):

    def __init__(self, parent, txid):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.txid = txid
        self.txidButton.setText(txid)

    @pyqtSlot()
    def on_txidButton_clicked(self):
        QApplication.clipboard().setText(self.txid)

    @pyqtSlot()
    def on_closeButton_clicked(self):
        self.reject()

