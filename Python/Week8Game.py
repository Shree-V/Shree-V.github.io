import pygame, sys, time
from pygame.locals import *

#set up pygame 
pygame.init()

#set up window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

MOVESPEED = 4

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#set up the box data structure
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir':UPRIGHT}
b2 = {'rect': pygame.Rect(200, 20, 20, 20), 'color': GREEN, 'dir':UPLEFT}
b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir':DOWNLEFT}
boxes = [b1,b2,b3]

while True:
    #check for a QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)

    for b in boxes:
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED

        if b['dir'] == DOWNLEFT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED

        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['dir'] == DOWNLEFT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['rect'].top < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        
    pygame.display.update()
    time.sleep(0.02)

