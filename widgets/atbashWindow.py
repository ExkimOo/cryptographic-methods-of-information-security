# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atbashWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from cyphers.atbash_cypher import Atbash


class Ui_Atbash(object):
    def setupUi(self, Atbash):
        Atbash.setObjectName("Atbash")
        Atbash.resize(485, 379)
        self.verticalLayoutWidget = QtWidgets.QWidget(Atbash)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 411, 351))
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
        self.input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input.setFont(font)
        self.input.setObjectName("input")
        self.verticalLayout.addWidget(self.input)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.encode = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.encode.setFont(font)
        self.encode.setObjectName("encode")
        self.horizontalLayout_2.addWidget(self.encode)
        self.decode = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decode.setFont(font)
        self.decode.setObjectName("decode")
        self.horizontalLayout_2.addWidget(self.decode)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.output = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)

        self.retranslateUi(Atbash)
        QtCore.QMetaObject.connectSlotsByName(Atbash)

        self.encode.clicked.connect(self.encodeText)
        self.decode.clicked.connect(self.decodeText)

    def encodeText(self):
        plaintext = self.input.toPlainText()
        atb = Atbash()
        cyphertext = atb.encode(plaintext)
        self.output.setText(cyphertext)

    def decodeText(self):
        cyphertext = self.input.toPlainText()
        atb = Atbash()
        plaintext = atb.decode(cyphertext)
        self.output.setText(plaintext)

    def retranslateUi(self, Atbash):
        _translate = QtCore.QCoreApplication.translate
        Atbash.setWindowTitle(_translate("Atbash", "Dialog"))
        self.label.setText(_translate("Atbash", "Атбаш"))
        self.encode.setText(_translate("Atbash", "Зашифровать"))
        self.decode.setText(_translate("Atbash", "Расшифровать"))