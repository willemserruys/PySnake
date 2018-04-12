import pygame
import random
from enum import Enum
from Snake.Enums import *

class Snake(pygame.sprite.Group): 
    def ConstructSnake(self):
        self.Direction = DirectionEnum.Forward
        body = BodyPart()
        body2 = BodyPart()
        body3 = BodyPart()
        
        body.rect.center = (30,30)
        body2.rect.center = (body.rect.center[0]-20,body.rect.center[1])
        body3.rect.center = (body.rect.center[0]-20,body.rect.center[1])
        
        self.add(body)        
        self.add(body2)     
        self.add(body3)
        
    def Move(self):
        head = self.sprites()[0]
        for x in range(1,len(self.sprites()))[::-1]:
            self.sprites()[x].rect.center =  self.sprites()[x-1].rect.center
        if self.Direction is DirectionEnum.Forward:
            head.rect.center = (head.rect.center[0]+20,head.rect.center[1])
        elif self.Direction is DirectionEnum.Backward:
            head.rect.center = (head.rect.center[0]-20,head.rect.center[1])
        elif self.Direction is DirectionEnum.Up:
            head.rect.center = (head.rect.center[0],head.rect.center[1]-20)
        elif self.Direction is DirectionEnum.Down:
            head.rect.center = (head.rect.center[0],head.rect.center[1]+20)
    
    def EatFood(self,foodBlock):
        allSprites = self.copy()
        self.empty()
        self.add(foodBlock)
        self.add(allSprites.sprites())

class BodyPart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()       

##TODO WIS: verbetering; voedsel mag niet verschijnen op plaats waar slang is
class Food:        
    def __init__(self):
        self.WidthList = []
        self.HeightList = []       
        x = 10
        y = 10       
        while x<640:
            self.WidthList.append(x)
            x=x+20
        
        while y< 480:
            self.HeightList.append(y)
            y=y+20
            
    def GetNewBlock(self):
        random.shuffle(self.WidthList)
        random.shuffle(self.HeightList)
        body = BodyPart()
        body.rect.center = (self.WidthList[0],self.HeightList[0])
        return body
                