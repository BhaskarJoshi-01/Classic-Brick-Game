import numpy as np
import sys
from startingvalues import *
'''This class creates and displays screen'''
class screen:
    def __init__(self,height,width):
        self.screenarray=np.full((height,width)," ",dtype='<U25')
        self.height=height
        self.width=width
    
    
    def showscreen(self):
        print("\x1b[{}A".format(height + 1))
        till_i=self.height
        till_j=self.width
        for i in range(0,till_i):
            for j in range (0, till_j):
                print(self.screenarray[i][j], end="")
            print()


class Create_Scenery(screen):
    def create_scenery(self): #boder of game
        till_i=self.height
        till_j=self.width
        for i in range(0,till_i):
            for j in range (0, till_j): 
                if( not i or  i==4 or i == till_i-1): #top line and bottom line horizontal ones
                    self.screenarray[i][j] = '@'
                if(not j or j == till_j -1):    #side (left and right lines vertical ones)
                    self.screenarray[i][j] = '@'
                if((not i or i==4 or i == till_i-1) and (not j or j == till_j-1)): #base line
                    self.screenarray[i][j] = '@'
        return self.screenarray

