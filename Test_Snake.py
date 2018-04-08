import pygame
from UI.Base.ScreenBase import *
from enum import Enum
import random



class DirectionEnum(Enum):
    Forward = 1
    Backward = 2
    Up = 3
    Down = 4

class PlayField:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([640,480])
        self.rect = self.image.get_rect()

class Head(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = ((90,30))

class BodyPart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()

        
        
class Snake(pygame.sprite.Group):
    def __init__(self,head):
        pygame.sprite.Group.__init__(self)
        self.Direction = DirectionEnum.Forward
        self.add(head)
        self.Head = head
        body = BodyPart()
        body.rect.center = (head.rect.center[0]-20,head.rect.center[1])
        self.add(body)
        body2 = BodyPart()
        body2.rect.center = (head.rect.center[0]-20,head.rect.center[1])
        self.add(body2)
        body3 = BodyPart()
        body3.rect.center = (head.rect.center[0]-20,head.rect.center[1])
        self.add(body3)

    def Move(self):
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
        self.Head = foodBlock
        dummyBlock = BodyPart()
        self.add(dummyBlock)
        
        for x in range(0,len(self.sprites())-1)[::-1]:
            self.sprites()[x+1] = self.sprites()[x]
        self.sprites()[0] = foodBlock
            
        
        
class SnakeScreen(ScreenBase):
    def __init__(self,display):
        super().__init__(display)
        display.fill(Color.White)
        
        
class Feed:
        
        
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
               
display = pygame.display.set_mode((640,480),0,32)
screen = SnakeScreen(display)
head = Head()
group = Snake(head)
field = PlayField()
feed = Feed()
block = feed.GetNewBlock()
groupFood = pygame.sprite.Group()
groupFood.add(block)

print(block.rect.center)

UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE,100)

while True:
    screen.CheckEvents()
    display.fill(Color.White)
    group.draw(display)   
    groupFood.draw(display)
    for event in pygame.event.get():
        if event.type==QUIT:
            self.Quit()
        if event.type==pygame.KEYDOWN:
            print("keypress")
            if event.key == pygame.K_UP and not group.Direction is DirectionEnum.Down:
                group.Direction = DirectionEnum.Up
            if event.key == pygame.K_DOWN and not group.Direction is DirectionEnum.Up:
                group.Direction = DirectionEnum.Down
            if event.key == pygame.K_LEFT and not group.Direction is DirectionEnum.Forward:
                group.Direction = DirectionEnum.Backward
            if event.key == pygame.K_RIGHT and not group.Direction is DirectionEnum.Backward:
                group.Direction = DirectionEnum.Forward
            print(group.Direction)
        if event.type==UPDATE:
            game_over = not(pygame.sprite.collide_rect(field,group.Head))
            if game_over:
                screen.Quit()
            group.Move()
            group.draw(display)
            group.update()
            if pygame.sprite.collide_rect(group.Head,groupFood.sprites()[0]):
                group.EatFood(groupFood.sprites()[0])
                block = feed.GetNewBlock()
                groupFood.empty()
                groupFood.add(block)

    