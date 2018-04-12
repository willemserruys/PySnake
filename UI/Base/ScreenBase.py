import pygame, sys
from pygame.locals import *
from enum import Enum
import playsound


from Logging.Log import Logger

class Font:
    def MonoSpace(size):       
        return pygame.font.SysFont("monospace", size)

class Color:
    Black = (0,0,0)
    Red = (255,0,0)
    White = (255,255,255)
    
class Button():
    def CheckIfWithinBorders(self,pos):
        x=pos[0]
        y=pos[1]
        if (x> self.LEFT and x< self.LEFT + self.WIDTH and y> self.TOP and y<self.TOP+self.HEIGHT):
            return True
        else:
            return False
            
    def DrawButton(self,color,thickness):
        pygame.draw.polygon(self.DISPLAY,color,[(self.LEFT,self.TOP),(self.LEFT+self.WIDTH,self.TOP),(self.LEFT+self.WIDTH,self.TOP+self.HEIGHT),(self.LEFT,self.TOP+self.HEIGHT)],thickness)
        label = self.FONT.render(self.TEXT,1,Color.Black)
        self.DISPLAY.blit(label,(self.LEFT,self.TOP))
         
    def __init__(self,x,y,width,height,display,text):
        self.LEFT  = x
        self.TOP = y
        self.WIDTH = width
        self.HEIGHT = height
        self.DISPLAY = display
        self.FONT = Font.MonoSpace(15)
        self.TEXT = text
                
class ScreenBase():
    def __init__(self,display):
        pygame.init()
        
        #General Properties
        self.DISPLAY=display
        self.DecisionMade = False
        self.previousMousePress = False
        self.Mute = False
    
    def DisplayButton(self,button,mousePos,color,thickness):
        if(button.CheckIfWithinBorders(mousePos)):
                button.DrawButton(color,thickness)
    
    def CheckEvents(self):                
        for event in pygame.event.get():
            if event.type==QUIT:
                self.Quit()
        pygame.display.update()
    
    def Quit(self,quitScreen=True):
        Logger.LogInfo('Exit Screen')
        if quitScreen: pygame.quit()
        sys.exit
    