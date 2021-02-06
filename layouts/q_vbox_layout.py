from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from layout_colorwidget import Color


# subclass the QMainWindow to customize the application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("green"))


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


# create application instance
app  = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default

# start the event loop
app.exec_()