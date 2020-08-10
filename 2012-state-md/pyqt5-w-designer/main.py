#!/usr/bin/python

#imports
import sys
from PyQt5 import QtWidgets

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #self.setupUi(self)
        self.setWindowTitle("E")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = ApplicationWindow()
    w.show()

    sys.exit(app.exec_())
