from tkinter import *
import MDtable, sprite, random, evil_sprite
#create table
window = Tk()
window.title("Circle Gets The Square")
my_table = MDtable.Table(window)
score_solo = 0

player_s = sprite.Sprite(table=my_table, width=30, height=30, x_posn=50, y_posn=50, color="green", x_speed=23, y_speed=23)
evil_sprite1 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
evil_sprite2 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
evil_sprite3 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
evil_sprite4 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
evil_sprite5 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))


def game_flow():
    global score_solo

    if player_s.detect_collision(evil_sprite1) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite1)
        my_table.draw_score(score_solo)
        if(score_solo >= 25):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite2) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite2)
        my_table.draw_score(score_solo)
        if(score_solo >= 25):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite3) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite3)
        my_table.draw_score(score_solo)
        if(score_solo >= 25):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite4)== True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite4)
        my_table.draw_score(score_solo)
        if(score_solo >= 25):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite5) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite5)
        my_table.draw_score(score_solo)
        if(score_solo >= 25):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)
            
    window.after(50, game_flow)

def restart_game(master):
    global evil_sprite1,evil_sprite2,evil_sprite3,evil_sprite4,evil_sprite5
    evil_sprite1 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
    evil_sprite2 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
    evil_sprite3 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
    evil_sprite4 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
    evil_sprite5 = evil_sprite.Evil_sprite(table=my_table, width=14, height=14, x_posn=random.randint(0, 600), y_posn=random.randint(0, 400))
    game_flow()

window.bind("<Left>", player_s.move_left)
window.bind("<Right>", player_s.move_right)
window.bind("<Up>", player_s.move_up)
window.bind("<Down>", player_s.move_down)
window.bind("<space>", restart_game)

game_flow()
window.mainloop


