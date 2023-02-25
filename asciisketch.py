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
buttonChars    = "+-()|_.'/\\#$*><xo^\"" # what characters to use to populate buttons
buttonCharSize = 12 # size of character selection buttons (font size)
cButtonSize    = 11 # size of canvas labels (font size)
lWidth         = 28 # amount of canvas labels in width
lHeight        = 16 # amount of canvas labels in height


#-----------#
# Functions #
#-----------#

# change the current character to draw to the current button pressed
def changeCurChar(char):
   label_curSelected.config(text = char)

def setCavnasTextToCurChar(canvasBlob):
   if label_curSelected['text'] == "DEL":
      canvasBlob['text'] = " "
      return
   canvasBlob['text'] = label_curSelected['text']

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

# create labels to "draw" to with the currently selected
labelframe_canvas = tkinter.LabelFrame(root, text="Canvas")
labelframe_canvas.grid(row = 1, column = 1, rowspan = 10, sticky = tkinter.NW)

canvas = as_generators.generateCanvas(labelframe_canvas, cButtonSize, lWidth, lHeight)
cCount = 0
for c in canvas:
    c.grid(row = 3 + cCount // lWidth, column = 3 + cCount % lWidth)
    #c.bind("<Button-1>", lambda e:setCavnasTextToCurChar(c, label_curSelected['text'])) # bind to event -> change text property to current label_curSelected's text
    c.config(command = partial(setCavnasTextToCurChar, c))
    cCount += 1

# create a label for the eraser tool

label_eraser = tkinter.Button(labelframe_selectable, text="DEL", font="Monospace " + str(buttonCharSize), bg="grey", width=4)
label_eraser.grid(row = bCount, column = 0, columnspan = 2)
#label_eraser.config(partial(changeCurChar, label_eraser['text']))
label_eraser.config(command = partial(changeCurChar, label_eraser['text']))

#------------------------------------#
# Tkinter specific window properties #
#------------------------------------#

root.title("asciiSketch")

root.minsize(650, 400)
root.geometry("1175x890")
root.mainloop()
