import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, QTextStream

from widgets.mainWindow import Ui_MainWindow

from resources import breeze_resources


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    file = QFile(":/dark/stylesheet.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())