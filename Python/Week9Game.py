import pygame, sys, random
from pygame.locals import *


#set up pygame
pygame.init()
mainClock = pygame.time.Clock()

#set up the window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 1000
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Collision Game")

#set up color
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

#set up player and food structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20

player = pygame.Rect(300,100,50,50).
foods = []



#set up movement vriables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6


#running the game loop
while True:
    #checking for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #draw the window on the screen
    pygame.display.update()
