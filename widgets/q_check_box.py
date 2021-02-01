from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox


# subclass the MainWindow to customize our application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("This is a checkbox")
        widget.setCheckState(Qt.Checked)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)


    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


# create application instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default

#  start event loop
app.exec_()
