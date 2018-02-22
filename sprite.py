import random, table

class Sprite:
    def __init__(self, table, width=14, height=14, color="red",
               x_speed=150, y_speed=4, x_start=0, y_start=0):
        self.width = width
        self.height = height
        self.x_posn = x_start
        self.y_posn = y_start
        self.color = color


        self.x_start = x_start
        self.y_start = y_start
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.circle = self.table.draw_oval(self)

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def start_sprite(self, x_speed, y_speed):
        self.x_speed = -x_speed if random.randint(0,1) else x_speed
        self.y_speed = -y_speed if random.randint(0,1) else y_speed
        self.start_position()


    def move_up(self, master):
        self.y_posn = self.y_posn - self.y_speed
        if(self.y_posn <= 0):
            self.y_posn = 0
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed
        far_bottom = self.table.height - self.height
        if(self.y_posn >= far_bottom):
            self.y_posn = far_bottom
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_left(self, master):
        self.x_posn = self.x_posn - self.x_speed
        if(self.x_posn <= 0):
            self.x_posn = 0
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        far_right = self.table.width - self.width
        if(self.x_posn >= far_right):
            self.x_posn = far_right
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def stop_sprite(self):
        self.x_speed = 0
        self.y_speed = 0




class Evil_sprite:
    def __init__(self, table, width=14, height=14, x_posn=random.randint(300, -300), y_posn=random.randint(200, -200)):

        evil_sprites = []
        es=1
        while es < 7:
            i=80
            evil_sprites.append(sprite(table = my_table, width=50, height=20, x_posn=(es*i), y_posn=75, color="red"))
            es = es+1


    def detect_collision(self, ball, sides_sweet_spot=True, topnbottom_sweet_spot=False):
        collision_direction = ""
        collision = False
        feel = 5


        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_centre = top + (self.height/2)
        h_centre = left + (self.width/2)

        top_es = evil_sprite.y_posn
        bottom_es = evil_sprite.y_posn + evil_sprite.height
        left_es = evil_sprite.x_posn
        right_es = evil_sprite.x_posn + evil_sprite.width
        r = (right_es - left_es)/2
        v_centre_es = top_es + r
        h_centre_es = left_es + r

        if((bottom_es > top) and (top_es < bottom) and (right_es > left) and (left_es < right)):
            collision = True
        if(collision):
            if((top_es > top-r) and (bottom_es < bottom+r) and (right_es > right) and (left_es <= right)):
                collision_direction = "E"
                evil_sprites.x_speed = abs(evil_sprites.x_speed)

            elif((left_es > left-r) and (right_es < right+r) and (bottom_es > bottom) and (top_es <= bottom)):
                collision_direction = "S"
                evil_sprite.y_speed = abs(evil_sprite.y_speed)

            elif((left_es > left-r) and (right_es < right+r) and (top_es < top) and (bottom_es >= top)):
                collision_direction = "N"
                evil_sprite.y_speed = -abs(evil_sprite.y_speed)

            elif((top_es > top-r) and (bottom_es < bottom+r) and (left_es < left) and (right_es >= left)):
                collision_direction = "W"
                evil_sprite.x_speed = -abs(evil_sprite.x_speed)
            else:
                collision_direction = "miss"

            if((sides_sweet_spot == True) and (collision_direction == "W" or collision_direction == "E")):
                adjustment = (-(v_centre - v_centre_es))/(self.height/2)
                evil_sprite.y_speed = feel * adjustment

            if((topnbottom_sweet_spot == True) and (collision_direction == "N" or collision_direction == "S")):
                adjustment = (-(h_centre - h_centre_es))/(self.width/2)
                evil_sprite.x_speed = feel * adjustment


            return (collision, collision_direction)


            

