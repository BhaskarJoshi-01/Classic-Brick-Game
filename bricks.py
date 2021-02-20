import numpy
from objects import *
import random as rnd
from colorama import Fore, Back, Style
from startingvalues import *

# sys_random = rnd.SystemRandom()
# rnd.seed(10)
bricks_life = [0, 1, 2, 1000]
size_of_str = 6
bricks = np.array(["[1lef]", "[2lef]",
                   "[3lef]", "[Xlef]"])

bricks_color = np.array([bred, byellow, bgreen, bblue])
# b_1 = "0&0&0&0&0&0&0&0&0&0"+" " + "1&1&1&1&1&1&1&1&1&1" + \
#     " "+"0&0&0&0&0&0&0&0&0&0"+" " + "1&1&1&1&1&1&1&1&1&1" + \
#         " "+"2&2&2&2&2&2&2&2&2&2"+" "+"0&0&0&0&10&0&0&0&0"

# b_2 = "1&1&1" + \
#     " "+"0&0&0"+" " + "0&0&0"+" "+"1&1&1"+" "+"1&1&1"
# b_3 = "0&0&0&0&0&0&0&0&0&0" + \
#     " "+"0&0&0&0&0&0&0&0&0&0"+" " + "0&0&0&0&0&0&0"+" " + "0&0&0&0&0&0&0"+" " + "0&0&0&0&0&0&0"+" " + "0&0&0&0&0&0&0"

# b_4 = "0&0&0&0&0&0&0&0&0&0"+" " + "1&1&1&1&1&1&1&1&1&1" + \
#     " "+"0&0&0&0&0&0&0&0&0&0"+" " + "1&1&1&1&1&1&1&1&1&1" + \
#         " "+"0&0&0&0&0&0&0&1&1&0"


b_5 = "0&0&0&0&0&0&0&0&0&0"+" " + "1&1&1&1&1&1&1&1&1&1" + \
    " "+"0&0&0&0&0&0&0&0&0&0"+" " + "1&1&1&1&1&1&1&1&1&1" + \
        " "+"0&0&0&1&0&0&0&1&0&0"


bricks_font_color = np.array([fyellow, fred, fblue, fgreen])
brick_orientation = np.array([b_5])
brick_orientation_size = brick_orientation.size


class Brick_inherit:
    def __init__(self, btype, x, y):
        self.color = bricks_color[btype]+bricks_font_color[btype]
        self.type = btype
        self.life = bricks_life[btype]
        self.startingx = x
        self.startingy = y

    def downgrade_blife(self, value, go_through):

        score = 0
        score = self.update_score(go_through)+score
        if(go_through):
            self.life = 0
            self.type = self.life-1
        elif(self.type != 3):
            self.life = bricks_life[self.type]
            self.type = self.type-1

        # if(self.type == 3):
        #     pass
        # else:
        #     self.life = bricks_life[self.type]
        #     self.type = self.type-1

            return (self.life, self.type, score)
        return(self.life, self.type, score)

    def bricks_color_change(self, btype):
        self.color = bricks_color[btype]+bricks_font_color[btype]
        return (bricks_color[btype]+bricks_font_color[btype])

    def retxy(self):
        return (self.startingx, self.startingy)

    def update_score(self, go_through):
        score = 0
        if(not go_through):
            score = score+50
        else:
            if(self.type == 2):
                score = score+150
            elif(self.type == 1):
                score = score+100
            elif(self.type == 0):
                score = score+50
            else:
                score = score+200
        return score


class Bricks:
    def __init__(self):
        self.brick_start_x = brick_starting_x
        self.sys_random=rnd.SystemRandom()
        self.brick_type = brick_orientation[self.sys_random.randint(0, ((brick_orientation_size)-1))].split()
        self.brick_start_y = brick_starting_y
        self.brick_data = np.array([])
        arr=[]
        for i in range(1,30):
            arr.append(i)
        self.poweruparray = arr
        for i in range(0, size_of_str):
            self.poweruparray[i] = size_of_str
            self.poweruparray[i] -= i

    def update_bricks_inscreen(self, screen_array):
        temp = 0
        bricks_array = np.array(self.brick_type)
        temp_data_brick = []
        bricks_array_size = bricks_array.size
        for i in range(0, bricks_array_size):
            bricks_array_len = len(bricks_array[i])
            for j in range(0, bricks_array_len):
                brick_temp = []
                temp = self.brick_start_y
                splited_bricks = np.array(bricks_array[i].split('&'))
                splited_bricks_size = splited_bricks.size
                for k in range(0, splited_bricks_size):
                    posn = splited_bricks[k]
                    brick_temp.insert(k, Brick_inherit(
                        int(posn), self.brick_start_x+i, temp))
                    for z in range(0, 6):
                        alpha = bricks_color[int(
                            posn)] + bricks_font_color[int(posn)]
                        screen_array[self.brick_start_x+i][temp] = alpha + \
                            bricks[int(posn)][z] + "\033[0m"
                        temp = temp+1

                temp_data_brick.append(brick_temp)
            self.brick_data = np.array(temp_data_brick)

    def remove_brick_inscreen(self, screen_array, x, y, go_through):
        """ This function is used to remove bricks that are being hit
        """
        pnt1 = y
        f = 0
        pnt = 10  # sum of col arr
        pnt2 = pnt1
        if(screen_array[x][pnt1][5] == 'P'):
            return (0, 0)
        index = [0, 0]
        while (screen_array[x][pnt1][pnt] != '['):
            # screen_array[x][pointer_1] = ' '
            pnt1 = pnt1-1
            if(screen_array[x][pnt1] == '⬤' or screen_array[x][pnt1] == ' '):
                len_val = len(screen_array[x][pnt1-1])
                if((len_val) >= 3):
                    screen_array[x][pnt1] = screen_array[x][1+pnt1]
                    if(screen_array[x][pnt1-1][pnt] == ']'):
                        break
                else:
                    i = pnt1+1
                    while(screen_array[x][i][pnt] != ']' or screen_array[x][i][pnt] != '['):
                        if (screen_array[x][i][pnt] != ']'):
                            pnt1 = i-5
                            break
                        elif(screen_array[x][i][pnt] != ']'):
                            pnt1 = i-6
                            break
                        i = i+1
                        if(len(screen_array[x][i]) < 2):
                            break
                    else:
                        continue
                    break

        till_i = self.brick_data.shape[0]
        for i in range(0, till_i):
            index[0] = i
            till_j = self.brick_data[i].size
            for j in range(0, till_j):
                index[1] = j
                fg = 0
                if((x, pnt1) == self.brick_data[i][j].retxy()):
                    fg = 1
                if(fg):
                    break
                else:
                    fg = 0
            else:
                continue
            break
        pos0 = index[0]
        pos1 = index[1]
        (life, btype, score_) = self.brick_data[pos0][pos1].downgrade_blife(
            1, go_through)
        k_color = self.brick_data[pos0
                                  ][pos1].bricks_color_change(btype)
        temp = 0

        if(life < 1):
            temp = pnt1
            for z in range(0, size_of_str):
                screen_array[x][temp] = ' '
                temp = temp+1
        else:
            temp = pnt1
            for z in range(0, size_of_str):
                screen_array[x][temp] = k_color+bricks[btype][z]+"\033[0m"
                temp = temp+1
        powerup_randomval = self.sys_random.choice(self.poweruparray)
        powerup_randomval=2
        return (score_, powerup_randomval)
