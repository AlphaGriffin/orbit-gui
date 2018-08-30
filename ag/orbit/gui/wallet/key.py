# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.gui.qt.wallet.key_ui import Ui_ShowKey

from PyQt5.Qt import QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog


class ShowKey(QDialog, Ui_ShowKey):

    def __init__(self, parent, key):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.key = key

        self.wifButton.setText(key.to_wif())

    @pyqtSlot()
    def on_wifButton_clicked(self):
        QApplication.clipboard().setText(self.key.to_wif())

    @pyqtSlot()
    def on_closeButton_clicked(self):
        self.reject()

