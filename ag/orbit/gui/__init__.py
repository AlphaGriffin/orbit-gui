# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

"""Graphical User Interface for ORBIT

This is a Qt GUI wallet following the ORBIT specification
defined at https://github.com/AlphaGriffin/orbit

.. module:: ag.orbit.gui
   :platform: Unix
   :synopsis: Graphical User Interface for ORBIT
.. moduleauthor:: Shawn Wilson <lannocc@alphagriffin.com>
"""

from .__version__ import __version__
print ("ORBIT Graphical User Interface version %s" % (__version__))

from ag.orbit.gui.qt.main_ui import Ui_Main
from ag.orbit.gui.about import About
from ag.orbit.gui.transaction import Transaction
from ag.orbit.gui.wallet.password import Password
from ag.orbit.gui.wallet.key import ShowKey
from ag.orbit.gui.wallet.create import NewWallet
from ag.orbit.gui import cash

from ag.orbit.wallet import list as list_wallets, path, access

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from decimal import Decimal


class Main(QMainWindow, Ui_Main):
    cashUpdated = pyqtSignal(int)
    broadcasted = pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.menu.setNativeMenuBar(False)
        self.status.showMessage(__version__)

        self.about = About(self)

        self.cashUpdated.connect(self.set_cash_balance)
        self.broadcasted.connect(self.on_broadcast)

        self.wallet = None
        self.reload_wallets()

    def refresh(self):
        self.actionImport.setEnabled(False) # FIXME
        self.actionRename.setEnabled(False) # FIXME
        self.actionSet_Password.setEnabled(False) # FIXME
        self.actionClose.setEnabled(self.wallet is not None)
        self.actionShow_Key.setEnabled(self.wallet is not None)
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

    @pyqtSlot()
    def on_actionShow_Key_triggered(self):
        key = ShowKey(self, self.wallet)
        key.show()
        key.raise_()
        key.activateWindow()

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
                self.on_refreshCashButton_clicked()

            except ValueError as e:
                self.error.setText("{}".format(e))
                self.wallets.setCurrentIndex(0)

        self.refresh()

    @pyqtSlot()
    def on_refreshCashButton_clicked(self):
        self.refreshCashButton.setEnabled(False)
        self.bch.setText("...")
        self.satoshi.setText("...")
        cash.Refresh(self, self.wallet).start()

    @pyqtSlot()
    def on_receiveCashButton_clicked(self):
        receive = cash.Receive(self, self.wallet.address)
        receive.show()
        receive.raise_()
        receive.activateWindow()

    @pyqtSlot()
    def on_sendCashButton_clicked(self):
        send = cash.Send(self, self.wallet)
        send.show()
        send.raise_()
        send.activateWindow()

    @pyqtSlot(int)
    def set_cash_balance(self, satoshi):
        self.bch.setText(str(Decimal(satoshi).scaleb(-8).normalize()))
        self.satoshi.setText(str(satoshi))
        self.refreshCashButton.setEnabled(True)

    @pyqtSlot()
    def on_actionClose_triggered(self):
        self.wallet = None
        self.wallets.setCurrentIndex(0)

    @pyqtSlot(str)
    def on_broadcast(self, txid):
        tx = Transaction(self, txid)
        tx.show()
        tx.raise_()
        tx.activateWindow()

        self.on_refreshCashButton_clicked()

