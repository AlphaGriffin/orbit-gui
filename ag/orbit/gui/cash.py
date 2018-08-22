# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from .qt.cash.receive_ui import Ui_Receive
from .qt.cash.send_ui import Ui_Send
from .qt.cash.confirm_ui import Ui_Confirm

from PyQt5.Qt import QApplication, QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog
from qrcode import QRCode
from PIL.ImageQt import ImageQt
from cashaddress.convert import InvalidAddress
from bitcash.exceptions import InsufficientFunds
from bitcash.network import NetworkAPI
from bitcash.transaction import calc_txid, estimate_tx_fee

from decimal import Decimal


class Refresh(QThread):

    def __init__(self, ui, key):
        QThread.__init__(self, ui)
        self.ui = ui
        self.key = key

    def run(self):
        self.ui.cashUpdated.emit(int(self.key.get_balance()))


class Receive(QDialog, Ui_Receive):

    def __init__(self, parent, address):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.address = address
        self.addressButton.setText(address)

        qr = QRCode()
        qr.add_data(address)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        qimg = ImageQt(img)
        self.qrcode.setPixmap(QPixmap.fromImage(qimg))

    @pyqtSlot()
    def on_addressButton_clicked(self):
        QApplication.clipboard().setText(self.address)

    @pyqtSlot()
    def on_closeButton_clicked(self):
        self.reject()


class Send(QDialog, Ui_Send):
    broadcasted = pyqtSignal(str)

    def __init__(self, parent, key):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.broadcasted.connect(self.on_broadcast)

        self.key = key
        self.validate()

    def validate(self):
        self.sendButton.setEnabled(len(self.address.text()) > 0)

    @pyqtSlot(str)
    def on_address_textEdited(self, text):
        self.validate()

    @pyqtSlot(int)
    def on_maximum_stateChanged(self, state):
        self.amount.setEnabled(state == 0)

    @pyqtSlot(str)
    def on_broadcast(self, txid):
        self.parent.broadcasted.emit(txid)

    @pyqtSlot()
    def on_cancelButton_clicked(self):
        self.reject()

    @pyqtSlot()
    def on_sendButton_clicked(self):
        self.setEnabled(False)
        confirm = Confirm(self, self.key, self.address.text(),
                int(Decimal(self.amount.text()).scaleb(8)) if self.amount.isEnabled() else None,
                int(self.fee.text()))

        if confirm.exec_():
            self.accept()
        else:
            self.setEnabled(True)


class Confirm(QDialog, Ui_Confirm):
    prepared = pyqtSignal(str, int, int)
    invalid = pyqtSignal(str)
    bad_value = pyqtSignal(str)
    broadcast_failed = pyqtSignal(str)
    broadcasted = pyqtSignal(str)

    def __init__(self, parent, key, address, amount, fee):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.key = key
        self.address = address
        self.amount = amount
        self.fee = fee

        self.prepared.connect(self.on_prepared)
        self.invalid.connect(self.on_invalid)
        self.bad_value.connect(self.on_bad_value)
        self.broadcast_failed.connect(self.on_broadcast_failed)
        self.broadcasted.connect(self.on_broadcast)

        self.error.setText('')
        self.to.setText(address)

        self.availableBCH.setText('...')
        self.availableSatoshi.setText('...')

        if amount:
            self.amountBCH.setText(str(Decimal(amount).scaleb(-8)))
            self.amountSatoshi.setText(str(amount))
        else:
            self.amountBCH.setText('...')
            self.amountSatoshi.setText('...')

        self.feeBCH.setText('...')
        self.feeSatoshi.setText('...')

        self.totalBCH.setText('...')
        self.totalSatoshi.setText('...')

        self.confirmButton.setEnabled(False)

        self.status.setText("Preparing transaction...")
        prepare = Prepare(self, key, address, amount, fee)
        prepare.start()

    @pyqtSlot(str, int, int)
    def on_prepared(self, tx, balance, fee):
        self.status.setText('')
        self.tx = tx

        self.availableBCH.setText(str(Decimal(balance).scaleb(-8).normalize()))
        self.availableSatoshi.setText(str(balance))

        self.feeBCH.setText(str(Decimal(fee).scaleb(-8).normalize()))
        self.feeSatoshi.setText(str(fee))

        if self.amount:
            total = self.amount + fee
        else:
            total = balance
            amount = balance - fee
            self.amountBCH.setText(str(Decimal(amount).scaleb(-8).normalize()))
            self.amountSatoshi.setText(str(amount))

        self.totalBCH.setText(str(Decimal(total).scaleb(-8).normalize()))
        self.totalSatoshi.setText(str(total))

        self.confirmButton.setEnabled(True)

    @pyqtSlot(str)
    def on_invalid(self, msg):
        self.status.setText('Error: Invalid Address')
        self.error.setText(msg)

    @pyqtSlot(str)
    def on_bad_value(self, msg):
        self.status.setText('Error: Insufficient Balance')
        self.error.setText(msg)

    @pyqtSlot(str)
    def on_broadcast_failed(self, msg):
        self.status.setText('Error: Broadcast Failed')
        self.error.setText(msg)
        self.confirmButton.setEnabled(True)

    @pyqtSlot(str)
    def on_broadcast(self, txid):
        self.parent.broadcasted.emit(txid)
        self.accept()

    @pyqtSlot()
    def on_cancelButton_clicked(self):
        self.reject()

    @pyqtSlot()
    def on_confirmButton_clicked(self):
        self.confirmButton.setEnabled(False)
        self.error.setText('')
        self.status.setText("Broadcasting...")

        broadcast = Broadcast(self, self.tx)
        broadcast.start()


class Prepare(QThread):

    def __init__(self, ui, key, address, amount, fee):
        QThread.__init__(self, ui)
        self.ui = ui
        self.key = key
        self.address = address
        self.amount = amount
        self.fee = fee

    def run(self):
        try:
            balance = int(self.key.get_balance())
            if balance == 0:
                raise ValueError("Zero balance")

            if self.amount:
                if balance < self.amount:
                    raise ValueError("Amount exceeds available balance")
                outputs = [ (self.address, self.amount, 'satoshi') ]
                tx = self.key.create_transaction(outputs, fee=self.fee)

            else:
                outputs = []
                tx = self.key.create_transaction(outputs, fee=self.fee, leftover=self.address)

            fee = estimate_tx_fee(len(self.key.unspents), len(outputs)+1, self.fee, True)

            self.ui.prepared.emit(tx, balance, fee)

        except InvalidAddress as e:
            self.ui.invalid.emit("{}".format(e))

        except InsufficientFunds as e:
            self.ui.bad_value.emit("{}".format(e))

        except ValueError as e:
            self.ui.bad_value.emit("{}".format(e))


class Broadcast(QThread):

    def __init__(self, ui, tx):
        QThread.__init__(self, ui)
        self.ui = ui
        self.tx = tx

    def run(self):
        try:
            NetworkAPI.broadcast_tx(self.tx)
            self.ui.broadcasted.emit(calc_txid(self.tx))

        except ConnectionError as e:
            self.ui.broadcast_failed.emit("{}".format(e))

