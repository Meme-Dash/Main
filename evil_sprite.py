import MDtable, random

class Evil_sprite:
    def __init__(self, table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400), color="red"):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color
        self.x_start = x_posn
        self.y_start = y_posn
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
    def remove(self,canvas):
        canvas.delete(self.rectangle)
        self.x_posn=999
