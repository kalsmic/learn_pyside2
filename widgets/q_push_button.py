from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

from PySide2.QtCore import Qt

import sys

#  subclass the mainwindow to customize my applications main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        # the .clicked signal sends extra information of what happened. 
        # the button toggled or checked state
        button.clicked.connect(self.the_button_was_toggled)
        

        # set the central widget of the window
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")


    def the_button_was_toggled(self, checked):
        print("Checked?", checked)



#  create QApplication instance
app = QApplication(sys.argv)

window = MainWindow()
window.show() # windows are hidden by default

#  start the event loop
app.exec_()
