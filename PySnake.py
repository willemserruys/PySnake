import pygame, sys
from UI.StartScreen import *
from UI.InputBox import *
from Logging.Log import Logger
from SnakeScreen import SnakeScreen

WIDTH = 640
HEIGHT = 480

display = pygame.display.set_mode((640,480),0,32)

start = StartScreen(display)
start.Show()
snake = SnakeScreen(display)

player_name = ""

while(True):
    if start.Decision is StartScreenDecisionEnum.PLAY:
        Logger.LogInfo('Play Screen Activated')
        if  player_name == "" : player_name = input("Enter Name ")
        print("Welcome, " + player_name)
        snake.Show()
        if snake.decision:
            print('you lost, ' + player_name + ", your score was " + str(snake.highscore))
            
            snake = SnakeScreen(display)
            start = StartScreen(display)
            start.Show()

    if start.Decision is StartScreenDecisionEnum.HIGH_SCORE:
        Logger.LogInfo('High Score Screen Activated')
        print(2)
