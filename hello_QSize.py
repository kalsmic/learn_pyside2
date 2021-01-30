from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton


#  subclass QMainWindow to customize my application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button  = QPushButton("Press Me !")

        # self.setFixedSize(QSize(400,300))
        # self.setMinimumSize(QSize(400,300)) # to set minimum size
        # self.setMaximumSize(QSize(500, 300)) # to set maximum size

        # set the central widget of the window
        self.setCentralWidget(button)

# create application instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default

app.exec_()