# File: VWF_Calculator.py
# Python version used: 3.7.3
# Author : Bunkai
# Version: 0.01
# Date:  2024

import sys # will allow us to handle the application's termination and exit status through the exit() function
from PyQt5.QtWidgets import * # Import QApplication and all the required widgets


# Instance of QApplication to use
app = QApplication([])

# Our application's GUI
window = QWidget()
window.setWindowTitle("Variable Width Font Calculator")
window.setGeometry(100, 100, 280, 80) # window.x, window.y, window.width, window.height
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)


# Show application's GUI in screen
window.show()

# Run application's event loop
sys.exit(app.exec())