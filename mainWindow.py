# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from widgets.albertiWindow import Ui_Alberti
from widgets.atbashWindow import Ui_Atbash
from widgets.cardanoGrilleWindow import Ui_CardanoGrille
from widgets.ceasarWindow import Ui_Ceasar
from widgets.gronsfeldWindow import Ui_Gronsfeld
from widgets.hillWindow import Ui_Hill
from widgets.playfairWindow import Ui_Playfair
from widgets.polybiusSquareWindows import Ui_PolybiusSquare
from widgets.richelieuWindow import Ui_Richelieu
from widgets.scytaleWindow import Ui_Scytale
from widgets.vernamWindow import Ui_Vernam
from widgets.vigenereWindow import Ui_Vigenere
from utils.freq_cryptanalysis.freqCryptanalysisWindow import Ui_FrequencyCryptanalysis
from widgets.xorWindow import Ui_XOR
from widgets.desWindow import Ui_DES


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 20, 691, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cyphersList = QtWidgets.QListWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cyphersList.setFont(font)
        self.cyphersList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cyphersList.setAutoFillBackground(False)
        self.cyphersList.setStyleSheet("")
        self.cyphersList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.cyphersList.setViewMode(QtWidgets.QListView.ListMode)
        self.cyphersList.setItemAlignment(QtCore.Qt.AlignCenter)
        self.cyphersList.setObjectName("cyphersList")
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cyphersList.addItem(item)
        self.verticalLayout.addWidget(self.cyphersList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.cyphersList.itemDoubleClicked.connect(self.doubleClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def doubleClicked(self, item):
        cypher = item.text().split()[0]
        if cypher == 'Atbash':
            self.atbashDialog()
        elif cypher == 'Scytale':
            self.scytaleDialog()
        elif cypher == 'Polybius':
            self.polybiusSquareDialog()
        elif cypher == 'Ceasar':
            self.ceasarSquareDialog()
        elif cypher == 'Cardano':
            self.cardanoGrilleDialog()
        elif cypher == 'Richelieu':
            self.richelieuDialog()
        elif cypher == 'Playfair':
            self.playfairDialog()
        elif cypher == 'Vigenere':
            self.vigenereDialog()
        elif cypher == 'Gronsfeld':
            self.gronsfeldDialog()
        elif cypher == 'Hill':
            self.hillDialog()
        elif cypher == 'Vernam':
            self.vernamDialog()
        elif cypher == 'Alberti\'s':
            self.albertiDialog()
        elif cypher == 'Frequency':
            self.frequencyCryptanalysisDialog()
        elif cypher == 'XOR':
            self.xorDialog()
        elif cypher == 'DES':
            self.desDialog()

    def atbashDialog(self):
        self.atbash = QtWidgets.QMainWindow()
        self.ui = Ui_Atbash()
        self.ui.setupUi(self.atbash)
        self.atbash.show()

    def scytaleDialog(self):
        self.scytale = QtWidgets.QMainWindow()
        self.ui = Ui_Scytale()
        self.ui.setupUi(self.scytale)
        self.scytale.show()

    def polybiusSquareDialog(self):
        self.polybiusSquare = QtWidgets.QMainWindow()
        self.ui = Ui_PolybiusSquare()
        self.ui.setupUi(self.polybiusSquare)
        self.polybiusSquare.show()

    def ceasarSquareDialog(self):
        self.ceasar = QtWidgets.QMainWindow()
        self.ui = Ui_Ceasar()
        self.ui.setupUi(self.ceasar)
        self.ceasar.show()

    def cardanoGrilleDialog(self):
        self.cardano = QtWidgets.QMainWindow()
        self.ui = Ui_CardanoGrille()
        self.ui.setupUi(self.cardano)
        self.cardano.show()

    def richelieuDialog(self):
        self.richelieu = QtWidgets.QMainWindow()
        self.ui = Ui_Richelieu()
        self.ui.setupUi(self.richelieu)
        self.richelieu.show()

    def playfairDialog(self):
        self.playfair = QtWidgets.QMainWindow()
        self.ui = Ui_Playfair()
        self.ui.setupUi(self.playfair)
        self.playfair.show()

    def vigenereDialog(self):
        self.vigenere = QtWidgets.QMainWindow()
        self.ui = Ui_Vigenere()
        self.ui.setupUi(self.vigenere)
        self.vigenere.show()

    def gronsfeldDialog(self):
        self.gronsfeld = QtWidgets.QMainWindow()
        self.ui = Ui_Gronsfeld()
        self.ui.setupUi(self.gronsfeld)
        self.gronsfeld.show()

    def hillDialog(self):
        self.hill = QtWidgets.QMainWindow()
        self.ui = Ui_Hill()
        self.ui.setupUi(self.hill)
        self.hill.show()

    def vernamDialog(self):
        self.vernam = QtWidgets.QMainWindow()
        self.ui = Ui_Vernam()
        self.ui.setupUi(self.vernam)
        self.vernam.show()

    def albertiDialog(self):
        self.alberti = QtWidgets.QMainWindow()
        self.ui = Ui_Alberti()
        self.ui.setupUi(self.alberti)
        self.alberti.show()

    def frequencyCryptanalysisDialog(self):
        self.freq = QtWidgets.QMainWindow()
        self.ui = Ui_FrequencyCryptanalysis()
        self.ui.setupUi(self.freq)
        self.freq.show()

    def xorDialog(self):
        self.xor = QtWidgets.QMainWindow()
        self.ui = Ui_XOR()
        self.ui.setupUi(self.xor)
        self.xor.show()

    def desDialog(self):
        self.des = QtWidgets.QMainWindow()
        self.ui = Ui_DES()
        self.ui.setupUi(self.des)
        self.des.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cryptographic Methods of Information Security"))
        self.label.setText(_translate("MainWindow", "Метод:"))
        __sortingEnabled = self.cyphersList.isSortingEnabled()
        self.cyphersList.setSortingEnabled(False)
        item = self.cyphersList.item(0)
        item.setText(_translate("MainWindow", "Atbash cypher"))
        item = self.cyphersList.item(1)
        item.setText(_translate("MainWindow", "Scytale cypher"))
        item = self.cyphersList.item(2)
        item.setText(_translate("MainWindow", "Polybius Square cypher"))
        item = self.cyphersList.item(3)
        item.setText(_translate("MainWindow", "Ceasar cypher"))
        item = self.cyphersList.item(4)
        item.setText(_translate("MainWindow", "Cardano cypher"))
        item = self.cyphersList.item(5)
        item.setText(_translate("MainWindow", "Richelieu cypher"))
        item = self.cyphersList.item(6)
        item.setText(_translate("MainWindow", "Alberti\'s Disk cypher"))
        item = self.cyphersList.item(7)
        item.setText(_translate("MainWindow", "Gronsfeld cypher"))
        item = self.cyphersList.item(8)
        item.setText(_translate("MainWindow", "Vigenere cypher"))
        item = self.cyphersList.item(9)
        item.setText(_translate("MainWindow", "Playfair cypher"))
        item = self.cyphersList.item(10)
        item.setText(_translate("MainWindow", "Hill cypher"))
        item = self.cyphersList.item(11)
        item.setText(_translate("MainWindow", "Vernam cypher"))
        item = self.cyphersList.item(12)
        item.setText(_translate("MainWindow", "Frequency Cryptanalysis"))
        item = self.cyphersList.item(13)
        item.setText(_translate("MainWindow", "XOR cypher"))
        item = self.cyphersList.item(14)
        item.setText(_translate("MainWindow", "DES cypher"))
        self.cyphersList.setSortingEnabled(__sortingEnabled)
