from art import *
import numpy as np
from colorama import Fore, Back, Style

ball_graphic = "⬤"

bricks = np.array(["[_|___|___|]", "[___|___|_]",
                   "[_|___|___|]", "[___|___|_]"])

paddle_size = np.array([5, 9, 13])

# brick pattern
b_1 = "0&0&0&0&0&0&0&0&0&0"+" " + "1&1&1&1&1&1&1&1&1&1" + \
    " "+"0&0&0&0&0&0&0&0&0&0"+" " + "1&1&1&1&1&1&1&1&1&1"

# brick pattern
brick_orientation = np.array([b_1])
instructions = print(Fore.YELLOW+art.instructions_art)
print(Back.GREEN+'Press g to start game')
print(Fore.RED+'Press q to quit game')
print()
print()
print(Fore.BLUE+'Press a to move board left')
print()
print()
print(Fore.BLUE+'Press d to move board right')
print(Style.RESET_ALL)


def print_instructions():
    return instructions

def sign(n):
    t1=0
    t2=0
    if(n>0):
        t1=1
    if(n<0):
        t2=1
    return t1-t2