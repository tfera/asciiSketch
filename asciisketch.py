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
buttonChars      = "+-()|_.'/\\#$*><xo^\"" # what characters to use to populate buttons
buttonCharSize   = 12 # size of character selection buttons (font size)
cButtonSize      = 11 # size of canvas labels (font size)
lWidth           = 28 # amount of canvas labels in width
lHeight          = 16 # amount of canvas labels in height
widthSelectables = 4  # how many characters wide the current character selection on left is


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

# draw canvas again with
def resetCanvasSize(width, height):
    try:
        width  = int(width)
        height = int(height)
    except:
        return

    for widget in labelframe_canvas.winfo_children():
        widget.destroy()

    canvas = as_generators.generateCanvas(labelframe_canvas, cButtonSize, width, height)
    cCount = 0
    for c in canvas:
        c.grid(row = cCount // width, column = cCount % width)
        c.config(command = partial(setCavnasTextToCurChar, c))
        cCount += 1


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
label_curSelected.grid(row = 3, column = 0, columnspan = 2, sticky = tkinter.W)

# create selectable buttons to change currently selected ascii char
labelframe_selectable = tkinter.LabelFrame(root, text = "Characters")
labelframe_selectable.grid(row = 2, column = 0, sticky = tkinter.NW)

buttons = as_generators.generateSelectables(labelframe_selectable, buttonChars, buttonCharSize)
bCount = 0
for bChar in buttons:
    bChar.grid(row = bCount // widthSelectables, column = bCount % widthSelectables)
    bChar.config(command = partial(changeCurChar, bChar['text']))
    bCount += 1

# create labels to "draw" to with the currently selected
labelframe_canvas = tkinter.LabelFrame(root, text="Canvas")
labelframe_canvas.grid(row = 1, column = 1, rowspan = 10, sticky = tkinter.NW)

canvas = as_generators.generateCanvas(labelframe_canvas, cButtonSize, lWidth, lHeight)
cCount = 0
for c in canvas:
    c.grid(row = 3 + cCount // lWidth, column = 3 + cCount % lWidth)
    c.config(command = partial(setCavnasTextToCurChar, c))
    cCount += 1

# create a label for the eraser tool
label_eraser = tkinter.Button(labelframe_selectable, text="DEL", font="Monospace " + str(buttonCharSize), bg="grey", width=4)
label_eraser.grid(row = bCount, column = 0, columnspan = 2)
label_eraser.config(command = partial(changeCurChar, label_eraser['text']))

# create a label frame for changing canvas size
labelframe_changeCanvas = tkinter.LabelFrame(root, text = "Canvas Size", width = 1)
labelframe_changeCanvas.grid(row = 1, column = 0, sticky = tkinter.NW)

lWidthSize = tkinter.Label(labelframe_changeCanvas, text="Width")
lWidthSize.grid(row = 0, column = 0, sticky = tkinter.NW)

widthEntry = tkinter.Entry(labelframe_changeCanvas)
widthEntry.grid(row = 1, column = 0, sticky = tkinter.NW)
widthEntry.insert(10, str(lWidth))

lHeightSize =  tkinter.Label(labelframe_changeCanvas, text="Height")
lHeightSize.grid(row = 2, column = 0, sticky = tkinter.NW)

heightEntry = tkinter.Entry(labelframe_changeCanvas)
heightEntry.grid(row = 4, column = 0, sticky = tkinter.NW)
heightEntry.insert(10, str(lHeight))

canvasResize = tkinter.Button(labelframe_changeCanvas, text="Resize Canvas")
canvasResize.grid(row = 5, column = 0, sticky = tkinter.NW)
canvasResize.config(command = lambda : resetCanvasSize(widthEntry.get(), heightEntry.get()))

#------------------------------------#
# Tkinter specific window properties #
#------------------------------------#

root.title("asciiSketch")

root.minsize(650, 400)
root.geometry("1175x890")
root.mainloop()
