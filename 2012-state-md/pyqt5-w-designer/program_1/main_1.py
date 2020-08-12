"""Program 1: PyQt5+designer used."""

import sys
from PyQt5 import QtWidgets, QtCore
from program_1 import Ui_MainWindow

class Player():
    """Represents a single batter."""

    def __init__(self, data):
        """Initialize the player using `data`, a `list`.

        `data` is of the format [player name, team code, times at
        bat, singles, doubles, triples, home runs].
        """
        #While true we can just store a bunch of arrays, I like storing a bunch
        #of these objects better

        #these two are strings
        self.name = data[0] 
        self.team = data[1] 
        #the rest are ints
        self.times_at_bat = data[2]
        self.singles = data[3]
        self.doubles = data[4]
        self.triples = data[5]
        self.home_runs = data[6]

    def hits(self):
        """Calculate and return the hits of this player.
        
        Equal to the sum of singles, doubles, triples, and home_runs, unweighted.
        """
        return self.singles + self.doubles + self.triples + self.home_runs

    def batting_average(self, places=4):
        """Calculate and return the batting average of this player.

        The batting average of a player is the number of hits divided by their times at bat.
        """
        return round(self.hits()/self.times_at_bat, places)

    def slugging_percentage(self, places=4):
        """Calculate and return the slugging percentage of this player.

        The slugging percentage of a player is equal to singles+doubles*2
        +triples*3+home runs*4 divided by the times at bat.

        Also rounds decimals to a certain number of `places`, default 4.
        """
        weighted = self.singles + self.doubles*2 + self.triples*3 + self.home_runs*4
        return round(weighted/self.times_at_bat, places)
    
    def is_valid(self):
        """Check if this is a valid player.
        
        An invalid player is one whose hits exceeds their times at bat or lacks a name.
        """
        if self.name == "":
            return False
        elif self.hits() > self.times_at_bat:
            return False
        else:
            return True

