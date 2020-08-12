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

    def batting_average(self):
        """Calculate and return the batting average of this player.

        The batting average of a player is the number of times at bat divided
        by their hits.
        """
        pass

    def slugging_average(self):
        """Calculate and return the slugging average of this player.

        The slugging average of a player is equal to singles+doubles*2
        +triples*3+home runs*4 divided by the times at bat.
        """
        pass

class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window. Instantiated once."""

    def __init__(self):
        """Initialize and connect signals/slots."""
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        #This will store all of the Player objects

        #Hide the "other screens"
        self.first_output_box.hide()
        self.final_output_box.hide()
    
    def exit(self):
        pass
    def calculate_and_add_player(self):
        pass
    def clear_and_return(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = ApplicationWindow()
    w.show()

    sys.exit(app.exec_())
