from objects import *
from colorama import Fore, Back, Style
from startingvalues import width

class paddle:
    def __init__(self,cur_X,cur_Y,cur_type):
        self.cur_X=cur_X
        self.free_ball=boolean_val[0]
        self.type=cur_type
        self.cur_Y=cur_Y
        self.Stick_powerup=boolean_val[0]
        self.incr_dec_paddle=0
    

    def updated_paddle(self,upd_X,upd_Y,upd_type):
        self.cur_X,self.cur_Y,self.type=upd_X,upd_Y,upd_type
        
    
    def update_type(self,changed_type):
        self.type=changed_type

    
    
    def updatingPS(self,PrintScreen):
        # paddle_val=paddle_size[self.type]
        paddle= '$'
        for i in range(0,paddle_size[self.type]):
            paddle+='#'
        paddle+='$'
        # print("added")    
        size_of_paddle=len(paddle)
        j=0
        start=self.cur_X-((int)(size_of_paddle/2))
        end=self.cur_X+((int)(size_of_paddle/2))+1
        #putting blank space in paddle's loc
        start_val=start-2 if start<=3 else start-3
        end_val = 2+end if end-width+6>0 else 3+end

        for i in range(start_val,end_val):
            if(PrintScreen[self.cur_Y][i]!='⬤' or PrintScreen[self.cur_Y][i]!='|'):
                PrintScreen[self.cur_Y][i]=' '
        

        # for i in range(start,end):
        #     PrintScreen[self.cur_Y][i]=' '
        # putting paddle where it has to be
        for i in range(start,end):
            PrintScreen[self.cur_Y][i]=paddle[j]
            j=j+1
        PrintScreen[self.cur_Y][0]='@'
