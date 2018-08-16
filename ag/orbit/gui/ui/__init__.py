# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from .. import __version__
from ..qt.main_ui import Ui_Main
from .about import About
from .password import Password

from ag.orbit.wallet import list as get_wallet_list

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
        self.refresh_wallets()

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        self.about.show()
        self.about.raise_()
        self.about.activateWindow()

    def refresh_wallets(self):
        self.wallets.clear()
        wallets = get_wallet_list()

        if len(wallets) > 0:
            self.wallets.addItem("--choose a wallet--")
        else:
            self.wallets.addItem("--no wallets found; use the wallet menu--")

        for wallet in wallets:
            self.wallets.addItem(wallet)

        self.wallets.setEnabled(len(wallets) > 0)

    @pyqtSlot(int)
    def on_wallets_currentIndexChanged(self, index):
        #self.on_actionClose_triggered()

        if index > 0:
            password = Password(self)
            password.show()
            password.raise_()
            password.activateWindow()

    @pyqtSlot()
    def on_actionClose_triggered(self):
        self.wallet = None
        self.refresh_wallets()

