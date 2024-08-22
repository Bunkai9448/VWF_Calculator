# Varible Width Font (VWF) Calculator
Variable Width Font Calculator aka Text Size Calculator

## Why do you need this tool?
Usually, the first though to see how a text looks in a game window, is about inserting said text. However, what if you could do the same without doing the inserting every time? Well, look no more, this is the tool you want.


## Files in this folder, with a description of each.

Background.png: This is the image that the tool will display, the purple rectangle in the sample.

EuropeanTeletext.ttf: This is a mono-space font (Fixed width Font), the tool will use it for display by default. You can put any other Font to see different options, put a non mono-space font for a VWF display.

LICENSE: selfexplanatory, right?

README.md: This is the file you are reading now.

Sample.png: This is an example image of the tool running.

VWF_Calculator.py: This is the script that you will run to launch the tool.

## How to use
![Display Sample](https://github.com/Bunkai9448/VWF_Calculator/blob/main/Sample.png)

First off all, you should now that to run this tool, you need python 3.7 and pyqt 5 installed in your system. Without them, it won't work.

With that out of the way, if you open your 
VWF_Calculator.py file (with a text editor), before launching (running) it, you can edit some settings for the tool's display. The full code is commented to the line, but here you can see the key values you want to have in mind.

- ScreenWidth: is your game's width
- ScreenHeight: is your game's height
- TileSize: Self-explatory name, right?
- Background: This is the name of the image file that will be displayed for the game, you don't really need to change it. [For ease of use, just replace the image file instead]
-	maxLineSize: is the maximum number of characters you want to have per line, set to ZERO (0) if you want no limit.
- ctrlCode = `"<NL>"` : this is an example of control code that is in use to create a line break. Currently this variable is unused, and only for explaining purposes.
- If you go to the `update_label` function around line 76, You can edit how and where the text will show: Font color, size, the margins for the text in the image... 
- For a Fixed width use Mono Space Font, for VWF use any other Font.
- To make the margins fit in display for more than one line, use the bottom-margin for the maximum number of lines it could display and add lines with <NL> if you don't write enough text to fill them. It's not the perfect solution, but will give you a good display until that is properly fixed.

## List of References and Documentation (in no particular order)
- PyQt https://realpython.com/python-pyqt-gui-calculator/ , https://github.com/pyqt/examples , https://doc.qt.io/qtforpython-6/overviews/stylesheet-examples.html , https://stackoverflow.com/questions/27955654/how-to-use-non-standard-custom-font-with-stylesheets
- Calculator https://calculator.academy/text-size-calculator/

## Included Files with different licenses.
- EuropeanTeletext, licensed under the CC0 1.0 Universal, https://creativecommons.org/publicdomain/zero/1.0/deed.en

## Credits and original source

This tool was developed by Bunkai, if you want to report an issue, you can find the source at: https://github.com/Bunkai9448/VWF_Calculator
