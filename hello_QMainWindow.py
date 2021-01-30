from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

#  subclass Qmainwindow to customize my application's main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyApp")

        button = QPushButton("Press Me!")

        #  Set the central widget of the window
        self.setCentralWidget(button)

#  create application instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default


app.exec_()