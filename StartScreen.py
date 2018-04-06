
import pygame, sys
from enum import Enum

from ScreenBase import *
from Log import Logger

class DecisionEnum(Enum):
    PLAY = 1
    HIGH_SCORE = 2

class StartScreen(ScreenBase):
    def __init__(self,screenWidth,screenHeight):
        super().__init__(screenWidth, screenHeight)
        
        #Local variables
        BACKGROUND_IMAGE = pygame.image.load("snake.jpg")
        BACKGROUND_IMAGE_2 = pygame.image.load("snake2.jpg")        
        BLACK=(0,0,0)
        
        #Properties specific to screen
        self.PlayButton = Button(370,240,170,75)
        self.HighScoreButton = Button(370,320,170,120)
        self.VolumeButton = Button(585,430,45,45)
        self.Mute = False
        
        Logger.LogInfo('StartScreen Initialized')
        
        #Functionality of the form
        while not self.DecisionMade:
            mousePos = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0] and not previousMousePress:
                if self.VolumeButton.CheckIfWithinBorders(mousePos):
                    self.Mute = not self.Mute
                    Logger.LogInfo('%s %s' % ('Mute: ' , str(self.Mute)))
                if self.HighScoreButton.CheckIfWithinBorders(mousePos):
                    self.Decision = DecisionEnum.HIGH_SCORE
                    self.DecisionMade = True
                if self.PlayButton.CheckIfWithinBorders(mousePos):
                    self.Decision = DecisionEnum.PLAY
                    self.DecisionMade = True
                previousMousePress = True
            if not pygame.mouse.get_pressed()[0]:
                previousMousePress = False
                
            if not self.Mute:
                self.DISPLAY.blit(BACKGROUND_IMAGE,(0,0))
            else:
                self.DISPLAY.blit(BACKGROUND_IMAGE_2,(0,0))
                
            self.DisplayButton(self.PlayButton,mousePos,self.DISPLAY,BLACK,4)
            self.DisplayButton(self.HighScoreButton,mousePos,self.DISPLAY,BLACK,4)
            self.DisplayButton(self.VolumeButton,mousePos,self.DISPLAY,BLACK,4)
            
            self.CheckEvents()
            
        self.Quit()
            

        
    

