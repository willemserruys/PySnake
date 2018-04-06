import StartScreen

from Log import Logger

start = StartScreen.StartScreen(640,480)

if start.Decision is StartScreen.DecisionEnum.PLAY:
    Logger.LogInfo('Play Screen Activated')
    print(1)
if start.Decision is StartScreen.DecisionEnum.HIGH_SCORE:
    Logger.LogInfo('High Score Screen Activated')
    print(2)