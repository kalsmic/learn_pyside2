from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton


# subclass the QMainWindow to modify the main window of our application
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # store the button state in a variable so that it can be referenced
        self.button_is_checked = True

        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        # .released is the signal, button_was_released is the slot.
        #  the signal is connected to the slot
        self.button.released.connect(self.button_was_released)
        self.button.setChecked(self.button_is_checked)

        #  set the central widget of the window
        self.setCentralWidget(self.button)

    def button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        # .isCheched() returns the check state of the button

        print(self.button_is_checked)

        # Also change the window title
        self.setWindowTitle("My one shot app")

# create an instance of the application
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default.

# start the event loop
app.exec_()


