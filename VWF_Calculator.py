# File: VWF_Calculator.py
# Python version used: 3.7.3
# Author : Bunkai
# Version: 0.01
# Date:  2024

import sys # will allow us to handle the application's termination and exit status through the exit() function
from PyQt5.QtWidgets import * # Import QApplication and all the required widgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		
		self.setWindowTitle("VWF size Calculator")
		self.setGeometry(100, 100, ScreenWidth, ScreenHeight+10)  # (x, y, width, height)
		
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
	def update_label(self,Dialogue):
		text = self.line_edit.text()
		self.label.setText(text)
		self.label.resize(ScreenWidth, ScreenHeight)
		self.label.setStyleSheet("background-image : url(Background); padding-left : 60px;  padding-bottom : 80px; font: TileSize px;")
		#self.label.setStyleSheet("background-image : url(Background); padding-left : 80px;  padding-top : 80px; font: TileSize px;")
		

		
if __name__ == "__main__":

	ScreenWidth = 280
	ScreenHeight = 280
	TileSize = 8
	Background = 'Background.png'
	
	# Instance of QApplication to use
	app = QApplication([])
	# Our application's GUI
	window = Window()
	# Show application's GUI in screen
	window.show()
	
	# Run application's event loop
	sys.exit(app.exec())