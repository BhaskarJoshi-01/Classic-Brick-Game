import time
import numpy as np
from objects import * 
height= 35
width = 165
brick_starting_x=10
brick_starting_y=45
ball_starting_vx=-1
ball_starting_vy=2
ball_starting_posx=height-4
ball_starting_posy=width//2 +1
power_up_x=0
power_up_y=0
various_powerups=6
powerup_flag=[0,0,0,0,0,0]
score=0
start_time=time.time()

AVAILABLE_TIME=500
livesleft=3
PA=np.array([width//2,height-3,2])
