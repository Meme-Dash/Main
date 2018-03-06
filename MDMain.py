from tkinter import *
import MDtable, sprite, random, evil_sprite
#create table
window = Tk()
window.title("Circle Gets The Square")
my_table = MDtable.Table(window)
score_solo = 0

player_s = sprite.Sprite(table=my_table, width=75, height=75, x_posn=2500, y_posn=525, color="green", x_speed=40, y_speed=40)
evil_sprite1 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite2 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite3 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite4 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite5 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite6 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite7 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite8 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite9 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
evil_sprite10 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
death1 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death2 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death3 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death4 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death5 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death6 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death7 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death8 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death9 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)
death10 = sprite.Sprite(table=my_table, width=100, height=100, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050), color="black", x_speed=0, y_speed=0)




def game_flow():
    global score_solo

    if death1.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death2.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death3.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death4.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death5.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death6.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death7.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death8.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death9.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    if death10.detect_collision(player_s) == True:
        my_table.remove_item(player_s)
    

    if player_s.detect_collision(evil_sprite1) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite1)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite2) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite2)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite3) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite3)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite4)== True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite4)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite5) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite5)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)
    if player_s.detect_collision(evil_sprite6) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite6)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite7) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite7)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite8) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite8)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite9)== True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite9)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)

    if player_s.detect_collision(evil_sprite10) == True:
        score_solo = score_solo + 1
        my_table.remove_item(evil_sprite10)
        my_table.draw_score(score_solo)
        if(score_solo >= 50):
            score_solo = "Ya Win"
            my_table.draw_score(score_solo)
            
    window.after(50, game_flow)

def restart_game(master):
    global evil_sprite1,evil_sprite2,evil_sprite3,evil_sprite4,evil_sprite5,evil_sprite6,evil_sprite7,evil_sprite8,evil_sprite9,evil_sprite10
    evil_sprite1 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite2 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite3 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite4 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite5 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite6 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite7 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite8 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite9 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    evil_sprite10 = evil_sprite.Evil_sprite(table=my_table, width=50, height=50, x_posn=random.randint(0, 4475), y_posn=random.randint(0, 1050))
    game_flow()

window.bind("<Left>", player_s.move_left)
window.bind("<Right>", player_s.move_right)
window.bind("<Up>", player_s.move_up)
window.bind("<Down>", player_s.move_down)
window.bind("<space>", restart_game)

game_flow()
window.mainloop

