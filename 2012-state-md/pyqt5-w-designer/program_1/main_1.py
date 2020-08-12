"""Program 1: PyQt5+designer used."""

import sys
from PyQt5 import QtWidgets
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

        self.name = data[0]
        self.team = data[1]
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

    def batting_average(self):
        """Calculate and return the batting average of this player.

        The batting average of a player is the number of hits divided by their times at bat.
        """
        return self.hits()/self.times_at_bat

    def slugging_average(self):
        """Calculate and return the slugging average of this player.

        The slugging average of a player is equal to singles+doubles*2
        +triples*3+home runs*4 divided by the times at bat.
        """
        weighted = self.singles + self.doubles*2 + self.triples*3 + self.home_runs*4
        return weighted/self.times_at_bat

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
        self.calculate_button.clicked.connect
    
    def exit(self):
        """Exit the program by calling `close()`.
        
        Normally called when the `Exit` button is clicked.
        """
        self.close()
    def handle_center_button(self):
        """Depending on the screen, determine what to do when the `Calculate` button is clicked.
        
        Note that this center button will change text during normal program operation."""
        if self.current_screen = 1:
            self.calculate_and_add_player()
        elif self.current_screen = 2:
            self.generate_final_screen()
        else:
            #case 3; default
            self.clear_and_return

    def calculate_and_add_player(self):
        """Get the player input data, create a Player object, and add it to the list of players.
        
        This also changes the screen and handles label updates.
        """
        #Change "calculate" button to "Go to final screen"
        pass
    def generate_final_screen(self):
        """Generate the final screen, updating the player list and applicable labels."""
        #Change "Go to final screen" to "Return to player entry"
        pass
    def clear_and_return(self):
        """Clear all input fields and set the current screen to the first."""
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = ApplicationWindow()
    w.show()

    sys.exit(app.exec_())
