# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ag/orbit/gui/qt/main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(633, 577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(24, 24))
        self.label_5.setMaximumSize(QtCore.QSize(24, 24))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icons/logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.wallets = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wallets.sizePolicy().hasHeightForWidth())
        self.wallets.setSizePolicy(sizePolicy)
        self.wallets.setObjectName("wallets")
        self.horizontalLayout.addWidget(self.wallets)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.main = QtWidgets.QStackedWidget(self.centralwidget)
        self.main.setObjectName("main")
        self.splash = QtWidgets.QWidget()
        self.splash.setObjectName("splash")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.splash)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.splash)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.splash)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.splash)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.main.addWidget(self.splash)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.page_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.refreshCashButton = QtWidgets.QPushButton(self.tab)
        self.refreshCashButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshCashButton.setIcon(icon1)
        self.refreshCashButton.setAutoDefault(True)
        self.refreshCashButton.setDefault(True)
        self.refreshCashButton.setObjectName("refreshCashButton")
        self.horizontalLayout_3.addWidget(self.refreshCashButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.bch = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bch.setFont(font)
        self.bch.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bch.setObjectName("bch")
        self.gridLayout.addWidget(self.bch, 0, 0, 1, 1)
        self.satoshi = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.satoshi.setFont(font)
        self.satoshi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.satoshi.setObjectName("satoshi")
        self.gridLayout.addWidget(self.satoshi, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.receiveCashButton = QtWidgets.QPushButton(self.tab)
        self.receiveCashButton.setObjectName("receiveCashButton")
        self.horizontalLayout_2.addWidget(self.receiveCashButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.sendCashButton = QtWidgets.QPushButton(self.tab)
        self.sendCashButton.setObjectName("sendCashButton")
        self.horizontalLayout_2.addWidget(self.sendCashButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.main.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.main)
        self.error = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setStyleSheet("color: red")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.verticalLayout.addWidget(self.error)
        Main.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(Main)
        self.menu.setGeometry(QtCore.QRect(0, 0, 633, 22))
        self.menu.setObjectName("menu")
        self.menuFile = QtWidgets.QMenu(self.menu)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menu)
        self.menuHelp.setObjectName("menuHelp")
        self.menuWallet = QtWidgets.QMenu(self.menu)
        self.menuWallet.setObjectName("menuWallet")
        self.menuNetwork = QtWidgets.QMenu(self.menu)
        self.menuNetwork.setObjectName("menuNetwork")
        self.menuBitCash = QtWidgets.QMenu(self.menuNetwork)
        self.menuBitCash.setObjectName("menuBitCash")
        Main.setMenuBar(self.menu)
        self.status = QtWidgets.QStatusBar(Main)
        self.status.setObjectName("status")
        Main.setStatusBar(self.status)
        self.actionQuit = QtWidgets.QAction(Main)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(Main)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew = QtWidgets.QAction(Main)
        self.actionNew.setObjectName("actionNew")
        self.actionImport = QtWidgets.QAction(Main)
        self.actionImport.setObjectName("actionImport")
        self.actionRename = QtWidgets.QAction(Main)
        self.actionRename.setObjectName("actionRename")
        self.actionShow_Key = QtWidgets.QAction(Main)
        self.actionShow_Key.setObjectName("actionShow_Key")
        self.actionRemove = QtWidgets.QAction(Main)
        self.actionRemove.setObjectName("actionRemove")
        self.actionClose = QtWidgets.QAction(Main)
        self.actionClose.setObjectName("actionClose")
        self.actionSet_Password = QtWidgets.QAction(Main)
        self.actionSet_Password.setObjectName("actionSet_Password")
        self.actionBitPay = QtWidgets.QAction(Main)
        self.actionBitPay.setCheckable(True)
        self.actionBitPay.setChecked(True)
        self.actionBitPay.setEnabled(False)
        self.actionBitPay.setObjectName("actionBitPay")
        self.actionBlockDozer = QtWidgets.QAction(Main)
        self.actionBlockDozer.setCheckable(True)
        self.actionBlockDozer.setChecked(True)
        self.actionBlockDozer.setEnabled(False)
        self.actionBlockDozer.setObjectName("actionBlockDozer")
        self.actionPeers = QtWidgets.QAction(Main)
        self.actionPeers.setEnabled(False)
        self.actionPeers.setObjectName("actionPeers")
        self.actionPool = QtWidgets.QAction(Main)
        self.actionPool.setEnabled(False)
        self.actionPool.setObjectName("actionPool")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuWallet.addAction(self.actionNew)
        self.menuWallet.addAction(self.actionImport)
        self.menuWallet.addSeparator()
        self.menuWallet.addAction(self.actionRename)
        self.menuWallet.addAction(self.actionSet_Password)
        self.menuWallet.addAction(self.actionClose)
        self.menuWallet.addSeparator()
        self.menuWallet.addAction(self.actionShow_Key)
        self.menuWallet.addSeparator()
        self.menuWallet.addAction(self.actionRemove)
        self.menuBitCash.addAction(self.actionBitPay)
        self.menuBitCash.addAction(self.actionBlockDozer)
        self.menuNetwork.addAction(self.menuBitCash.menuAction())
        self.menuNetwork.addAction(self.actionPeers)
        self.menuNetwork.addAction(self.actionPool)
        self.menu.addAction(self.menuFile.menuAction())
        self.menu.addAction(self.menuWallet.menuAction())
        self.menu.addAction(self.menuNetwork.menuAction())
        self.menu.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Main)
        self.main.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(Main.close)
        QtCore.QMetaObject.connectSlotsByName(Main)
        Main.setTabOrder(self.refreshCashButton, self.tabWidget)
        Main.setTabOrder(self.tabWidget, self.receiveCashButton)
        Main.setTabOrder(self.receiveCashButton, self.pushButton_2)
        Main.setTabOrder(self.pushButton_2, self.sendCashButton)
        Main.setTabOrder(self.sendCashButton, self.wallets)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "ORBIT Wallet"))
        self.label_3.setText(_translate("Main", "Wallet:"))
        self.label_4.setText(_translate("Main", "ORBIT Bitcoin Cash"))
        self.label.setText(_translate("Main", "Open a wallet to begin"))
        self.label_6.setText(_translate("Main", "Bitcoin Cash"))
        self.groupBox.setTitle(_translate("Main", "Balance"))
        self.label_8.setText(_translate("Main", "BCH"))
        self.bch.setText(_translate("Main", "(bch)"))
        self.satoshi.setText(_translate("Main", "(satoshi)"))
        self.label_9.setText(_translate("Main", "satoshi"))
        self.receiveCashButton.setText(_translate("Main", "Receive..."))
        self.pushButton_2.setText(_translate("Main", "Transfer..."))
        self.sendCashButton.setText(_translate("Main", "Send..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Main", "Cash"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Main", "Tokens"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Main", "Crowd Sales"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Main", "Free Faucets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Main", "Admin"))
        self.error.setText(_translate("Main", "(error)"))
        self.menuFile.setTitle(_translate("Main", "&File"))
        self.menuHelp.setTitle(_translate("Main", "&Help"))
        self.menuWallet.setTitle(_translate("Main", "&Wallet"))
        self.menuNetwork.setTitle(_translate("Main", "Network"))
        self.menuBitCash.setTitle(_translate("Main", "BitCash"))
        self.actionQuit.setText(_translate("Main", "&Quit"))
        self.actionQuit.setShortcut(_translate("Main", "Alt+F4"))
        self.actionAbout.setText(_translate("Main", "&About"))
        self.actionNew.setText(_translate("Main", "&New..."))
        self.actionImport.setText(_translate("Main", "&Import..."))
        self.actionRename.setText(_translate("Main", "&Rename..."))
        self.actionShow_Key.setText(_translate("Main", "Show &Private Key"))
        self.actionRemove.setText(_translate("Main", "&Delete..."))
        self.actionClose.setText(_translate("Main", "&Close"))
        self.actionSet_Password.setText(_translate("Main", "&Set Password..."))
        self.actionBitPay.setText(_translate("Main", "BitPay"))
        self.actionBlockDozer.setText(_translate("Main", "BlockDozer"))
        self.actionPeers.setText(_translate("Main", "Peers"))
        self.actionPool.setText(_translate("Main", "Pool..."))

from . import icons_rc
from . import images_rc
