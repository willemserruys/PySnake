import pygame
import sys
from pgu import gui

    
    
app = gui.Desktop()
app.connect(gui.QUIT,app.quit,None)

img = gui.Image("snake2.jpg")

PlayButton = gui.Button("Play",width = 100, height = 50)
HighScoreButton = gui.Button("High Score",width = 100, height = 50)
VolumeButton = gui.Button("Volume",height = 50)

c = gui.Container(width=640,height=480,icon = img)


c.add(PlayButton,200,200)
c.add(HighScoreButton,320,200)
c.add(VolumeButton,600,440)

app.run(c)





