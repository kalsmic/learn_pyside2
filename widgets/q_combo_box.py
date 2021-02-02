from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox

# subclass the QMainWindow to customize the application's main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello ComboBox")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        # widget can be editable
        # widget.setEditable(True)
        # widget.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.setCentralWidget(widget)

    def index_changed(self, i:int):# i is the index of the choice made
        print(i)

    def text_changed(self, s:str): # s is the text of the choice made
        print(s)


# create application instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default

# start event loop
app.exec_()