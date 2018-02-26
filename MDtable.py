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
        font = ("monaco", 72)
        self.scoreboard = self.canvas.create_text(300, 65, font=font, fill="red")
    #remove item for colision with enemy sprite
    def remove_item(self, item):
        self.canvas.delete(item)

    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
 
    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.color
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)

    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)

    def draw_score(self, left, right):
        scores = str(right) + " " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores)

