from PySide2.QtWidgets import QApplication, QPushButton

#  create QApplication instance
app = QApplication([])

window = QPushButton("Push Me")
window.show() # windows are hidden by default

#  start the event loop
app.exec_()