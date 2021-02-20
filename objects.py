import numpy as np
from colorama import Fore, Back, Style
import math

paddle_size = np.array([5, 9, 13])

fred = "\033[31m"
fgreen = "\033[32m"
fyellow = "\033[33m"
fblue = "\033[34m"

bred = "\033[41m"
bgreen = "\033[42m"
byellow = "\033[43m"
bblue = "\033[44m"

boolean_val=[False,True]

instructions = print(Fore.YELLOW+"Insrtuctions"+Back.WHITE)
print()
print()
print(Back.GREEN+'Press g to start game')
print()
print()
print(Fore.RED+'Press q to quit game')
print()
print()
print(Fore.BLUE+'Press a to move board left')
print()
print()
print(Fore.RED+'Press SpaceBar to launch Ball')
print()
print()

print(Fore.BLUE+'Press d to move board right')
print(Style.RESET_ALL)

updatedx=0
updatedy=0

def print_instructions():
    return instructions


def sign(n):
    t1 = 0
    t2 = 0
    if(n > 0):
        t1 = 1
    if(n < 0):
        t2 = 1
    return t1-t2


def sign_wrt_line(a, b, c):
    sing = c-a[1]-b*a[0]
    return sing


def check_btw_lines(a, b, c):
    f = 0
    dx = 1e-8
    if((sign_wrt_line(a, b+1, c)*sign_wrt_line(a, b, c+1)) <= dx or (sign_wrt_line(a, b, c)*sign_wrt_line(a, b+1, c+1) <= dx)):
        f = 1
    return True if f else False

def sort_bydist(arr,x,y,flag_check):
    size=len(arr)
    j=0
    a=[]
    val=[]
    for i in arr:
        if(not flag_check):
            v1=math.pow(i[0]-x,2)
            v2=math.pow(i[1]-y,2)
            dist=math.sqrt(v1+v2)
            a.append((dist,(i[0],i[1])))
        else:
            if((j+1)!=size and j!=0):
                v1=math.pow(i[0]-x,2)
                v2=math.pow(i[1]-y,2)
                dist=math.sqrt(v1+v2)
                a.append((dist,(i[0],i[1])))
        j=j+1
    a.sort()
    for i in a:
        val.append(i[1])
    return val




def grid_cross(A,B):
    f=0
    (xA,yA)=A
    coeff=[]
    (xB,yB)=B
    valA=xB-xA
    valB=yB-yA
    (dx,dy)=(valA,valB)
    if(dy/dx>=0):
        pass
    else:
        f=1
        if(dy<=0):
            yA=yA+1
            xB=xB+1
        else:
            yB=yB+1
            xA=xA+1
        
    (dx,dy)=(xB-xA,yB-yA)
    coeff.append(dy/dx)
    result=[]
    coeff.append(yA-xA*coeff[0])
    x=0
    y=0
    j=0
    sigvar=(sx,sy)=(sign(dx),sign(dy))
    x=xA
    grid_start=A
    y=yA
    while((xB+sx)!=x):
        y=yA
        while((yB+sy)!=y):
            if(check_btw_lines(coeff,x,y)):
                result.append((x,y))
            else:
                pass
            y=sy+y
            j=j+1
        x=sx+x
    result=sort_bydist(result,xA,yA,f)
    return result

