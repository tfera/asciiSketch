"""
ASCIISKETCH

as_generators.py
---
This file will contain code that does obvious and repetitive tasks
that do not belong in asciisketch.py

example: generate tkinter buttons for multiple ascii chars

"""

import tkinter


# generate tkinter buttons for multiple selectable ascii chars
def generateSelectables(root, buttonChars, buttonCharSize):
    buttons = []
    for bChar in buttonChars:
        buttons.append(tkinter.Button(root, text=bChar, font="Monospace " + str(buttonCharSize), bg="lightgrey", width=2))
    
    return buttons

# generate tkinter labels as a canvas
def generateLabels(root, cLabelSize, width, height):
    cLabels = []
    for lCanvas in range(height * width):
        cLabels.append(tkinter.Label(root, text=" ", font="Monospace " + str(cLabelSize), bg="grey", width=3, height=2))
    
    return cLabels
