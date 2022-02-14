# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hillWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from cyphers.hill_cypher import Hill as hill


class Ui_Hill(object):
    def setupUi(self, Hill):
        Hill.setObjectName("Hill")
        Hill.resize(485, 385)
        self.widget = QtWidgets.QWidget(Hill)
        self.widget.setGeometry(QtCore.QRect(37, 30, 411, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cypherName = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cypherName.setFont(font)
        self.cypherName.setAlignment(QtCore.Qt.AlignCenter)
        self.cypherName.setObjectName("cypherName")
        self.verticalLayout.addWidget(self.cypherName)
        self.input = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input.setFont(font)
        self.input.setObjectName("input")
        self.verticalLayout.addWidget(self.input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.encrypt = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.encrypt.setFont(font)
        self.encrypt.setObjectName("encrypt")
        self.horizontalLayout.addWidget(self.encrypt)
        self.decrypt = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decrypt.setFont(font)
        self.decrypt.setObjectName("decrypt")
        self.horizontalLayout.addWidget(self.decrypt)
        self.lang = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lang.setFont(font)
        self.lang.setObjectName("lang")
        self.lang.addItem("")
        self.lang.addItem("")
        self.horizontalLayout.addWidget(self.lang)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.key = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.key.setFont(font)
        self.key.setObjectName("key")
        self.verticalLayout.addWidget(self.key)
        self.output = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)

        self.retranslateUi(Hill)
        QtCore.QMetaObject.connectSlotsByName(Hill)

        self.encrypt.clicked.connect(self.encodeText)
        self.decrypt.clicked.connect(self.decodeText)
        self.key.textChanged.connect(self.updateKeyLang)
        self.lang.currentTextChanged.connect(self.updateKeyLang)

        self.key.setPlaceholderText('Длина ключа - квадрат числа')

        self.hill = hill(self.key.text(), self.lang.currentText())


    def encodeText(self):
        plaintext = self.input.toPlainText()
        cyphertext = self.hill.encode(plaintext)
        self.output.setText(cyphertext)

    def decodeText(self):
        cyphertext = self.input.toPlainText()
        plaintext = self.hill.decode(cyphertext)
        self.output.setText(plaintext)

    def updateKeyLang(self):
        self.hill = hill(self.key.text(), self.lang.currentText())

    def retranslateUi(self, Hill):
        _translate = QtCore.QCoreApplication.translate
        Hill.setWindowTitle(_translate("Hill", "Hill"))
        self.cypherName.setText(_translate("Hill", "Хилл"))
        self.encrypt.setText(_translate("Hill", "Зашифровать"))
        self.decrypt.setText(_translate("Hill", "Расшифровать"))
        self.lang.setItemText(0, _translate("Hill", "ENG"))
        self.lang.setItemText(1, _translate("Hill", "RUS"))