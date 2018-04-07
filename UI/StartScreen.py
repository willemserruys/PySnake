
import pygame, sys
from enum import Enum

from UI.Base.ScreenBase import *
from Logging.Log import Logger

class StartScreenDecisionEnum(Enum):
    PLAY = 1
    HIGH_SCORE = 2

class Colors:
    Black = (0,0,0)
    
class StartScreen(ScreenBase):
                  
    def __init__(self,display):
        super().__init__(display)
        
        #Local variables
        self.BACKGROUND_IMAGE = pygame.image.load("UI\SourceFiles\snake.jpg")
        self.BACKGROUND_IMAGE_2 = pygame.image.load("UI\SourceFiles\snake2.jpg")        
        
        #Properties specific to screen
        self.PlayButton = Button(370,240,170,75,display,"")
        self.HighScoreButton = Button(370,320,170,120,display,"")
        self.VolumeButton = Button(585,430,45,45,display,"")
        
        
        Logger.LogInfo('StartScreen Initialized')
        
    def Show(self):
                #Functionality of the form
        while not self.DecisionMade:
            mousePos = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0] and not previousMousePress:
                if self.VolumeButton.CheckIfWithinBorders(mousePos):
                    self.Mute = not self.Mute
                    Logger.LogInfo('%s %s' % ('Mute: ' , str(self.Mute)))
                if self.HighScoreButton.CheckIfWithinBorders(mousePos):
                    self.Decision = StartScreenDecisionEnum.HIGH_SCORE
                    self.DecisionMade = True
                if self.PlayButton.CheckIfWithinBorders(mousePos):
                    self.Decision = StartScreenDecisionEnum.PLAY
                    self.DecisionMade = True
                previousMousePress = True
            if not pygame.mouse.get_pressed()[0]:
                previousMousePress = False
                
            self.DISPLAY.fill(Color.White)  
            if not self.Mute:
                self.DISPLAY.blit(self.BACKGROUND_IMAGE,(0,0))
            else:
                self.DISPLAY.blit(self.BACKGROUND_IMAGE_2,(0,0))
                
            self.DisplayButton(self.PlayButton,mousePos,Color.Black,4)
            self.DisplayButton(self.HighScoreButton,mousePos,Color.Black,4)
            self.DisplayButton(self.VolumeButton,mousePos,Color.Black,4)
            
            self.CheckEvents()                   
        self.Quit()


        
    

