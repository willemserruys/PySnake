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

        body.rect.center = (30, 30)
        body2.rect.center = (body.rect.center[0]-20, body.rect.center[1])
        body3.rect.center = (body.rect.center[0]-20, body.rect.center[1])

        self.add(body)
        self.add(body2)
        self.add(body3)

    def Move(self):
        previousHead = self.sprites()[0]
        newHead = BodyPart()
        if self.Direction is DirectionEnum.Forward:
            newHead.rect.center = (
                previousHead.rect.center[0]+20, previousHead.rect.center[1])
        elif self.Direction is DirectionEnum.Backward:
            newHead.rect.center = (
                previousHead.rect.center[0]-20, previousHead.rect.center[1])
        elif self.Direction is DirectionEnum.Up:
            newHead.rect.center = (
                previousHead.rect.center[0], previousHead.rect.center[1]-20)
        elif self.Direction is DirectionEnum.Down:
            newHead.rect.center = (
                previousHead.rect.center[0], previousHead.rect.center[1]+20)
        allSprites = self.copy()
        self.empty()
        self.add(newHead)
        self.add(allSprites.sprites())
        self.remove(self.sprites()[len(self.sprites())-1])

        # previousHead = self.sprites()[0]
        # for x in range(1,len(self.sprites()))[::-1]:
        #     self.sprites()[x].rect.center =  self.sprites()[x-1].rect.center
        # if self.Direction is DirectionEnum.Forward:
        #     previousHead.rect.center = (previousHead.rect.center[0]+20,previousHead.rect.center[1])
        # elif self.Direction is DirectionEnum.Backward:
        #     previousHead.rect.center = (previousHead.rect.center[0]-20,previousHead.rect.center[1])
        # elif self.Direction is DirectionEnum.Up:
        #     previousHead.rect.center = (previousHead.rect.center[0],previousHead.rect.center[1]-20)
        # elif self.Direction is DirectionEnum.Down:
        #     previousHead.rect.center = (previousHead.rect.center[0],previousHead.rect.center[1]+20)

    def UpdateDirection(self, key):
        if key == pygame.K_UP and not self.Direction is DirectionEnum.Down:
            self.Direction = DirectionEnum.Up
        if key == pygame.K_DOWN and not self.Direction is DirectionEnum.Up:
            self.Direction = DirectionEnum.Down
        if key == pygame.K_LEFT and not self.Direction is DirectionEnum.Forward:
            self.Direction = DirectionEnum.Backward
        if key == pygame.K_RIGHT and not self.Direction is DirectionEnum.Backward:
            self.Direction = DirectionEnum.Forward

    def EatFood(self, foodBlock):
        allSprites = self.copy()
        self.empty()
        self.add(foodBlock)
        self.add(allSprites.sprites())

    def DetectCollisionWithItself(self):
        collisionDetected = False
        for x in range(3, len(self.sprites())):
            if pygame.sprite.collide_rect(self.sprites()[0], self.sprites()[x]):
                collisionDetected = True
                if collisionDetected:
                    print(1)
        return collisionDetected


class BodyPart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

# TODO WIS: verbetering; voedsel mag niet verschijnen op plaats waar slang is


class Food:
    def __init__(self):
        self.WidthList = []
        self.HeightList = []
        x = 10
        y = 10
        while x < 640:
            self.WidthList.append(x)
            x = x+20

        while y < 480:
            self.HeightList.append(y)
            y = y+20

    def GetNewBlock(self, sprites):
        inSnake = True

        while inSnake:
            random.shuffle(self.WidthList)
            random.shuffle(self.HeightList)
            body = BodyPart()
            body.rect.center = (self.WidthList[0], self.HeightList[0])
            inSnake = False
            for x in range(0, len(sprites)-1):
                if self.CheckIfPosEqual(sprites[x].rect.center, body.rect.center):
                    print(1)
                    inSnake = True
                    break
        return body

    def CheckIfPosEqual(self, pos1, pos2):
        if pos1[0] == pos2[0] and pos1[1] == pos2[1]:
            return True
        else:
            return False
