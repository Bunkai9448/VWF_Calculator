# File: VWF_Calculator.py
# Python version used: 3.7.3
# Author : Bunkai
# Version: 0.01
# Date:  2024

import sys # will allow us to handle the application's termination and exit status through the exit() function
from PyQt5.QtWidgets import * # Import QApplication and all the required widgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Read the input and parse any control code into the action it should do instead of display the code itself
def parseControlCodes(text):
	array = ""
	maxLineSize=7 # maximum number of characters per line if any ; ZERO for no limit
	currentLineSize = 0	# current number of characters in the printing line
	ctrlCode = "<NL>"
	
	for i in text: # Traverse the text array, character by character
	
		if maxLineSize != 0 and currentLineSize == maxLineSize: # check if the line has reached its limit if any
			array += "\n"  			# insert a breakline into the displayed text			
			currentLineSize = 0		# a new line starts with zero characters
		array += i			 # add current character to the display array
		currentLineSize += 1 # update the number of characters in the current line

	return array

# Main tool
class Window(QWidget):
	# Load User Font
	app = QApplication(sys.argv)
	QFontDatabase.addApplicationFont("EuropeanTeletext.ttf")

	def __init__(self):
		super(Window, self).__init__()
		
		self.setWindowTitle("VWF size Calculator")
		self.setGeometry(100, 100, ScreenWidth+22, ScreenHeight+65)  # (x, y, width, height)
		
		layout = QVBoxLayout(self)

		# Create a QLineEdit widget
		self.label = QLabel("ScreenSize: " + str(ScreenWidth) + "x" + str(ScreenHeight) + "  ||  TileSize: " + str(TileSize) ) # Display Game's screen Resolution and Font Game's Resolution
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setFixedHeight(10)
		layout.addWidget(self.label)	
		
		
		# Create a QLineEdit widget
		self.line_edit = QLineEdit(self)
		layout.addWidget(self.line_edit)


		# Create a QLabel widget
		self.label = QLabel("", self)
		layout.addWidget(self.label)
		self.label.setStyleSheet(" background-image : url(Background);")
		
		# Connect the textChanged signal to the update_label slot
		self.line_edit.textChanged.connect(self.update_label)
		
		
	# Slot function to update the label text
	def update_label(self):
		text = self.line_edit.text()	# Take the text from the User input
		text = parseControlCodes(text)	# Parse the text with control codes and line size stuff
		self.label.setText(text)		# Set the received text as input for the display
		self.label.setFixedWidth(ScreenWidth)	# Set Game's Window Width
		self.label.setFixedHeight(ScreenHeight)	# Set Game's Window Height
		self.label.setFont(QFont('European Teletext', TileSize))	# Set Font and Font Size
		# Add The Game's Screenshot as background, Set Text Coordinates and other Font config. Like Font color
		self.label.setStyleSheet("background-image : url(Background); padding-left : 60px;  padding-bottom : 80px;")
		#self.label.setStyleSheet("background-image : url(Background); padding-left : 80px;  padding-top : 80px; font: TileSize px;")
		

		
if __name__ == "__main__":

	ScreenWidth = 256
	ScreenHeight = 224
	TileSize = 10
	Background = 'Background.png'
	
	# Instance of QApplication to use
	app = QApplication([])
	# Our application's GUI
	window = Window()
	# Show application's GUI in screen
	window.show()
	
	# Run application's event loop
	sys.exit(app.exec())