#!/usr/bin/python

#yes i used the online qt docs for this since i couldn't figure out how to compile them lol

#imports
import sys
from PyQt5 import QtWidgets
from program_2 import Ui_MainWindow

def pad_zeroes(input):
    #yes i used stockoverflow for this one
    #if i were under time pressure i would've done something like converting it to a string
    #and checking the last two digits lol
    return '{:.2f}'.format(input)

class Pizza():
    """Represents a pizza object.
    
    Takes an array `pizza_arr` of four ints, the first three of which should be the
    button IDs of their respective groups; the last of which should be the topping
    count.
    """

    def __init__(self, pizza_arr):
        """Create/initialize the pizza.

        Instance attributes are of the form [`name`, `cost`], where `name`
        is a `str` of the quality ("large", "thin", etc.) and `cost` is a
        `str` of the cost of that specific property.
        """
        #Based on the integer array `pizza`, we'll create the actual attributes
        #While shape and crust have no cost, they maintain the same format for consistency
        #and flexibility
        #These are specificially tailored around the integer IDs of their related button (group)
        sizes = {1:["Large", 15.95], 2:["Medium", 12.95], 3:["Small", 10.95]}
        shapes = {1:["Round", 0.00], 2:["Square", 0.00]}
        crusts = {1:["Thick", 0.00], 2:["Thin", 0.00]}
        #We iterate over each integer "property" except the last, which is the topping count
        self.size = sizes[pizza_arr[0]]
        self.shape = shapes[pizza_arr[1]]
        self.crust = crusts[pizza_arr[2]]
        #Finally, we figure out how much the toppings cost before adding it to the pizza object
        #Topping count is still a `str` for consistency
        topping_cost = pizza_arr[3]*1.25
        self.toppings = [str(pizza_arr[3]), topping_cost]
        #Convenience attribute representing the cost
        self.cost = self.size[1] + self.shape[1] + self.crust[1] + self.toppings[1]


