import pygame, sys
from pygame.locals import *
from enum import Enum

from Log import Logger

class Button():
    def CheckIfWithinBorders(self,pos):
        x=pos[0]
        y=pos[1]
        if (x> self.LEFT and x< self.LEFT + self.WIDTH and y> self.TOP and y<self.TOP+self.HEIGHT):
            return True
        else:
            return False
            
    def DrawButton(self,display,color,thickness):
        pygame.draw.polygon(display,color,[(self.LEFT,self.TOP),(self.LEFT+self.WIDTH,self.TOP),(self.LEFT+self.WIDTH,self.TOP+self.HEIGHT),(self.LEFT,self.TOP+self.HEIGHT)],thickness)
                
    def __init__(self,x,y,width,height):
        self.LEFT  = x
        self.TOP = y
        self.WIDTH = width
        self.HEIGHT = height
                
class ScreenBase():
    def __init__(self,screenWidth,screenHeight):
        pygame.init()
        
        #General Properties
        self.DISPLAY=pygame.display.set_mode((screenWidth,screenHeight),0,32)  
        self.DecisionMade = False
        self.previousMousePress = False
    
    def DisplayButton(self,button,mousePos,display,color,thickness):
        if(button.CheckIfWithinBorders(mousePos)):
                button.DrawButton(display,color,thickness)
    
    def CheckEvents(self):                
        for event in pygame.event.get():
            if event.type==QUIT:
                self.Quit()
        pygame.display.update()
    
    def Quit(self):
        Logger.LogInfo('Exit Screen')
        pygame.quit()
        sys.exit
    