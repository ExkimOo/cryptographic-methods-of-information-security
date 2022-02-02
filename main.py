import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from widgets.mainWindow import Ui_MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    with open(r'D:\Projects\from school\cryptographic-methods\resources\styles.stylesheet', 'r') as f:
        styleData = f.read()
    app.setStyleSheet(styleData)

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())