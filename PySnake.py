import pygame, sys
from UI.StartScreen import *
from UI.InputBox import *
from Logging.Log import Logger

WIDTH = 640
HEIGHT = 480

display = pygame.display.set_mode((640,480),0,32)

start = StartScreen(display)
start.Show()




if start.Decision is StartScreenDecisionEnum.PLAY:
    Logger.LogInfo('Play Screen Activated')
    print(1)
if start.Decision is StartScreenDecisionEnum.HIGH_SCORE:
    Logger.LogInfo('High Score Screen Activated')
    print(2)