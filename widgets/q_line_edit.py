from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit


# sub class the QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter text")

        # widget.setReadOnly(True)

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        # widget.setInputMask('000.000.000.000;_')

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())
    
    def text_changed(self, s:str):
        print("Text Changed ...")
        print(s)

    def text_edited(self, s:str):
        print("Text edited...")
        print(s)


# create applicatio instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default


# start event loop
app.exec_()