import numpy
from objects import *
import random as rnd
from colorama import Fore, Back, Style
from startingvalues import *

sys_random = rnd.SystemRandom()
brick_orientation_size = brick_orientation.size
bricks_life = [0, 1, 2, 1000]


class Brick_inherit:
    def __init__(self, btype, x, y):
        self.color = bricks_color[btype]+bricks_font_color[btype]
        self.type = btype
        self.life = bricks_life[btype]
        self.startingx = x
        self.startingy = y

    def downgrade_blife(self):
        if(self.type == 3):
            pass
        else:
            self.life = bricks_life[self.type]
            self.type = self.type-1
            return (self.life, self.type)

    def bricks_color_change(self, btype):
        self.color = bricks_color[btype]+bricks_font_color[btype]
        return (bricks_color[btype]+bricks_font_color[btype])

    def retxy(self):
        return (self.startingx, self.startingy)


class Bricks:
    def __init__(self):
        self.brick_start_x = brick_starting_x
        self.brick_type = brick_orientation[sys_random.randint(
            0, ((brick_orientation_size)-1))].split()
        self.brick_start_y = brick_starting_y
        self.brick_data = np.array([])

    def update_bricks_inscreen(self, screen_array):
        temp = 0
        bricks_array = np.array(self.brick_type)
        temp_data_brick = []
        bricks_array_size = bricks_array.size
        for i in range(0, bricks_array_size):
            bricks_array_len = len(bricks_array[i])
            for j in range(0, bricks_array_len):
                splited_bricks = np.array(bricks_array[i].split('&'))
                temp = self.brick_start_y
                brick_temp = []
                for k in range(0, splited_bricks.size):
                    brick_temp.insert(k, Brick_inherit(int(splited_bricks[k]),i+self.brick_start_x,temp))
                    for z in range(0, 6):
                        alpha = bricks_color[int(
                            splited_bricks[k])] + bricks_font_color[int(splited_bricks[k])]
                        screen_array[i+self.brick_start_x][temp] = alpha + \
                            bricks[int(splited_bricks[k])][z] + "\033[0m"
                        temp = temp+1

                temp_data_brick.append(brick_temp)
            self.brick_data=np.array(temp_data_brick)
                        # print(str(Back.BLACK+Fore.RED+bricks[int(splited_bricks[k])][z]+Style.RESET_ALL))
                        # for l in range(0,len(screen_array[i+self.brick_start_x][temp-1])):
                        #     print(screen_array[i+self.brick_start_x][temp-1][l])

    

    # def remove_brick_inscreen(self, screen_array, x, y):
    #     """ This function is used to remove bricks that are being hit
    #     """
    #     pointer_1 = y
    #     pointer_2 = y
    #     flag = 0
    #     if(screen_array[x][pointer_2][10] == ']'):
    #         flag = 1
    #     while (screen_array[x][pointer_1][10] != '['):
    #         screen_array[x][pointer_1] = ' '
    #         pointer_1 -= 1
    #     screen_array[x][pointer_1] = ' '
    #     pointer_2 += 1
    #     if(not flag):
    #         while (screen_array[x][pointer_2][10] != ']'):
    #             screen_array[x][pointer_2] = ' '
    #             pointer_2 += 1
    #         screen_array[x][pointer_2] = ' '


    def remove_brick_inscreen(self, screen_array, x, y):
        """ This function is used to remove bricks that are being hit
        """
        pnt1 = y
        f = 0
        pnt=10 #sum of col arr
        pnt2 = pnt1
        index=[0,0]
        while (screen_array[x][pnt1][pnt] != '['):
            # screen_array[x][pointer_1] = ' '
            pnt1 = pnt1-1

        till_i=self.brick_data.shape[0]
        for i in range(0,till_i):
            till_j=self.brick_data[i].size
            index[0]=i
            for j in range(0,till_j):
                index[1]=j
                if((x,pnt1)==self.brick_data[i][j].retxy()):
                    break
            else:
                continue
            break
        (life,btype)=self.brick_data[index[0]][index[1]].downgrade_blife()
        k_color=self.brick_data[index[0]][index[1]].bricks_color_change(btype)
        temp=pnt1
        if(life==0):
            for z in range(0,6):
                screen_array[x][temp]=' '
                temp=temp+1
        else:
            for z in range(0,6):
                screen_array[x][temp]=k_color+bricks[btype][z]+"\033[0m"
                temp=temp+1