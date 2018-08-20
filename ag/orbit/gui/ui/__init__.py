# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from .. import __version__
from ..qt.main_ui import Ui_Main
from .about import About
from .wallet.password import Password
from .wallet.create import NewWallet

from ag.orbit.wallet import list as list_wallets, path, access

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow


class Main(QMainWindow, Ui_Main):

    def __init__(self):
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.menu.setNativeMenuBar(False)
        self.status.showMessage(__version__)

        self.about = About(self)

        self.wallet = None
        self.reload_wallets()

    def refresh(self):
        self.actionImport.setEnabled(False) # FIXME
        self.actionRename.setEnabled(False) # FIXME
        self.actionSet_Password.setEnabled(False) # FIXME
        self.actionClose.setEnabled(self.wallet is not None)
        self.actionShow_Key.setEnabled(False) # FIXME
        self.actionRemove.setEnabled(False) # FIXME

        self.main.setCurrentIndex(1 if self.wallet else 0)

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        self.about.show()
        self.about.raise_()
        self.about.activateWindow()

    @pyqtSlot()
    def on_actionNew_triggered(self):
        create = NewWallet(self)
        create.show()
        create.raise_()
        create.activateWindow()

    def reload_wallets(self, name=None):
        self.error.setText("")

        if name is None and self.wallets.currentIndex() > 0:
            name = self.wallets.currentItem()

        self.wallets.clear()
        wallets = list_wallets()
        wallets.sort()

        if len(wallets) > 0:
            self.wallets.addItem("--choose a wallet--")
        else:
            self.wallets.addItem("--no wallets found; use the wallet menu--")

        index = 0
        for i, wallet in enumerate(wallets):
            self.wallets.addItem(wallet)
            if name == wallet:
                index = i + 1

        self.wallets.setCurrentIndex(index)
        self.wallets.setEnabled(len(wallets) > 0)

    @pyqtSlot(int)
    def on_wallets_currentIndexChanged(self, index):
        if self.wallet:
            self.wallet = None

        if index > 0:
            self.error.setText("")

            def password():
                password = Password(self)
                if password.exec_():
                    return password.password.text()
                else:
                    raise ValueError("User abort")

            try:
                wpath = path(self.wallets.currentText())
                self.wallet = access(wpath, get_password=password)

            except ValueError as e:
                self.error.setText("{}".format(e))
                self.wallets.setCurrentIndex(0)

        self.refresh()

    @pyqtSlot()
    def on_actionClose_triggered(self):
        self.wallet = None
        self.wallets.setCurrentIndex(0)

