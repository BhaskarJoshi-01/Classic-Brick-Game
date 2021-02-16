import time
import numpy as np
height= 40
width = 140
brick_starting_x=15
brick_starting_y=40
score=0
start_time=time.time()

available_time=500
livesleft=3
paddle_array=np.array([width//2,height-3,2])
