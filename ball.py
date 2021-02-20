import numpy
from objects import *
from bricks import *
import math

diff_flag=[-2,-1,0,1,2]


class Ball:
    def __init__(self, vx, vy, x, y, PrintScreen):
        self._x = x
        self._y = y
        # file=open("1.txt","a")
        # print(PrintScreen.shape,self._x,self._y)
        # file.close()
        if(PrintScreen[self._x][self._y] == ' '):
            PrintScreen[self._x][self._y] = '⬤'
        self.vx = vx
        self.vy = vy
        self._thru_ball=boolean_val[0]
        self.SB=boolean_val[0]
        # self.sticky_at_start=boolean_val[1]

    def NewBallOnscreen(self, PrintScreen):
        if(PrintScreen[self._x][self._y] == ' '):
            PrintScreen[self._x][self._y] = '⬤'


    

    def SticknessofBall(self,PrintScreen,x,y):
        PrintScreen[self._x][self._y]=' '
        self._x=x+self._x
        self._y=y+self._y
        PrintScreen[self._x][self._y]='⬤'

    def update_speed(self,x,y):
        self.vx=y+updatedy
        self.vy=x+updatedx

    def UltimateFireBall(self,value):
        self._thru_ball=value

    def update_xandy(self,x,y):
        self._y=(y)+updatedy
        # print("here")
        self._x=(x+updatedx)
    
    def NeedForSpeed(self,x,y):
        self.vx=abs(x)*self.vx
        self.vy=abs(y)*self.vy

    def ret_class_inti(self):
        return (self.vx,self.vy,self._x,self._y)

    def BallMoment(self, PrintScreen, cbrick, paddle_start, paddle_end):
        previous_x = self._x
        tmpx = self._x+self.vx
        previous_y = self._y
        tmpy = self._y+self.vy
        magn_x = abs(self.vx)
        magn_y = abs(self.vy)
        score_is=0
        chosen_val=0
        if(tmpx >= (height-3)):
            if((height-3) == tmpx or self._x<=(height-3)):
                paddle_center=(paddle_end+paddle_start)/2

                # if((tmpy-paddle_end) <= 0 and (tmpy-paddle_start) >= 0):
                    # div = math.floor((paddle_end-paddle_start)/3)
                    # arr = [div+paddle_start, paddle_end-div]
                    


                    # if((arr[0]-tmpy) > 0):
                    #     self.vy = self.vy-1
                    # elif((arr[1]-tmpy) < 0):
                    #     self.vy = self.vy+1
                if((tmpy-paddle_start)>=0 and (tmpy-paddle_end)<= 0):
                    if((tmpy-paddle_center)>0):
                        self.vy=self.vy+math.ceil(abs(paddle_center-tmpy))
                    if((tmpy-paddle_center)<=0):
                        self.vy=self.vy-math.ceil(abs(paddle_center-tmpy))
                    tmpy = previous_y
                    tmpx = previous_x
                    self.vx = -1*self.vx
                    return (diff_flag[3],score_is,chosen_val)
                else:
                    PrintScreen[previous_x][previous_y] = ' '
                    return (diff_flag[0],score_is,chosen_val)
            if((height-3)!=tmpx and self._x>(height-3)):
                PrintScreen[previous_x][previous_y] = ' '
                return (diff_flag[0],score_is,chosen_val)
        else:
            array = [FCofBricks[i]+ShadesOfBricks[i]+bricks[i]
                     [1]+"\033[0m" for i in range(0, bricks.size)]
            PrintScreen[previous_x][previous_y] = ' '

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
                if (not self._thru_ball):
                    sec_flag=1
                    i=0

                    for i in range(1,till_i):
                        g1=ball_temp[i][0]
                        g2=ball_temp[i][1]
                        if(PrintScreen[ball_temp[i][0]][ball_temp[i][1]]!=' '):
                            
                            if((1+cur_x,1+cur_y)==(g1,g2) or 
                                (cur_x-1,cur_y-1)==(g1,g2) or 
                                (cur_x-1,1+cur_y)==(g1,g2) or 
                                (1+cur_x,cur_y-1)==(g1,g2)):
                                self.vx=-1*self.vx
                                self.vy=-1*self.vy
                            elif((cur_x,cur_y+1)==(g1,g2) or 
                                (cur_x,cur_y-1)==(g1,g2)):
                                self.vy=-1*self.vy
                            elif((cur_x+1,cur_y)==(g1,g2) or
                                (cur_x-1,cur_y)==(g1,g2)):
                                self.vx=-1*self.vx
                            (score_is,chosen_val)= cbrick.BricksRemoval(PrintScreen,g1,g2,False)
                            tmpx=cur_x
                            tmpy=cur_y
                            break
                        else:
                            cur_x=g1
                            cur_y=g2

                if (self._thru_ball):
                    for i in range(1,till_i):
                        g1=ball_temp[i][0]
                        g2=ball_temp[i][1]
                        if(PrintScreen[g1][g2]!= '⬤' or
                            PrintScreen[g1][g2]!= '@' or 
                            PrintScreen[g1][g2] != '$' or 
                            PrintScreen[g1][g2] != '#' or 
                            PrintScreen[g1][g2] != '=' or 
                            PrintScreen[g1][g2] != '>' or 
                            PrintScreen[g1][g2] != '<'):
                            if(PrintScreen[g1][g2]!=' '):
                                (score_,choosen_value) = cbrick.BricksRemoval(PrintScreen,g1,g2,boolean_val[1])

            # if(self._thru_ball):
            #     # self._x=tmpx
            #     # self._y=tmpy
            #     pass
            if(PrintScreen[tmpx][tmpy]==' ' and not self._thru_ball):
                PrintScreen[tmpx][tmpy]='⬤'
                self._x=tmpx
                self._y=tmpy
                return (diff_flag[3],score_is,chosen_val)
            elif(self._thru_ball):
                self._x=tmpx
                self._y=tmpy
                PrintScreen[tmpx][tmpy]='⬤'
                return (diff_flag[3],score_is,chosen_val)

                    