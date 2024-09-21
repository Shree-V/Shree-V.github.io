import pygame

class fish(object):
    images = [pygame.image.load('fish1.png'), pygame.image.load('fish2.png'), pygame.image.load('fish3.png')]
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.imagesCount = 0


class cannedFood(fish):
    image = []
    def draw(self):
        self.hitbox = []


