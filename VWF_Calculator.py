# File: VWF_Calculator.py
# Python version: Compatible with 3.7+ and modern versions
# Author: Bunkai
# Version: 0.02
# Date: 2024

import sys  # will allow us to handle the application's termination and exit status through the exit() function
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel # Import QApplication and all the required widgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase

# Configuration constants
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 224
TILE_SIZE = 10
MAX_LINE_SIZE = 7  # ZERO for no limit
BACKGROUND = 'Background.png'

# Read the input and parse any control code into the action it should do instead of display the code itself
def parse_control_codes(text, max_line_size):
    array = ""
    current_line_size = 0# current number of characters in the printing line

    i = 0 # variable to iterate through the string
    while i < len(text):  # traverse the text array, character by character
        if max_line_size != 0 and current_line_size >= max_line_size: # check if the line has reached its limit if any
            array += "\n" # insert a breakline into the displayed text
            current_line_size = 0 # a new line starts with zero characters

        # look for control code inputs
        if i + 3 < len(text) and text[i:i+4] == "<NL>":
            array += "\n" # insert the display for the control code
            current_line_size = 0
            i += 4 # update the current position of the i to avoid re-reading (and printing) the control code characters
            continue

        array += text[i] # add the current character
        current_line_size += 1 # update the number of characters in the current line
        i += 1 # update current position of the iterator in the array for the next iteration

    return array

# Main application window
class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("VWF Size Calculator")
        self.setGeometry(100, 100, SCREEN_WIDTH + 22, SCREEN_HEIGHT + 65)

        # Layout
        layout = QVBoxLayout(self)

        # Screen size label
        self.info_label = QLabel(f"ScreenSize: {SCREEN_WIDTH}x{SCREEN_HEIGHT}  ||  TileSize: {TILE_SIZE}")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFixedHeight(10)
        self.info_label.setStyleSheet("font-weight: bold")
        layout.addWidget(self.info_label)

        # Text input
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)

        # Display label
        self.display_label = QLabel("", self)
        layout.addWidget(self.display_label)

        # Load font
        font_id = QFontDatabase.addApplicationFont("EuropeanTeletext.ttf")
        if font_id == -1:
            print("Warning: Could not load font 'EuropeanTeletext.ttf'")

        # Connect signal
        self.line_edit.textChanged.connect(self.update_label)

    def update_label(self):
        text = self.line_edit.text()
        parsed_text = parse_control_codes(text, MAX_LINE_SIZE)
        self.display_label.setText(parsed_text)
        self.display_label.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.display_label.setFont(QFont("European Teletext", TILE_SIZE))
        self.display_label.setContentsMargins(64, 62, 0, 120)
        self.display_label.setStyleSheet(f"background-image: url({BACKGROUND}); color: red;")

if __name__ == "__main__":
    # Single QApplication instance
    app = QApplication(sys.argv)

    # Create and show window
    window = Window()
    window.show()

    # Run event loop
    sys.exit(app.exec())