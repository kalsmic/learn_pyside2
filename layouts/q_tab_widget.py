from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget
)

from layouts.layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        for n, color in enumerate(["red","green", "blue", "yellow", "purple"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication([])
window = MainWindow()
window.show()

app.exec_()