class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window. Instantiated once."""

    def __init__(self):
        """Initialize and connect signals/slots."""
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        #This will store all of the Player objects.
        self.players = []

        #For convenience, we can store the current screen here.
        #1 is the input screen, 2 is the single-player representation screen, 
        #and 3 is the final screen.
        self.current_screen = 1

        #Hide the "other screens" to reflect the above
        self.first_output_box.hide()
        self.final_output_box.hide()

        #Connect buttons
        self.exit_button.clicked.connect(self.exit)
        self.calculate_button.clicked.connect(self.handle_center_button)
        self.clear_button.clicked.connect(self.clear_and_return)
    
    def exit(self):
        """Exit the program by calling `close()`.
        
        Normally called when the `Exit` button is clicked.
        """
        self.close()
    def handle_center_button(self):
        """Depending on the screen, determine what to do when the `Calculate` button is clicked.
        
        Note that this center button will change text during normal program operation.
        """
        if self.current_screen == 1:
            self.calculate_and_add_player()
        elif self.current_screen == 2:
            self.generate_final_screen()
        else:
            #case 3; default
            self.clear_and_return()
    def calculate_and_add_player(self):
        """Get the player input data, create a Player object, and add it to the list of players.
        
        This calls generate_second_screen after execution. Note that this also validates
        several values - the number of times at bat cannot be zero and cannot be less than the amount of hits,
        and the player name cannot be blank.
        """
        player_data = []
        player_data.append(self.player_name_edit.text())
        player_data.append(self.team_code_combobox.currentText())
        #This should be guaranteed to get each spinbox in the same order each time
        for spinbox in self.player_entry_box.findChildren(QtWidgets.QSpinBox):
            player_data.append(spinbox.value())
        #Now we create the player object and have it validate itself
        new_player = Player(player_data)
        #If valid, add the player and change to the second screen
        #Else, throw an error dialog at the user
        if new_player.is_valid():
            self.players.append(new_player)
            self.generate_second_screen()
        else:
            self.bad_player_dialog()
    def generate_second_screen(self):
        """Generate the first output screen using the most recently added Player object.
        
        This changes the screen and handles label updates.
        """
        #Get the most recent player
        last_player = self.players[-1]
        #Set label text based on that Player object
        self.player_name_label.setText(last_player.name)
        self.team_code_label.setText(f'Team {last_player.team}')
        self.at_bat_label.setText(str(last_player.times_at_bat))
        self.batting_avg_label.setText(str(last_player.batting_average()))
        self.slugging_label.setText(str(last_player.slugging_percentage()))
        self.total_hits_label.setText(str(last_player.hits()))
        self.singles_label.setText(str(last_player.singles))
        self.doubles_label.setText(str(last_player.doubles))
        self.triples_label.setText(str(last_player.triples))
        self.home_runs_label.setText(str(last_player.home_runs))
        #Change the screen
        self.change_screen(2)
    def generate_final_screen(self):
        """Generate the final screen, updating the player list and applicable labels."""
        #Change "Go to final screen" to "Return to player entry"
        
        #First we'll figure out who has the highest average
        #By default, the best player is the first
        #This is guaranteed to run since the only way to get to the third screen
        #is via the second screen, at which point at least one player MUST be added
        best_player = self.players[0]
        for player in self.players:
            if player.batting_average() > best_player.batting_average():
                best_player = player
        
        #Now we'll update the end labels
        self.highest_avg_label.setText(f'Best Player by Batting Average: {best_player.name}')
        self.avg_value_label.setText(f'Batting Average: {best_player.batting_average()}')

        self.table_widget.setSortingEnabled(False)

        #If I had extra time, I'd try to impress with this thing they didn't ask for
        #clear the table
        self.table_widget.setRowCount(0)
        for player in self.players:
            #index of this row
            row = self.table_widget.rowCount()
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(player.name))
            self.table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(player.team))
            self.table_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(player.batting_average())))
            self.table_widget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(player.slugging_percentage())))
            self.table_widget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(player.times_at_bat)))
            self.table_widget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(player.hits())))
            self.table_widget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(player.singles)))
            self.table_widget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(player.doubles)))
            self.table_widget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(player.triples)))
            self.table_widget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(player.home_runs)))

        self.table_widget.setSortingEnabled(True)
        self.table_widget.sortByColumn(2, QtCore.Qt.DescendingOrder)

        self.change_screen(3)
    def clear_and_return(self):
        """Clear/reset all input fields and set the current screen to the first."""
        self.player_name_edit.clear()
        self.team_code_combobox.setCurrentIndex(0)
        for spinbox in self.player_entry_box.findChildren(QtWidgets.QSpinBox):
            spinbox.setValue(0)
        if self.current_screen != 1:
            self.change_screen(1)
    def change_screen(self, new_screen):
        """Set the current screen. Simplifies widget hiding."""
        if new_screen not in (1,2,3):
            #Debug only
            raise ValueError
        self.current_screen = new_screen
        if new_screen == 1:
            self.player_entry_box.show()
            self.first_output_box.hide()
            self.final_output_box.hide()
            self.calculate_button.setText("Calculate")
            self.calculate_button.setToolTip("Calculate this player's statistics.")
        elif new_screen == 2:
            self.player_entry_box.hide()
            self.first_output_box.show()
            self.final_output_box.hide()
            self.calculate_button.setText("Go to final screen")
            self.calculate_button.setToolTip("Show the best player and a table of all data.")
        else:
            #again, default to the last screen
            self.player_entry_box.hide()
            self.first_output_box.hide()
            self.final_output_box.show()
            self.calculate_button.setText("Return to player entry")
            self.calculate_button.setToolTip("This button has the same effect as clicking Clear.")
    def bad_player_dialog(self):
        """Generate a dialog telling the user they have inputted bad data."""
        #Really this is a roundabout way of handling zero division errors
        QtWidgets.QMessageBox.critical(self, "Bad player data!",
                                       "<p>Validation of your player data failed! This means "
                                       "that at least one of the following is true:</p>"
                                       "<p><ul>"
                                       "<li>You are missing a player name.</li>"
                                       "<li>The number of hits (singles+doubles+...) exceeds "
                                       "the number of times at bat.</li></ul></p>"
                                       "<p>Please check your inputs and try again.</p>",
                                       QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = ApplicationWindow()
    w.show()

    sys.exit(app.exec_())
