# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from .qt.cash.receive_ui import Ui_Receive
from .qt.cash.send_ui import Ui_Send

from PyQt5.Qt import QApplication, QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog
from qrcode import QRCode
from PIL.ImageQt import ImageQt


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

    def __init__(self, parent, key):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.key = key

    @pyqtSlot()
    def on_cancelButton_clicked(self):
        self.reject()

