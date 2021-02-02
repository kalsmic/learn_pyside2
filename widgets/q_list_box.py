from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget

# sub class the QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)


        self.setCentralWidget(widget)


    def index_changed(self, i:object):# Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s:str):
        print(s)


# create application instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default

#  start event loop
app.exec_()