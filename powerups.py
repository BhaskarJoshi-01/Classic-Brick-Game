import numpy
import math
import time
from paddle import *
from ball import *

powerup_temper=[fred+"1"+"\033[0m",fgreen+"2"+"\033[0m",fyellow+"3"+"\033[0m",fred+"4"+"\033[0m",fgreen+"5"+"\033[0m",fyellow+"6"+"\033[0m"]

class power0:
    def __init__(self,x,y):
        self.active=0
        self.index=0
        self.max_time=10
        self.time_activated=time.time()
        self._x=x
        self._y=y
        self._x=x+5

    def update_time_activated(self):
        self.active=2
        self.time_activated=time.time()
    
    def make_power_active(self):
        self.active=1
        self.time_activated=time.time()

    def check_time(self):
        val=boolean_val[1]
        if(self.active==0):
            return False
        else:
            if((time.time()-self.time_activated-self.max_time)>0):
                self.active=0
                val=boolean_val[0]
        return val

    def ret_status(self):
        val=self.active
        return val
        
    def deactivate_time(self):
        self.time_activated = time.time() - self.max_time


    def update_status(self,value):
        self.active=value

    def update_xy(self,x,y):
        self._x=5+x
        self._y=updatedy+y
    
    def upadate_powerup_inscreen(self,PrintScreen,paddle_end,paddle_start,Paddle):

        if((self.active-1)==0):
            if(self._x<(height-3)):
                temp=powerup_temper[self.index]
                locn=self._x-1
                PrintScreen[locn][self._y]=' '
                PrintScreen[locn+1][self._y]=temp
            elif(self._x>(height-3)):
                self.active=0
            else:
                temp=powerup_temper[self.index]
                locn=self._x-1
                PrintScreen[locn][self._y]=' '
                if((self._y-paddle_start)>=0 and (self._y-paddle_end)<=0):
                    self.active=2
                    return boolean_val[1]
            self._x=self._x+1
            return boolean_val[0]

    def undo(self,Paddle):
        Paddle.update_type(1)
   
    def do (self, Paddle):
        Paddle.update_type(3)

    
class power1(power0):
    def __init__(self,x,y):
        self.active=0
        self.time_activated=time.time()
        self.max_time=self.active+15
        self._x=self.active+x+5
        self._y=self.active+y
        self.index=1

    def undo(self,Paddle):
        Paddle.update_type(1)
    def do (self,Paddle):
        Paddle.update_type(0)


class power2(power0):
    def __init__(self,x,y):
        self.active=0
        self.time_activated=time.time()
        self.max_time=self.active+10
        self._x=self.active+x+5
        self._y=self.active+y
        self.index=2

    def undo(self,ball_class,PrintScreen,ball_index):
        x=ball_class
        #remaining code

    def do(self,ball_class,PrintScreen,ball_index):
        x=ball_class
        
        #remaining code


class power3(power0):
    def __init__(self,x,y):
        self.active,self.index=0,3
        self.time_activated=time.time()
        self.max_time=self.active+5
        self._x=self.active+x+5
        self._y=self.active+y
        

    def undo (self,ball_class):
        ball_class.NeedForSpeed(+2,+2)   

    def do (self,ball_class):
        ball_class.NeedForSpeed(+2,+2)            

class power4(power0):
    def __init__(self,x,y):
        self.index=4
        self.active=0
        self.max_time=self.active+15
        self._x=self.active+x+5
        self._y=self.active+y
        self.time_activated=time.time()

    def undo (self,ball_class):
        ball_class.UltimateFireBall(boolean_val[0])
    def do (self,ball_class):
        ball_class.UltimateFireBall(boolean_val[1])

class power5(power0):
    def __init__(self,x,y):
        self.active=0
        self.time_activated=time.time()
        self.max_time=self.active+20
        self._x=self.active+x+5
        self._y=self.active+y
        self.index=5

    def undo (self):
        # ball_class.NeedForSpeed(2,2)            
        return boolean_val[0]
    def do (self):
        # ball_class.NeedForSpeed(2,2)  
        return boolean_val[1]