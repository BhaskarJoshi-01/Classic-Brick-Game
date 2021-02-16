import time
import os
from screen import *
from objects import *
from inputs import *
from startingvalues import *
from topdata import *
from paddle import *
from bricks import *
from ball import *
# printing the instructions in the beginning of the game
import random as rnd

sys_random = rnd.SystemRandom()
# os.system('clear')
print_instructions()
# print(Back.WHITE)

while True:
    key_pressed = input_to()
    # print(key_pressed)
    if (key_pressed == 'q'):
        print(Fore.YELLOW+art.you_quit_art+Style.RESET_ALL)
        exit()
    elif (key_pressed == 'g'):

        break
    else:
        pass
os.system('clear')
# handling screen
screen_board = Create_Scenery(height, width)
# print("hello2")
screen_array = screen_board.create_scenery()
# print("hello3")
bricks=Bricks()

# handling paddle
paddle = paddle(paddle_array[0], paddle_array[1], paddle_array[2])
paddle.updated_paddle_inscreen(screen_array)

bricks.update_bricks_inscreen(screen_array)

ball=Ball(-1,-1,20,20,screen_array)
# ball.update_ball_inscreen(screen_array)
# handling gamedata
# calling the class to update time,lives and score
gamedata = gametop(available_time, score, livesleft)
gamedata.update_gametop_inscreen(screen_array)

tic_toc=time.time()
screen_board.showscreen()


while True:
    toc=time.time()
    key = input_to()
    paddle_start = paddle_array[0]-(int)((paddle_size[paddle_array[2]]+2)/2)
    paddle_end = paddle_array[0]+1+(int)((paddle_size[paddle_array[2]]+2)/2)
    
    
    print('\033[2J')
    if(key=='a' or key =='d'):
        if (key=='a'):
            if((paddle_start-2)>0):
                #moving paddle to 1 unit left
                paddle_array[0]=paddle_array[0]-1

        if(key=='d'):
            if((paddle_end+2)<width):
                #moving paddle to 1 unit right
                paddle_array[0]=paddle_array[0]+1
        #updating paddle so that it could move in one key down
        paddle.updated_paddle(paddle_array[0],paddle_array[1],paddle_array[2])
    

    if (key == 'q'):
        print(Fore.YELLOW+art.you_quit_art+Style.RESET_ALL)
        break

    current_time = time.time()
    available_time = available_time-current_time+start_time
    start_time = current_time
    if(available_time < 0):
        print(Fore.YELLOW+ art.timeover_art)
        break
    # ball.update_ball_inscreen(screen_array)


    gamedata.update_gametop(available_time, score, livesleft)
    gamedata.update_gametop_inscreen(screen_array)
    paddle.updated_paddle_inscreen(screen_array)

    # print(Style.RESET_ALL)
    screen_board.showscreen()
