from tkinter import *

class Table:
    # initialize variables window
    def __init__(self, window, color="cyan",
                 width=600, height=400):
        self.width = width
        self.height = height
        self.color = color
        self.canvas = Canvas(window, bg=self.color, height=self.height, width=self.width)
        self.canvas.pack()
    #remove item for colision with enemy sprite
    def move_item(self, item):
        self.canvas.delete(item)
 