class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window. Instantiated once."""

    def __init__(self):
        """Initialize and connect signals/slots."""
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

        #Again, while we can figure out how many pizzas there are from the combobox
        #It's easier to just have an explicit property of such
        self.pizzas_ordering = 1

        #Here we create several QButtonGroups to simplify obtaining the various radio button states
        #We can then create arrays as necessary to pass to business logic functions
        #We also assign permanent IDs to each one, done in order of appearance
        #Reduces ambiguity, although a little messy
        self.size_group_1 = QtWidgets.QButtonGroup()
        self.size_group_1.addButton(self.size_large_radio, 1)
        self.size_group_1.addButton(self.size_medium_radio, 2)
        self.size_group_1.addButton(self.size_small_radio, 3)
        self.shape_group_1 = QtWidgets.QButtonGroup()
        self.shape_group_1.addButton(self.shape_round_radio, 1)
        self.shape_group_1.addButton(self.shape_square_radio, 2)
        self.crust_group_1 = QtWidgets.QButtonGroup()
        self.crust_group_1.addButton(self.shape_thick_radio, 1)
        self.crust_group_1.addButton(self.shape_thin_radio, 2)
        self.size_group_2 = QtWidgets.QButtonGroup()
        self.size_group_2.addButton(self.size_large_radio_2, 1)
        self.size_group_2.addButton(self.size_medium_radio_2, 2)
        self.size_group_2.addButton(self.size_small_radio_2, 3)
        self.shape_group_2 = QtWidgets.QButtonGroup()
        self.shape_group_2.addButton(self.shape_round_radio_2, 1)
        self.shape_group_2.addButton(self.shape_square_radio_2, 2)
        self.crust_group_2 = QtWidgets.QButtonGroup()
        self.crust_group_2.addButton(self.shape_thick_radio_2, 1)
        self.crust_group_2.addButton(self.shape_thin_radio_2, 2)

        #We'll add the pizza-specific groups to their own array so they can be iterated over
        self.pizza_1_groups = [self.size_group_1, self.shape_group_1, self.crust_group_1]
        self.pizza_2_groups = [self.size_group_2, self.shape_group_2, self.crust_group_2]

        #Enable or disable the second group box depending on what the user selects
        #Listen for changes to the combobox to do so
        self.pizzas_ordering_combobox.currentIndexChanged.connect(self.update_groupboxes)

        #Bottom buttons
        self.exit_button.clicked.connect(self.exit)
        self.calculate_button.clicked.connect(self.calculate_and_swap)
        self.clear_button.clicked.connect(self.clear_inputs)
    def exit(self):
        """Close the program. Note that this is intercepted with an override closeEvent.
        
        This is called when the `Exit` button is clicked, but can be extended if necessary.
        """
        self.close()
    def calculate_and_swap(self):
        """Toggle between screen 1 and 2, calculating and reading order values if needed."""
        if self.current_screen == 1:
            #Here we validate the choices and the name before doing anything
            #These conditionals will return None and error dialogs if validation fails
            #This stops execution of this function
            if self.customer_name_edit.text() == '':
                self.noname_dialog()
                return None
            for group in self.pizza_1_groups:
                if group.checkedId() == -1:
                    self.missing_dialog()
                    return None
            if self.pizzas_ordering == 2:
                for group in self.pizza_2_groups:
                    if group.checkedId() == -1:
                        self.missing_dialog()
                        return None

            self.screen_1_box.hide()
            self.screen_2_box.show()
            self.current_screen = 2
            self.calculate_button.setText("Return to Order Selection")
            #We'll prevent the customer from changing their name or pizza count after calculation
            #By disabling these two widgets, they *must* return to the first screen to change these
            self.customer_name_edit.setEnabled(False)
            self.pizzas_ordering_combobox.setEnabled(False)
            #We also disable the "Clear" button to remove ambiguity
            self.clear_button.setEnabled(False)
            #Here we should check if the second group box should be shown or not...
            #Note that we don't check if it's already shown as that would require an extra conditional
            if self.pizzas_ordering_combobox.currentText() == "1":
                self.pizza_two_groupbox_2.hide()
            else:
                self.pizza_two_groupbox_2.show()

            #Update the big customer's name label
            #Also get angry if they don't have a name inputted
            #This comes before any calculations to 


            
            #Here we create a pizza with format [size, shape, crust, topping count]
            #Since self.pizza_1_groups always has the QButtonGroups in a specific order, 
            #it's possible to ensure the pizza is always built this way
            #Then we'll create an actual Pizza object that is dedicated to this process
            pizza_1_temp = []
            for i in range(0, 3):
                id = self.pizza_1_groups[i].checkedId()
                pizza_1_temp.append(id)
            pizza_1_temp.append(self.toppings_spinbox.value())
            pizza_1 = Pizza(pizza_1_temp)

            #in an ideal world this wouldn't be as messy, but since the labels are predefined
            #and there are so few of them, this seems like the best method
            #a better way - if you could add additional pizzas, for example - would be to 
            #programmatically define and create these labels rather than through Qt Designer

            #Now we change the labels as necessary based on the values of our new Pizza object
            #Recall the quality names are stored in index 0 of each instance attribute as `str`
            self.size_label.setText(f"Size - {pizza_1.size[0]}")
            self.toppings_label.setText(f"Toppings - {pizza_1.toppings[0]}")
            self.shape_label.setText(f"Shape - {pizza_1.shape[0]}")
            self.crust_label.setText(f"Crust - {pizza_1.crust[0]}")
            self.size_cost_label.setText(f"${pizza_1.size[1]}")
            self.toppings_cost_label.setText(f"${pad_zeroes(pizza_1.toppings[1])}")
            self.shape_cost_label.setText(f"${pad_zeroes(pizza_1.shape[1])}")
            self.crust_cost_label.setText(f"${pad_zeroes(pizza_1.crust[1])}")
            self.subcost_label.setText(f"${pad_zeroes(pizza_1.cost)}")

            #We do the same things for the second pizza if needed
            if self.pizzas_ordering == 2:
                pizza_2_temp = []
                for i in range(0, 3):
                    id = self.pizza_2_groups[i].checkedId()
                    pizza_2_temp.append(id)
                pizza_2_temp.append(self.toppings_spinbox_2.value())
                pizza_2 = Pizza(pizza_2_temp)

                self.size_label_2.setText(f"Size - {pizza_2.size[0]}")
                self.toppings_label_2.setText(f"Toppings - {pizza_2.toppings[0]}")
                self.shape_label_2.setText(f"Shape - {pizza_2.shape[0]}")
                self.crust_label_2.setText(f"Crust - {pizza_2.crust[0]}")
                self.size_cost_label_2.setText(f"${pad_zeroes(pizza_2.size[1])}")
                self.toppings_cost_label_2.setText(f"${pad_zeroes(pizza_2.toppings[1])}")
                self.shape_cost_label_2.setText(f"${pad_zeroes(pizza_2.shape[1])}")
                self.crust_cost_label_2.setText(f"${pad_zeroes(pizza_2.crust[1])}")
                self.subcost_label_2.setText(f"${pad_zeroes(pizza_2.cost)}")

            #finally, update the "cost" label
            if self.pizzas_ordering == 1:
                self.total_cost_label.setText(f'Total: ${pad_zeroes(pizza_1.cost)}')
            else:
                self.total_cost_label.setText(f'Total: ${pad_zeroes(pizza_1.cost+pizza_2.cost)}')

            #As well as the customer's name (label)
            self.customer_name_label.setText(f'Customer Name: {self.customer_name_edit.text()}')
        else:
            self.screen_1_box.show()
            self.screen_2_box.hide()
            self.current_screen = 1
            self.calculate_button.setText("Calculate")
            #Allow the user to change these inputs again
            self.customer_name_edit.setEnabled(True)
            self.pizzas_ordering_combobox.setEnabled(True)
            self.clear_button.setEnabled(True)
    def clear_inputs(self):
        """Clear all inputs from both pizzas.
        
        This is done by getting the checked buttons of the QButtonGroups, then deselecting them.
        There is no disambiguation on whether or not to clear both pizza ordering fields, so I
        have defaulted to clearing both.
        """
        #Deselect the selected button of each group
        #Note that in order to achieve this, their exclusivity must be disabled
        for group in self.pizza_1_groups:
            group.setExclusive(False)
            selected_button = group.checkedButton()
            if selected_button:
                selected_button.setChecked(False)
            group.setExclusive(True)
        for group in self.pizza_2_groups:
            group.setExclusive(False)
            selected_button = group.checkedButton()
            if selected_button:
                selected_button.setChecked(False)
            group.setExclusive(True)
        #Reset toppings spinboxes to 0
        self.toppings_spinbox.setValue(0)
        self.toppings_spinbox_2.setValue(0)
    def update_groupboxes(self, index):
        """Update the `enabled` property of the 2nd pizza group boxes as needed.
        
        This is based off of the currentIndexChanged signal of the combo box handling
        the number of pizzas the user wants to order (either 1 or 2). This is only executed
        when the selected index actually changes, limiting unnecessary calls.
        """
        if index == 0:
            self.pizza_two_groupbox_1.setEnabled(False)
            self.pizza_two_groupbox_2.setEnabled(False)
            self.pizzas_ordering = 2
        else:
            #There are only two possible states, since an invalid index is impossible normally
            #So assuming two pizzas otherwise is alright
            self.pizza_two_groupbox_1.setEnabled(True)
            self.pizza_two_groupbox_2.setEnabled(True)
            self.pizzas_ordering = 2
    def missing_dialog(self):
        """Creates a critical dialog informing the user of missing values.
        
        This is currently shown when a button group returns a selected id of -1,
        meaning no button from the group has been selected. This is an invalid input,
        and must be resolved by the user.
        """
        QtWidgets.QMessageBox.critical(self, "Missing values!",
                                       "<p>Please make sure you have selected an option "
                                       "for each pizza you are ordering.</p>",
                                       QtWidgets.QMessageBox.Ok)
    def noname_dialog(self):
        """Creates a critical dialog informing the user that they must enter a name."""
        QtWidgets.QMessageBox.critical(self, "Enter your name!",
                                       "<p>Please enter a name in the Customer Name field above.</p>",
                                       QtWidgets.QMessageBox.Ok)
    def closeEvent(self, event):
        """Intercept the built-in closeEvent.
        
        Here, we always ask the user if they want to exit. It would be possible
        to check if buttons have been pressed, but there is no need. 
        """
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
