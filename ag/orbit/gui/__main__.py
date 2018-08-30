# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.gui import Main

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import sys
import signal

QApplication.setAttribute(Qt.AA_X11InitThreads)
app = QApplication(sys.argv)

win = Main()
win.show()

try:
    # override signals to allow for Ctr+C in command line
    try:
        signal.siginterrupt(signal.SIGCHLD, False)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    except AttributeError:
        pass

    # this blocks until application exit
    sys.exit(app.exec_())

except KeyboardInterrupt:
    pass

