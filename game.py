import time
from screen import *
from objects import *
import os
from inputs import *
from startingvalues import *
from topdata import *
from paddle import *
import numpy as nmp
from bricks import *
from ball import *
import random as rnd
from powerups import *
# printing the instructions in the beginning of the game
import random as rnd



# def gamefunction():

sys_random = rnd.SystemRandom()
# os.system('clear')
print_instructions()
powerups = []
# print(Back.WHITE)

while True:
    key_pressed = input_to()
    # print(key_pressed)
    if (key_pressed == 'q'):
        print(Fore.YELLOW+"You Quit"+Style.RESET_ALL)
        print()
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
bricks = Bricks()

# handling paddle
paddle = paddle(paddle_array[0], paddle_array[1], paddle_array[2])
paddle.updated_paddle_inscreen(screen_array)
# doubt
bricks.update_bricks_inscreen(screen_array)
###################
ball = Ball(ball_starting_vx, ball_starting_vy,
            ball_starting_posx, ball_starting_posy, screen_array)
# ball.update_ball_inscreen(screen_array)
# handling gamedata
# calling the class to update time,lives and score

powerups.append(power0(0, 0))
p0_added=True

powerups.append(power1(0, 0))
p1_added=True

powerups.append(power2(0, 0))
p2_added=True

powerups.append(power3(0, 0))
p3_added=True

powerups.append(power4(0, 0))
p4_added=True

powerups.append(power5(0, 0))
p5_added=True

gamedata = gametop(available_time, score, livesleft)
gamedata.update_gametop_inscreen(screen_array)
sticky_ball_motion = True
sticky_ball_powerup = False
screen_board.showscreen()
tic_toc = time.time()


while True:
    toc = time.time()
    if(toc-tic_toc-0.15 >= 0):
        key = input_to()
        tic_toc = toc
        paddle_start = paddle_array[0] - \
            (int)((paddle_size[paddle_array[2]]+2)/2)
        paddle_end = paddle_array[0]+1 + \
            (int)((paddle_size[paddle_array[2]]+2)/2)

        print("\033[0;0H")
        if(key == 'a' or key == 'd'):
            if (key == 'a'):
                if((paddle_start-4) > 0):
                    # moving paddle to 3 unit left
                    paddle_array[0] = paddle_array[0]-3
                    if(sticky_ball_motion):
                        ball.ball_sticky_movement(screen_array, 0, -3)
                    paddle.updated_paddle(
                        paddle_array[0], paddle_array[1], paddle_array[2])

            if(key == 'd'):
                if((paddle_end+3) < width):
                    # moving paddle to 3 unit right
                    paddle_array[0] = paddle_array[0]+3
                if(sticky_ball_motion):
                    ball.ball_sticky_movement(screen_array, 0, 3)
                paddle.updated_paddle(
                    paddle_array[0], paddle_array[1], paddle_array[2])
            # updating paddle so that it could move in one key down
            # if(sticky_ball_motion):
            #     ball.ball_sticky_movement(screen_array,0,-3)
            # paddle.updated_paddle(paddle_array[0],paddle_array[1],paddle_array[2])

            # paddle.updated_paddle(paddle_array[0],paddle_array[1],paddle_array[2])

        if (key == 'q'):
            print(Fore.YELLOW+"You Quit"+Style.RESET_ALL)
            print()
            break
        if (key == ' '):
            sticky_ball_motion = False

        current_time = time.time()
        available_time = available_time-current_time+start_time
        start_time = current_time
        if(available_time < 0):
            print(Fore.YELLOW + art.timeover_art)
            break
        # ball.update_ball_inscreen(screen_array)
        if(not sticky_ball_motion):

            (ball_return_val, score_is, chosen_val) = ball.ball_motion(
                screen_array, bricks, paddle_start, paddle_end)
            score = score+score_is
            score_is = 0

            tempo = 0
            for i in range(0, 6):
                if(powerup_flag[i]-1 == 0):
                    tempo = tempo+1
            if(chosen_val != 0 and tempo < 3):
                if(powerup_flag[chosen_val-1]-1 != 0):
                    powerup_flag[chosen_val-1] = 1
                else:
                    powerups[chosen_val-1].update_time_activated()

            if(ball_return_val < 0):
                livesleft = livesleft-1
                # print("Lives left : ",livesleft)
                if(livesleft > 0):
                    pass
                else:
                    print(Fore.YELLOW+"Game Over"+Style.RESET_ALL)
                    print()
                    break
                # arr=[i  for i in range(paddle_start,paddle_end) ]
                arr = []
                for i in range(paddle_start, paddle_end):
                    arr.append(i)
                temp_random = rnd.choice(arr)
                ball = Ball(-1, -1, ball_starting_posx,
                            temp_random, screen_array)
                sticky_ball_motion = True

        for i in range(0, various_powerups):
            if(not powerup_flag[i]):
                powerups[i].update_status(0)
                if((i-1) == 0 or i == 0):
                    powerups[i].undo(paddle)
                    # print("i is 1 ",i)
                elif((i-5) == 0):
                    # print("i is 2 ",i)
                    sticky_ball_powerup = powerups[i].undo()
                elif(i-4 == 0):
                    # print("i is 3 ",i)
                    powerups[i].undo(ball)

            else:
                if(powerups[i].ret_status() == 0):

                    (bavx, bavy, bax, bay) = ball.ret_class_inti()
                    powerups[i].update_xy(bax, bay)
                    powerups[i].make_power_active()

                if(powerups[i].ret_status() == 1):
                    ret_value = powerups[i].upadate_powerup_inscreen(
                        screen_array, paddle_end, paddle_start, paddle)
                    if(ret_value == boolean_val[1]):
                        if((i-1) == 0 or (i == 0)):
                            powerups[i].do(paddle)
                        elif((i-3) == 0 or (i-4) == 0):
                            powerups[i].do(ball)
                        elif((i-5) == 0):
                            sticky_ball_powerup = powerups[i].do()

                    if(powerups[i].ret_status() == 0):
                        powerup_flag[i] = 0

                if(powerups[i].ret_status() == 2):
                    if((i-1) == 0 or (i == 0)):
                        powerups[i].do(paddle)
                    if(not powerups[i].check_time()):
                        powerup_flag[i] = 0
                        if((i-1) == 0 or (i == 0)):
                            powerups[i].undo(paddle)
                        elif((i-3) == 0 or (i-4) == 0):
                            powerups[i].undo(ball)
                        elif((i-5) == 0):
                            sticky_ball_powerup = powerups[i].undo()

        gamedata.update_gametop(available_time, score, livesleft)
        gamedata.update_gametop_inscreen(screen_array)
        paddle.updated_paddle_inscreen(screen_array)
        # print(Style.RESET_ALL)
        screen_board.showscreen()

        if(sticky_ball_powerup):
            (bavx, bavy, bax, bay) = ball.ret_class_inti()
            if(bax >= (height-3)):
                if((bay-paddle_start) >= 0 and (bay-paddle_end) <= 0):
                    self.sticky_ball_motion = boolean_val[1]


fd = sys.stdin.fileno()
settings = termios.tcgetattr(fd)
settings[3] = settings[3] | termios.ECHO
termios.tcsetattr(fd, termios.TCSADRAIN, settings)

# class Mygame():
#     def __init__(self):
#         self.game=gamefunction()
        
#     def startgame(self):
#         return self.game
