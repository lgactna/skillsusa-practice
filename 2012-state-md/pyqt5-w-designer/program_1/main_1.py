"""Program 1: PyQt5+designer used."""

import sys
from PyQt5 import QtWidgets
from program_1 import Ui_MainWindow

class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window. Instantiated once."""

    def __init__(self):
        """Initialize and connect signals/slots."""
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        #Hide the "other screens"
        self.first_output_box.hide()
        self.final_output_box.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = ApplicationWindow()
    w.show()

    sys.exit(app.exec_())
