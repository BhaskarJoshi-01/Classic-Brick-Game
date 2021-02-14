from objects import *
from colorama import Fore, Back, Style

class paddle:
    def __init__(self,cur_X,cur_Y,cur_type):
        self.cur_X=cur_X
        self.cur_Y=cur_Y
        self.type=cur_type
    
    def updated_paddle(self,upd_X,upd_Y,upd_type):
        self.cur_X=upd_X
        self.cur_Y=upd_Y
        self.type=upd_type
    
    def updated_paddle_inscreen(self,screen_array):
        # paddle_val=paddle_size[self.type]
        paddle= '$'
        for i in range(0,paddle_size[self.type]):
            paddle+='#'
        paddle+='$'
        # print("added")    
        size_of_paddle=len(paddle)
        j=0
        start=self.cur_X-((int)(size_of_paddle/2))-1
        end=self.cur_X+((int)(size_of_paddle/2))+2
        #putting blank space in paddle's loc
        for i in range(start,end):
            screen_array[self.cur_Y][i]=' '
        # putting paddle where it has to be
        for i in range(start+1,end-1):
            screen_array[self.cur_Y][i]=paddle[j]
            j=j+1
