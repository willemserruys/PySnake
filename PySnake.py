
from UI.StartScreen import *
from Logging.Log import Logger

start = StartScreen(640,480)

if start.Decision is DecisionEnum.PLAY:
    Logger.LogInfo('Play Screen Activated')
    print(1)
if start.Decision is DecisionEnum.HIGH_SCORE:
    Logger.LogInfo('High Score Screen Activated')
    print(2)