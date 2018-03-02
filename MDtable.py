from tkinter import *

class Table:
    # initialize variables window
    def __init__(self, window, color="cyan",
                 width=4475, height=1050):
        self.width = width
        self.height = height
        self.color = color
        self.canvas = Canvas(window, bg=self.color, height=self.height, width=self.width)
        self.canvas.pack()
        font = ("monaco", 150)
        self.scoreboard = self.canvas.create_text(950, 525, font=font, fill="red")
    #remove item for colision with enemy sprite
    def remove_item(self, item):
         item.remove(self.canvas)
        
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

    def draw_score(self, score):
        scores = str(score)
        self.canvas.itemconfigure(self.scoreboard, text=scores)
