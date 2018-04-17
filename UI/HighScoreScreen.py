
import pygame, sys
import pymysql

from enum import Enum
from DataAccess.DataBaseConnection import *
from UI.Base.ScreenBase import *
##from Logging.Log import Logger
  
class HighScoreScreen(ScreenBase):
                  
    def __init__(self,display):
        super().__init__(display)
        self.DISPLAY.fill(Color.White)
     
    def Show(self):
        data = DataBaseConnection()
        cursor = data.GetHighScores()
        positionX = 30
        if data.connectionMade:
            for  row in cursor:
                textsurface = Font.MonoSpace(15).render(str(row),False,Color.Black)
                self.DISPLAY.blit(textsurface,(20,positionX))
                positionX+=30
                #Functionality of the form
        while not self.DecisionMade:
            self.CheckEvents()                   
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.DecisionMade = True         
        self.Quit(False)
        

    
    