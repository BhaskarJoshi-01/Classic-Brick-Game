import numpy
from objects import *
import random as rnd
from colorama import Fore, Back, Style
from startingvalues import *

sys_random = rnd.SystemRandom()
brick_orientation_size=brick_orientation.size
class Bricks:
    def __init__(self):
        self.brick_start_x=brick_starting_x
        self.brick_type= brick_orientation[sys_random.randint(0,((brick_orientation_size)-1))].split()
        self.brick_start_y=brick_starting_y

    

    def update_bricks_inscreen(self,screen_array):
        temp=0
        bricks_array=np.array(self.brick_type)
        bricks_array_size=bricks_array.size
        for i in range( 0, bricks_array_size):
            bricks_array_len=len(bricks_array[i])
            for j in range(0,bricks_array_len):
                splited_bricks=np.array(bricks_array[i].split('&'))
                temp=self.brick_start_y
                for k in range(0,splited_bricks.size):
                    for z in range(0,6):
                        alpha = bricks_color[int(splited_bricks[k])] + bricks_font_color[int(splited_bricks[k])]
                        screen_array[i+self.brick_start_x][temp] = alpha +bricks[int(splited_bricks[k])][z] + "\033[0m"
                        temp = temp+1
                        # print(str(Back.BLACK+Fore.RED+bricks[int(splited_bricks[k])][z]+Style.RESET_ALL))
                        # for l in range(0,len(screen_array[i+self.brick_start_x][temp-1])):
                        #     print(screen_array[i+self.brick_start_x][temp-1][l])

    # def remove_brick_inscreen(self,screen_array,x,y):
    #     pt1=y
    #     pnt=10
    #     f=0
    #     pt2=pt1
    #     print(screen_array,x,pt2,pnt)
    #     if(screen_array[x][pt2][pnt]==']'):
    #         f=1
    #     while(screen_array[x][pt1][pnt]!='['):
    #         screen_array[x][pt1]=' '
    #         pt1=pt1-1
    #     screen_array[x][pt1]=' '
    #     pt2=pt2+1
    #     if (f):
    #         pass
    #     else:
    #         while(screen_array[x][pt2][pnt]!=']'):
    #             screen_array[x][pt2]=' '
    #             pt2=pt2+1
    #         screen_array[x][pt2]=' '


    def remove_brick_inscreen(self,screen_array,x,y):
        """ This function is used to remove bricks that are being hit
        """
        pointer_1 = y
        pointer_2 = y
        flag = 0 
        if(screen_array[x][pointer_2][10]==']'):
            flag = 1
        while (screen_array[x][pointer_1][10]!='['):
            screen_array[x][pointer_1] = ' '
            pointer_1 -= 1
        screen_array[x][pointer_1] = ' '
        pointer_2 += 1
        if(not flag):
            while (screen_array[x][pointer_2][10]!=']'):
                screen_array[x][pointer_2] = ' '
                pointer_2 += 1
            screen_array[x][pointer_2] = ' '


