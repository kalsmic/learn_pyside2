from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox


# subclass the QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s:str):
        """string includes both the prefix and suffix characters"""
        print(s)

    
# create application instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default

# start the event loop
app.exec_()
