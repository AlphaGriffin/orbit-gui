# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from .. import __version__
from ..qt.about_ui import Ui_About

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog


class About(QDialog, Ui_About):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent

        self.version.setText(__version__)

