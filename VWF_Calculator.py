# File: VWF_Calculator.py
# Python version used: 3.7.3
# Author : Bunkai
# Version: 0.01
# Date:  2024

import sys # will allow us to handle the application's termination and exit status through the exit() function
from PyQt5.QtWidgets import * # Import QApplication and all the required widgets


# Displayed Window
class Window(QDialog):

	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("Variable Width Font Calculator")
		self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)
		
		layout = QVBoxLayout()
		
		# Create a QLineEdit widget
		self.label = QLabel("ScreenSize: " + str(ScreenResolution) + "  ||  TileSize: " + str(TileSize) ) # Display Game's screen Resolution and Font Game's Resolution
		layout.addWidget(self.label)			
		
		# Create a QLineEdit widget
		self.line_edit = QLineEdit(self)
		layout.addWidget(self.line_edit)
		
		# Create a QLabel widget
		self.label = QLabel("Display: ", self)
		layout.addWidget(self.label)
		
		# Connect the textChanged signal to the update_label slot
		self.line_edit.textChanged.connect(self.update_label)
		
		self.setLayout(layout)
		
	# Slot function to update the label text
	def update_label(self):
		text = self.line_edit.text()
		self.label.setText("Display: " + text)


if __name__ == "__main__":

	ScreenResolution = 18
	TileSize = 8

	# Instance of QApplication to use
	app = QApplication([])
	# Our application's GUI
	window = Window()
	# Show application's GUI in screen
	window.show()
	# Run application's event loop
	sys.exit(app.exec())