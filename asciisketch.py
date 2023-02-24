"""
ASCIISKETCH

asciisketch.py
---
This is the main entry point of the asciisketch project.
This source file will contain all non-library code for the project.

"""

#---------#
# Imports #
#---------#

import tkinter
import as_generators
from functools import partial


#---------#
# Globals #
#---------#

root=tkinter.Tk() # toplevel window widget
buttonChars    = "+-|_.'/\\#$*><xo" # what characters to use to populate buttons
buttonCharSize = 14 # size of character selection buttons (font size)
cLabelSize     = 12 # size of canvas labels (font size)
lWidth         = 28 # amount of canvas labels in width
lHeight        = 16 # amount of canvas labels in height


#-----------#
# Functions #
#-----------#

# change the current character to draw to the current button pressed
def changeCurChar(char):
   label_curSelected.config(text = char)


#--------------------------#
# Tkinter specific widgets #
#--------------------------#

# create a logo to show on the top left of the window
img_logo   = tkinter.PhotoImage(file = "./img/asLogo.png")
label_logo = tkinter.Label(image = img_logo)
label_logo.grid(row = 0, column = 0, sticky = tkinter.NW)

# create text to go beside the logo
label_titleOfApp = tkinter.Label(root, text="asciiSketch", font="Monospace 12 italic bold")
label_titleOfApp.grid(row = 0, column = 1, sticky = tkinter.NW)

# create label to show the currently selected ascii char to draw
label_curSelected = tkinter.Label(root, text = "+", font = "Monospace 24", bg = "yellow", width = 3)
label_curSelected.grid(row = 2, column = 0, columnspan = 2, sticky = tkinter.W)

# create selectable buttons to change currently selected ascii char
labelframe_selectable = tkinter.LabelFrame(root, text = "Characters", width = 1)
labelframe_selectable.grid(row = 1, column = 0, sticky = tkinter.NW)

buttons = as_generators.generateSelectables(labelframe_selectable, buttonChars, buttonCharSize)
bCount = 0
for bChar in buttons:
    bChar.grid(row = bCount // 2, column = bCount % 2)
    bChar.config(command = partial(changeCurChar, bChar['text']))
    bCount += 1

# create labels to "draw" to with the currently seleceted
labelframe_canvas = tkinter.LabelFrame(root, text="Canvas")
labelframe_canvas.grid(row = 1, column = 1, rowspan = 10, sticky = tkinter.NW)

canvas = as_generators.generateLabels(labelframe_canvas, cLabelSize, lWidth, lHeight)
cCount = 0
for c in canvas:
    c.grid(row = 3 + cCount // lWidth, column = 3 + cCount % lWidth, padx = 1, pady = 1)
    cCount += 1

#------------------------------------#
# Tkinter specific window properties #
#------------------------------------#

root.title("asciiSketch")

root.minsize(650, 400)
root.geometry("1075x775")
root.mainloop()
