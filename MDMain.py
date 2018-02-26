from tkinter import *
import MDtable, sprite, random
#create table
window = Tk()
window.title("Circle Gets The Square")
my_table = MDtable.Table(window)

player_s = sprite.Sprite(table=my_table, width=15, height=15, x_posn=50, y_posn=50, color="green", x_speed=23, y_speed=23)
evil_sprite1 = sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
evil_sprite2 = sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
evil_sprite3 = sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
evil_sprite4 = sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
evil_sprite5 = sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
def game_flow():

    if evil_sprite1.detect_collision(player_s, sides_sweet_spot=True, topnbottom_sweet_spot=True):
        remove_item(evil_sprite1)
    
    window.after(50, game_flow)

window.bind("<A>", player_s.move_left)
window.bind("<D>", player_s.move_right)
window.bind("<W>", player_s.move_up)
window.bind("<S>", player_s.move_down)

game_flow()
window.mainloop

