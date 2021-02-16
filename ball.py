import numpy
from objects import *
from bricks import *
import math

class Ball:
    def __init__(self,vx,vy,x,y,screen_array):
        self.vx=vx
        self._x=x
        self.vy=vy
        self._y=y
        if(screen_array[self._x][self._y]==' '):
            screen_array[self._x][self._y]='⬤'
    
    def update_ball_inscreen(self,screen_array):
        if(screen_array[self._x][self._y]==' '):
            screen_array[self._x][self._y]='⬤'

    def vel(self,screen_array,tx,ty,cbrick):
        previous_x=self._x
        vx_sign=sign(self.vx)
        previous_y=self._y
        vy_sign= sign(self.vy)
        t2x=tx-vx_sign
        t2y=ty-vy_sign
        #reversing vel
        if(screen_array[t2x][ty]!=' ' and screen_array[tx][t2y]!=' '):
            self.vx=-self.vx
            self.vy=-self.vy
            cbrick.remove_brick_inscreen(screen_array,t2x,ty)
            cbrick.remove_brick_inscreen(screen_array,tx,t2y)
            tx=previous_x
            ty=previous_y
        elif(screen_array[t2x][ty]!=' '):
            cbrick.remove_brick_inscreen(screen_array,t2x,ty)
            self.vy=-self.vy
            tx=tx-vx_sign
        
        elif(screen_array[tx][t2y]!=' '):
            cbrick.remove_brick_inscreen(screen_array,tx,t2y)
            self.vx=-self.vx
            ty=ty-vy_sign
        
        elif(screen_array[tx][ty]!=' '):
            cbrick.remove_brick_inscreen(screen_array,tx,ty)
            self.vx=-self.vx
            self.vy=-self.vy
        
        return(tx,ty)

    def ball_motion(self,screen_array,cbrick,paddle_start,paddle_end):
        previous_x=self._x
        tmpx=self._x+self.vx
        previous_y=self._y
        tmpy=self._y+self.vy
        magn_x=abs(self.vx)
        magn_y=abs(self.vy)
        if(tmpx>=(height-2)):
            if( tmpy<=paddle_end and tmpy>=paddle_size ):
                ps=paddle_end-paddle_size
                tmpx=previous_x
                tmpy=previous_y
                self.vx=-self.vx
                return 1
            else:
                screen_array[previous_x][previous_y]=' '
                return -2

        





