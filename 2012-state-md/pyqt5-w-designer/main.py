#!/usr/bin/python

#yes i used the online qt docs for this since i couldn't figure out how to compile them lol

#imports
import sys
from PyQt5 import QtWidgets
from program_2 import Ui_MainWindow

class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window. Instantiated once."""
    def __init__(self):
        """Initialization and connection of signals/slots"""
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        #Since the default number of pizzas is 1, we'll default to disabling both of the second group boxes
        self.pizza_two_groupbox_1.setEnabled(False)
        self.pizza_two_groupbox_2.setEnabled(False)
        
        #We hide the "second screen" until the user wants it
        self.screen_2_box.hide()

        #While we can easily determine what "screen" is visible via isVisible(), this
        #instance attribute provides clarity
        self.current_screen = 1

        #Here we create several QButtonGroups to simplify obtaining the various radio button states
        #We can then create arrays as necessary to pass to business logic functions
        #...

        #Enable or disable the second group box depending on what the user selects
        #Listen for changes to the combobox to do so
        self.pizzas_ordering_combobox.currentIndexChanged.connect(self.update_groupboxes)

        #Bottom buttons
        self.exit_button.clicked.connect(self.exit)
        self.calculate_button.clicked.connect(self.calculate_and_swap)
        self.clear_button.clicked.connect(self.clear_inputs)

    def exit(self):
        #note that closeEvent is intercepted with a dialog
        self.close()
    def calculate_and_swap(self):
        if self.current_screen == 1:
            self.screen_1_box.hide()
            self.screen_2_box.show()
            self.current_screen = 2
            self.calculate_button.setText("Return to Order Selection")
            #We'll prevent the customer from changing their name or pizza count after calculation
            #By disabling these two widgets, they *must* return to the first screen to change these
            self.customer_name_edit.setEnabled(False)
            self.pizzas_ordering_combobox.setEnabled(False)
            #Here we should check if the second group box should be shown or not...
            #Note that we don't check if it's already shown as that would require an extra conditional
            if self.pizzas_ordering_combobox.currentText() == "1":
                self.pizza_two_groupbox_2.hide()
            else:
                self.pizza_two_groupbox_2.show()
            #calculate...

        else:
            self.screen_1_box.show()
            self.screen_2_box.hide()
            self.current_screen = 1
            self.calculate_button.setText("Calculate")
            #Allow the user to change these inputs again
            self.customer_name_edit.setEnabled(True)
            self.pizzas_ordering_combobox.setEnabled(True)
    def clear_inputs(self):
        pass
    def update_groupboxes(self, index):
        """Update the `enabled` property of the 2nd pizza group boxes as needed.
        
        This is based off of the currentIndexChanged signal of the combo box handling
        the number of pizzas the user wants to order (either 1 or 2). This is only executed
        when the selected index actually changes, limiting unnecessary calls."""
        if index == 0:
            self.pizza_two_groupbox_1.setEnabled(False)
            self.pizza_two_groupbox_2.setEnabled(False)
        else:
            #There are only two possible states, since an invalid index is impossible normally
            #So assuming two pizzas otherwise is alright
            self.pizza_two_groupbox_1.setEnabled(True)
            self.pizza_two_groupbox_2.setEnabled(True)
    def closeEvent(self, event):
        response = QtWidgets.QMessageBox.question(self, "Exit?",
                                                  "<p>Are you sure you want to exit pizza ordering?</p>"
                                                  "<p>Any entered selections will not be saved.</p>", 
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if response == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = ApplicationWindow()
    w.show()

    sys.exit(app.exec_())
