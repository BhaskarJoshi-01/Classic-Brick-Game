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
###################doubt
bricks.update_bricks_inscreen(screen_array)
###################
ball=Ball(ball_starting_vx,ball_starting_vy,ball_starting_posx,ball_starting_posy,screen_array)
# ball.update_ball_inscreen(screen_array)
# handling gamedata
# calling the class to update time,lives and score
gamedata = gametop(available_time, score, livesleft)
gamedata.update_gametop_inscreen(screen_array)

screen_board.showscreen()
tic_toc=time.time()


while True:
    toc=time.time()
    if(toc-tic_toc-0.15>=0):
        key = input_to()
        tic_toc=toc
        paddle_start = paddle_array[0]-(int)((paddle_size[paddle_array[2]]+2)/2)
        paddle_end = paddle_array[0]+1+(int)((paddle_size[paddle_array[2]]+2)/2)
        
        
        print("\033[0;0H")
        if(key=='a' or key =='d'):
            if (key=='a'):
                if((paddle_start-4)>0):
                    #moving paddle to 3 unit left
                    paddle_array[0]=paddle_array[0]-3

            if(key=='d'):
                if((paddle_end+3)<width):
                    #moving paddle to 3 unit right
                    paddle_array[0]=paddle_array[0]+3
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
        ball_return_val=ball.ball_motion(screen_array,bricks,paddle_start,paddle_end)
        if(ball_return_val<0):
            livesleft=livesleft-1
            if(livesleft>0):
                pass
            else:
                print(Fore.YELLOW+art.game_over_art+Style.RESET_ALL)
                break
            ball=Ball(-1,-1,ball_starting_posx,ball_starting_posy,screen_array)
            


        gamedata.update_gametop(available_time, score, livesleft)
        gamedata.update_gametop_inscreen(screen_array)
        paddle.updated_paddle_inscreen(screen_array)

        # print(Style.RESET_ALL)
        screen_board.showscreen()
