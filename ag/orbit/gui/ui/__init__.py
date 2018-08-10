# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from .. import __version__
from ..qt.main_ui import Ui_Main
from .about import About

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow


class Main(QMainWindow, Ui_Main):

    def __init__(self):
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.menu.setNativeMenuBar(False)
        self.status.showMessage(__version__)

        self.about = About(self)

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        self.about.show()
        self.about.raise_()
        self.about.activateWindow()

