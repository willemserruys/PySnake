
import pygame, sys
from pygame.locals import *
from enum import Enum

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

class DecisionEnum(Enum):
    PLAY = 1
    HIGH_SCORE = 2

class StartScreen():
    def __init__(self,screenWidth,screenHeight):
        SCREEN_WIDTH = screenWidth
        SCREEN_HEIGHT = screenHeight
        
        BACKGROUND_IMAGE = pygame.image.load("snake.jpg")
        BACKGROUND_IMAGE_2 = pygame.image.load("snake2.jpg")
        DISPLAY=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
        
        WHITE=(255,255,255)
        BLACK=(0,0,0)
        
        pygame.init()

        self.PlayButton = Button(370,240,170,75)
        self.HighScoreButton = Button(370,320,170,120)
        self.VolumeButton = Button(585,430,45,45)
        self.Mute = False
        self.DecisionMade = False
        
        previousMousePress = False
        while not self.DecisionMade:
            mousePos = pygame.mouse.get_pos()
            DISPLAY.blit(BACKGROUND_IMAGE,(0,0))
         
            once = True
            if pygame.mouse.get_pressed()[0] and not previousMousePress:
                if self.VolumeButton.CheckIfWithinBorders(mousePos):
                    self.Mute = not self.Mute
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
                DISPLAY.blit(BACKGROUND_IMAGE,(0,0))
            else:
                DISPLAY.blit(BACKGROUND_IMAGE_2,(0,0))
                
            self.DisplayButton(self.PlayButton,mousePos,DISPLAY,BLACK,4)
            self.DisplayButton(self.HighScoreButton,mousePos,DISPLAY,BLACK,4)
            self.DisplayButton(self.VolumeButton,mousePos,DISPLAY,BLACK,4)

            
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            
        pygame.quit()
        sys.exit
        
    def DisplayButton(self,button,mousePos,display,color,thickness):
        if(button.CheckIfWithinBorders(mousePos)):
                button.DrawButton(display,color,thickness)
    

