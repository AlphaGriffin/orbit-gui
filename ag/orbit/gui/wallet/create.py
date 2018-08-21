# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ..qt.wallet.create_ui import Ui_NewWallet
from ..qt.wallet.unencrypted_ui import Ui_Unencrypted

from ag.orbit.wallet import path, create

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog


class NewWallet(QDialog, Ui_NewWallet):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.validate()

    @pyqtSlot()
    def on_cancelButton_clicked(self):
        self.reject()

    @pyqtSlot(str)
    def on_name_textEdited(self, text):
        self.validate()

    @pyqtSlot(str)
    def on_password_textEdited(self, text):
        self.validate()

    @pyqtSlot(str)
    def on_passwordVerify_textEdited(self, text):
        self.validate()

    def validate(self):
        self.error.setText("")
        self.saveButton.setEnabled(len(self.name.text()) > 0 and
                self.password.text() == self.passwordVerify.text())

    @pyqtSlot()
    def on_saveButton_clicked(self):
        self.error.setText("")
        name = self.name.text()

        try:
            wpath = path(name)

            def get_password():
                return self.password.text()

            def warning():
                if not Unencrypted(self).exec_():
                    raise ValueError("User abort")

            create(wpath, get_password=get_password, unencrypted_warning=warning)
            
            self.parent.reload_wallets(name)
            self.accept()

        except ValueError as e:
            self.error.setText("{}".format(e))


class Unencrypted(QDialog, Ui_Unencrypted):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

    @pyqtSlot()
    def on_cancelButton_clicked(self):
        self.reject()

    @pyqtSlot()
    def on_acceptButton_clicked(self):
        self.accept()

