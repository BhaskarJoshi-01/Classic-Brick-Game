import numpy
from objects import *
from bricks import *
import math


class Ball:
    def __init__(self, vx, vy, x, y, screen_array):
        self.vx = vx
        self._x = x
        self.vy = vy
        self._y = y
        if(screen_array[self._x][self._y] == ' '):
            screen_array[self._x][self._y] = '⬤'

    def update_ball_inscreen(self, screen_array):
        if(screen_array[self._x][self._y] == ' '):
            screen_array[self._x][self._y] = '⬤'

    # def vel(self,screen_array,tx,ty,cbrick):
    #     previous_x=self._x
    #     vx_sign=sign(self.vx)
    #     previous_y=self._y
    #     vy_sign= sign(self.vy)
    #     t2x=tx-vx_sign
    #     t2y=ty-vy_sign
    #     #reversing vel
    #     if(screen_array[t2x][ty]!=' ' and screen_array[tx][t2y]!=' '):
    #         self.vx=-self.vx
    #         self.vy=-self.vy
    #         cbrick.remove_brick_inscreen(screen_array,t2x,ty)
    #         cbrick.remove_brick_inscreen(screen_array,tx,t2y)
    #         tx=previous_x
    #         ty=previous_y
    #     elif(screen_array[t2x][ty]!=' '):
    #         cbrick.remove_brick_inscreen(screen_array,t2x,ty)
    #         self.vy=-self.vy
    #         tx=tx-vx_sign

    #     elif(screen_array[tx][t2y]!=' '):
    #         cbrick.remove_brick_inscreen(screen_array,tx,t2y)
    #         self.vx=-self.vx
    #         ty=ty-vy_sign

    #     elif(screen_array[tx][ty]!=' '):
    #         cbrick.remove_brick_inscreen(screen_array,tx,ty)
    #         self.vx=-self.vx
    #         self.vy=-self.vy

    #     return(tx,ty)

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
                    self.vx = -self.vx
                    return 1
                else:
                    screen_array[previous_x][previous_y] = ' '
                    return -2
            else:
                screen_array[previous_x][previous_y] = ' '
                return -2
        else:
            # size=bricks.size
            array = [bricks_font_color[i]+bricks_color[i]+bricks[i]
                     [1]+Style.RESET_ALL for i in range(0, bricks.size)]
            screen_array[previous_x][previous_y] = ' '
            point_is = 1

            if((tmpx-5) <= 0):
                self.vx = -self.vx
                temp_val = 5-tmpx
                tmpx = 5+temp_val
                if(tmpy <= 2):
                    self.vy = -self.vy
                    temp_val = 2-tmpy
                    tmpy = 2+temp_val
                elif(tmpy >= width-2):
                    self.vy = -self.vy
                    temp_val = width-2-tmpy
                    tmpy = width-2+temp_val
                self._x = tmpx
                self._y = tmpy
            elif((tmpy-2) <= 0):
                self.vy = -self.vy
                temp_val = -tmpy+2
                tmpy = temp_val+2
            elif((tmpy+2) >= width):
                self.vy = -self.vy
                temp_val = width-tmpy-2
                tmpy = width+temp_val-2
            else:
                sign_vx=sign(self.vx)
                sign_vy=sign(self.vy)
                ball_temp=grid_cross((self._x,self._y),(tmpx,tmpy))
                cur_x=self._x
                cur_y=self._y
                f2=1
                i=0
                for i in range(1,len(ball_temp)):
                    if(screen_array[ball_temp[i][0]][ball_temp[i][1]]!=' '):
                        if((cur_x+1,cur_y+1)==(ball_temp[i][0],ball_temp[i][1]) or 
                            (cur_x-1,cur_y-1)==(ball_temp[i][0],ball_temp[i][1]) or 
                            (cur_x-1,cur_y+1)==(ball_temp[i][0],ball_temp[i][1]) or 
                            (cur_x+1,cur_y-1)==(ball_temp[i][0],ball_temp[i][1])):
                            self.vx=-self.vx
                            self.vy=-self.vy
                        elif((cur_x,cur_y+1)==(ball_temp[i][0],ball_temp[i][1]) or 
                            (cur_x,cur_y-1)==(ball_temp[i][0],ball_temp[i][1])):
                            self.vy=-self.vy
                        elif((cur_x+1,cur_y)==(ball_temp[i][0],ball_temp[i][1]) or
                            (cur_x-1,cur_y)==(ball_temp[i][0],ball_temp[i][1])):
                            self.vx=-self.vx
                        cbrick.remove_brick_inscreen(screen_array,ball_temp[i][0],ball_temp[i][1])
                        tmpx=cur_x
                        tmpy=cur_y
                        break
                    else:
                        cur_x=ball_temp[i][0]
                        cur_y=ball_temp[i][1]
            if(screen_array[tmpx][tmpy]==' '):
                self._x=tmpx
                self._y=tmpy
                screen_array[tmpx][tmpy]='⬤'
                return 1

                    