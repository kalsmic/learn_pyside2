from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

# subclasss the QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QLabel("Hello")
        font = widget.font() # get current font
        font.setPointSize(38) # modify it.
        widget.setFont(font) # apply the modified font back.
        # use the pipe (|) to  combine flags together
        # only one vertical or horizontal aligemtn flag at a time
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
       # shorthand widget.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(widget)


# create application instance
app= QApplication([])

window = MainWindow()
window.show() # window is hidden by default

# start the event loop
app.exec_()
