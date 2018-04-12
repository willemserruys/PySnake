
import pygame, sys
from enum import Enum

from UI.Base.ScreenBase import *
from Logging.Log import Logger

class InputBox(ScreenBase):
    def __init__(self,display):
        super().__init__(display)
      
    def Show(self):
        while not self.DecisionMade:
            self.DISPLAY.fill(Color.White)
            self.CheckEvents()
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print(1)
        #Functionality of the form
##        while not self.DecisionMade:
##            mousePos = pygame.mouse.get_pos()
##            label = myfont.render("Some text!", 1, (255,255,0))
##            self.DISPLAY.blit(label, (10, 10))
##            if pygame.mouse.get_pressed()[0] and not previousMousePress:              
##                previousMousePress = True
##            if not pygame.mouse.get_pressed()[0]:
##                previousMousePress = False
##                            
##            self.CheckEvents()
##            
##        self.Quit()
            

##input = InputBox(200,100)
##
##while True:
##    self.DISPLAY.fill(Color.White)
    


