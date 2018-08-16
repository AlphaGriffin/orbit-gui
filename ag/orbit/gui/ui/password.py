# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from .. import __version__
from ..qt.password_ui import Ui_Password

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog


class Password(QDialog, Ui_Password):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

