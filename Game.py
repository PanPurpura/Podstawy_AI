import pygame as engine
from pygame.locals import *
import sys
from Agent import *

engine.init()

WHITE = (255, 255, 255)

DISPLAYSURF = engine.display.set_mode((720, 480))
FPS = engine.time.Clock()
FPS.tick(60)
DISPLAYSURF.fill(WHITE)
engine.display.set_caption("Project 1")

test_agent = Agent(1)


while True:
    for event in engine.event.get():
        if event.type == QUIT:
            engine.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    test_agent.update(1.0)
    test_agent.draw(DISPLAYSURF, test_agent.position, 5.0)

    engine.display.update()

