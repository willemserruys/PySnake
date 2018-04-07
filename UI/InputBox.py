
import pygame, sys
from enum import Enum

from UI.Base.ScreenBase import *
from Logging.Log import Logger

class InputDecisionEnum(Enum):
    OK = 1


class InputBox(ScreenBase):
    def __init__(self,screenWidth,screenHeight):
        super().__init__(screenWidth, screenHeight)
        myfont = pygame.font.SysFont("monospace", 30)   
        Logger.LogInfo('StartScreen Initialized')
        
        #Functionality of the form
        while not self.DecisionMade:
            mousePos = pygame.mouse.get_pos()
            label = myfont.render("Some text!", 1, (255,255,0))
            self.DISPLAY.blit(label, (10, 10))
            if pygame.mouse.get_pressed()[0] and not previousMousePress:              
                previousMousePress = True
            if not pygame.mouse.get_pressed()[0]:
                previousMousePress = False
                            
            self.CheckEvents()
            
        self.Quit()
            
