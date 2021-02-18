import time
import numpy as np
from objects import * 
height= 45
width = 165
brick_starting_x=15
brick_starting_y=40
ball_starting_vx=-1
ball_starting_vy=2
ball_starting_posx=41
ball_starting_posy=83
score=0
start_time=time.time()

available_time=500
livesleft=3
paddle_array=np.array([width//2,height-3,2])
