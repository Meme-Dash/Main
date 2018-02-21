from tkinter import *
import MDtable
#create table with title
window = Tk()
window.title("MEMEDASH")
my_table = MDtable.Table(window)

player_s = sprite.Sprite(MDtable=my_table, width=100, height=10, x_posn=250, y_posn=370, color="blue")
evil_sprite = 

def game_flow():

    if evil_sprite1.detect_collision(player_s):
        remove_item(enemy_sprite1)
    
    window.after(50, game_flow)

window.bind("<Left>", player_s.move_left)
window.bind("<Right>", player_s.move_right)
window.bind("<Up>", player_s.move_up)
window.bind("<Down>"), player_s.move_down)

game_flow()
window.mainloop
