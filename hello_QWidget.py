from PySide2.QtWidgets import QApplication, QWidget

import sys

# only one application instance is needed per application
app = QApplication(sys.argv) 
# app = QApplication([]) is valid if no command line arguments 
# are to be passed. empty list can be provided instead.


# Create an instance of a QT widget,
# which will be our window
window = QWidget()

window.show() # windows are hidden by default.
# The window holds the user-interface of te application
# Every application needs atleast one
# Application will exit by default when last window is closed.


# start the event loop
app.exec_()

# The application won't reach here until I exit and the event
# loop has stooped.

