import StartScreen


start = StartScreen.StartScreen(640,480)

if start.Decision is StartScreen.DecisionEnum.PLAY:
    print(1)
if start.Decision is StartScreen.DecisionEnum.HIGH_SCORE:
    print(2)