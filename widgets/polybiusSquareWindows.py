# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'polybiusSquareWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from cyphers.polybius_square_cypher import PolybiusSquare


class Ui_PolybiusSquare(object):
    def setupUi(self, PolybiusSquare):
        PolybiusSquare.setObjectName("PolybiusSquare")
        PolybiusSquare.resize(480, 374)
        self.verticalLayoutWidget = QtWidgets.QWidget(PolybiusSquare)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 20, 371, 331))
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.encode = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.encode.setFont(font)
        self.encode.setObjectName("encode")
        self.horizontalLayout.addWidget(self.encode)
        self.method = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.method.setFont(font)
        self.method.setToolTipDuration(-1)
        self.method.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.method.setAutoFillBackground(False)
        self.method.setStyleSheet("")
        self.method.setObjectName("method")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.horizontalLayout.addWidget(self.method)
        self.decode = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decode.setFont(font)
        self.decode.setObjectName("decode")
        self.horizontalLayout.addWidget(self.decode)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.output = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)

        self.retranslateUi(PolybiusSquare)
        QtCore.QMetaObject.connectSlotsByName(PolybiusSquare)

        self.encode.clicked.connect(self.encodeText)
        self.decode.clicked.connect(self.decodeText)

    def encodeText(self):
        plaintext = self.input.toPlainText()
        pol = PolybiusSquare()
        cyphertext = pol.encode(plaintext, self.method.currentText()[-1])
        self.output.setText(cyphertext)

    def decodeText(self):
        cyphertext = self.input.toPlainText()
        pol = PolybiusSquare()
        plaintext = pol.decode(cyphertext, self.method.currentText()[-1])
        self.output.setText(plaintext)

    def retranslateUi(self, PolybiusSquare):
        _translate = QtCore.QCoreApplication.translate
        PolybiusSquare.setWindowTitle(_translate("PolybiusSquare", "Polybius Square"))
        self.label.setText(_translate("PolybiusSquare", "Квадрат Полибия"))
        self.encode.setText(_translate("PolybiusSquare", "Зашифровать"))
        self.method.setItemText(0, _translate("PolybiusSquare", "Метод 1"))
        self.method.setItemText(1, _translate("PolybiusSquare", "Метод 2"))
        self.method.setItemText(2, _translate("PolybiusSquare", "Метод 3"))
        self.decode.setText(_translate("PolybiusSquare", "Расшифровать"))