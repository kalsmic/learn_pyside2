import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStackedLayout,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)


        btn = QPushButton("red")
        btn.pressed.connect(self.activate_red_tab)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('red'))

        btn = QPushButton("green")
        btn.pressed.connect(self.activate_green_tab)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('green'))

        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_yellow_tab)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('yellow'))

        


        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_red_tab(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_green_tab(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_yellow_tab(self):
        self.stacklayout.setCurrentIndex(2)    




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
