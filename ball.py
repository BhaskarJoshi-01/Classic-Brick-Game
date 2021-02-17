import numpy
from objects import *
from bricks import *
import math

diff_flag=[-2,-1,0,1,2]


class Ball:
    def __init__(self, vx, vy, x, y, screen_array):
        self._x = x
        self._y = y
        if(screen_array[self._x][self._y] == ' '):
            screen_array[self._x][self._y] = '⬤'
        self.vx = vx
        self.vy = vy

    def update_ball_inscreen(self, screen_array):
        if(screen_array[self._x][self._y] == ' '):
            screen_array[self._x][self._y] = '⬤'



    def ball_motion(self, screen_array, cbrick, paddle_start, paddle_end):
        previous_x = self._x
        tmpx = self._x+self.vx
        previous_y = self._y
        tmpy = self._y+self.vy
        magn_x = abs(self.vx)
        magn_y = abs(self.vy)
        if(tmpx >= (height-3)):
            if((height-3) == tmpx):
                if((tmpy-paddle_end) <= 0 and (tmpy-paddle_start) >= 0):
                    div = math.floor((paddle_end-paddle_start)/3)
                    arr = [div+paddle_start, paddle_end-div]

                    if((arr[0]-tmpy) > 0):
                        self.vy = self.vy-1
                    elif((arr[1]-tmpy) < 0):
                        self.vy = self.vy+1
                    # else:
                    #     pass
                    tmpy = previous_y
                    tmpx = previous_x
                    self.vx = -1*self.vx
                    return diff_flag[3]
                else:
                    screen_array[previous_x][previous_y] = ' '
                    return diff_flag[0]
            if((height-3)!=tmpx):
                screen_array[previous_x][previous_y] = ' '
                return diff_flag[0]
        else:
            # size=bricks.size
            array = [bricks_font_color[i]+bricks_color[i]+bricks[i]
                     [1]+Style.RESET_ALL for i in range(0, bricks.size)]
            screen_array[previous_x][previous_y] = ' '
            point_is = 1

            if((tmpx-5) <= 0):
                self.vx = -1*self.vx
                temp_val = 5-tmpx
                tmpx = 5+temp_val
                if((tmpy-2) <= 0):
                    self.vy = -1*self.vy
                    temp_val = 2-tmpy
                    tmpy = 2+temp_val
                elif((tmpy+2) >= width):
                    self.vy = -1*self.vy
                    # temp_val = width-2-tmpy
                    tmpy = 2*width-4-tmpy
                self._y = tmpy
                self._x = tmpx
            elif((tmpy-2) <= 0):
                self.vy = -1*self.vy
                temp_val = -tmpy+2
                tmpy = temp_val+2
            elif((tmpy+2) >= width):
                self.vy = -1*self.vy
                temp_val = width-tmpy-2
                tmpy = width+temp_val-2
            else:
                sign_vx=sign(self.vx)
                f2=1
                sign_vy=sign(self.vy)
                i=0
                ball_temp=grid_cross((self._x,self._y),(tmpx,tmpy))
                cur_x=self._x
                till_i=len(ball_temp)
                cur_y=self._y
                for i in range(1,till_i):
                    g1=ball_temp[i][0]
                    g2=ball_temp[i][1]
                    if(screen_array[ball_temp[i][0]][ball_temp[i][1]]!=' '):
                        
                        if((1+cur_x,1+cur_y)==(g1,g2) or 
                            (cur_x-1,cur_y-1)==(g1,g2) or 
                            (cur_x-1,1+cur_y)==(g1,g2) or 
                            (1+cur_x,cur_y-1)==(g1,g2)):
                            self.vx=-self.vx
                            self.vy=-self.vy
                        elif((cur_x,cur_y+1)==(g1,g2) or 
                            (cur_x,cur_y-1)==(g1,g2)):
                            self.vy=-self.vy
                        elif((cur_x+1,cur_y)==(g1,g2) or
                            (cur_x-1,cur_y)==(g1,g2)):
                            self.vx=-self.vx
                        cbrick.remove_brick_inscreen(screen_array,g1,g2)
                        tmpx=cur_x
                        tmpy=cur_y
                        break
                    else:
                        cur_x=g1
                        cur_y=g2
            if(screen_array[tmpx][tmpy]==' '):
                self._x=tmpx
                self._y=tmpy
                screen_array[tmpx][tmpy]='⬤'
                return diff_flag[3]

                    