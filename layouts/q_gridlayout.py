from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QGridLayout

from layout_colorwidget import Color


# subclass the QMainWindow to customize the application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()
        layout.addWidget(Color("red"), 0,0)
        layout.addWidget(Color("yellow"), 0,1)
        layout.addWidget(Color("green"), 1,0)
        layout.addWidget(Color("blue"), 1,1)
        layout.addWidget(Color("orange"), 2,0)
        layout.addWidget(Color("purple"), 2,1)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

# create application instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default

app.exec_()
