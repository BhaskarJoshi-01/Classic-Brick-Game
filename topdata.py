from colorama import Fore, Back, Style
import numpy as np


class gametop:
    def __init__(self, timeleft, score, lives_rem):
        self.timeleft = timeleft
        self.livesleft = lives_rem
        self.score = score

    def update_gametop_inscreen(self, screen_array):
        value = np.array([Fore.RED+Back.GREEN+ "\t GAME INFO \t "+"\nYour Score is : "+str(self.score)+"\nLives Remaining : " +
                          str(self.livesleft)+"\nTime Remaining is : "+str(self.timeleft)+Style.RESET_ALL])
        till_i=len(value)
        for i in range(0,till_i):
            till_j=len(value[i])
            for j in range(0,till_j):
                screen_array[1+i][4+j]= value[i][j]

    def update_gametop(self, timeleft, score, lives_rem):
        self.livesleft = lives_rem
        self.timeleft = timeleft
        self.score = score
