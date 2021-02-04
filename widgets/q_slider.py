from PySide2.QtWidgets import QApplication, QMainWindow, QSlider


# subclass the QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSlider()
        # widget = QSlider(Qt.Vertical) # Vertical slider
        # widget = QSlider(Qt.Horizontal) # Horizontal slider

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")

    
# create application instance
app = QApplication([])

window = MainWindow()
window.show() # windows are hidden by default

# start the event loop
app.exec_()
