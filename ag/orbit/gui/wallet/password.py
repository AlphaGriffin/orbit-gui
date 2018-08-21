# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ..qt.wallet.password_ui import Ui_Password

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog


class Password(QDialog, Ui_Password):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.decryptButton.setEnabled(False)

    @pyqtSlot()
    def on_cancelButton_clicked(self):
        self.reject()

    @pyqtSlot(str)
    def on_password_textEdited(self, text):
        self.decryptButton.setEnabled(len(text) > 0)

    def on_decryptButton_clicked(self):
        self.accept()

