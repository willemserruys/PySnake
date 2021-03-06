import pygame, sys
from UI.StartScreen import *
from UI.HighScoreScreen import *
from SnakeScreen import SnakeScreen
from DataAccess.DataBaseConnection import *
import pymysql

WIDTH = 640
HEIGHT = 480

display = pygame.display.set_mode((WIDTH,HEIGHT))

player_name = 'willem' #input("Enter Name ")
print("Welcome, " + player_name)

start = StartScreen(display)
start.Show()
snake = SnakeScreen(display)
data = DataBaseConnection()

                
while(True):
    if start.Decision is StartScreenDecisionEnum.PLAY:
        snake.Show()
        if snake.decision:
            print('you lost, ' + player_name + ", your score was " + str(snake.highscore))
            data.SetHighScore(player_name,snake.highscore)
            snake = SnakeScreen(display)
            start = StartScreen(display)
            start.Show()
            
    if start.Decision is StartScreenDecisionEnum.HIGH_SCORE:
        scr = HighScoreScreen(display)
        scr.Show()
        
        start = StartScreen(display)
        start.Show()
        
