# File: VWF_Calculator.py
# Python version used: 3.7.3
# Author : Bunkai
# Version: 0.01
# Date:  2024

import sys # will allow us to handle the application's termination and exit status through the exit() function
from PyQt5.QtWidgets import * # Import QApplication and all the required widgets


class Window(QDialog):

	def __init__(self):

		super().__init__(parent=None)

		self.setWindowTitle("Variable Width Font Calculator")
			
		helloMsg = QLabel("<h1>Hello, World!</h1>") # Display Game's screen Resolution and Font Game's Resolution

		dialogLayout = QVBoxLayout()

		formLayout = QFormLayout()
			
		formLayout.addRow(helloMsg)

		formLayout.addRow("Input:", QLineEdit())

		formLayout.addRow("Display:", QLineEdit())

		dialogLayout.addLayout(formLayout)

		self.setLayout(dialogLayout)


if __name__ == "__main__":

	# Instance of QApplication to use
	app = QApplication([])
	# Our application's GUI
	window = Window()
	# Show application's GUI in screen
	window.show()
	# Run application's event loop
	sys.exit(app.exec())