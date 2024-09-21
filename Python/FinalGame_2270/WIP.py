# importing the libraries
import pygame, sys, random
from pygame.locals import *

# setting up pygame
pygame.init()
mainClock = pygame.time.Clock()
FPS = 60

# setting up the window
windowWidth = 800
windowHeight = 800

# create the screen
screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)

# changing title and icon
pygame.display.set_caption(" Something Fishy")
icon = pygame.image.load("Python/FinalGame_2270/images/shoal.png")
pygame.display.set_icon(icon)

# levels and difficulties
level = 1
# # difficulty setting
# numberFish = 3 # starting number of fish on the screen

# # setting up player and good items
# fishCounter = 0
# newFish = 50
# fishSize = 30

# # creating fish and collisions
# fishImage1 = pygame.image.load("Python/FinalGame_2270/images/fish1.png")
# fishImage2 = pygame.image.load("Python/FinalGame_2270/images/fish2.png")


# fishes = []
# for i in range(numberFish):
#     fishes.append(pygame.Rect(random.randint(0,windowWidth - fishSize), random.randint(0, windowHeight - fishSize), fishSize, fishSize))


# main character
player_cat = pygame.Rect(10, 750, 50, 50)
player1Img = pygame.image.load("Python/FinalGame_2270/images/Kitty1.jpg")
playerStretchedImage = pygame.transform.scale(player1Img, (50,50))

# enemy
class enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Background
background = pygame.transform.scale(pygame.image.load('Python/FinalGame_2270/images/background.jpg').convert(), (windowHeight, windowHeight))

# player movement variables
moveDown = False
moveUp = False
moveRight = False
moveLeft = False

moveSpeed = 6

# Player Movement
'''class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        self.player_cat = pygame.Rect(10, 750, 50, 50)
        player1Img = pygame.image.load('cat-in-black-silhouette.png')
        self.playerStretchedImage = pygame.transform.scale(player1Img, (50,50))'''




# Creating the scoring system
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 28)

textX = 15
textY = 15

score_rect = Rect(10,10,10,10)

delay = 0.1

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x,y))

def paused():
    font = pygame.font.SysFont('arial', 80)

fishCounter = 0
newFish = 30
fishSize = 50

fishes = ["Python/FinalGame_2270/images/fish1.png", "Python/FinalGame_2270/images/fish2.png", "Python/FinalGame_2270/images/fish3.png"]
sprites = pygame.sprite.Group()
class Fish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(random.choice(fishes))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, windowWidth)
        self.rect.y = random.randint(0, windowHeight)
    def update(self):
        pygame.Rect.update(self.rect.x, self.rect.y)

# fish = Fish()
# sprites.add(fish)

# Game Loop
running = True
while running:
    screen.fill((173, 216, 230))


    # Background Image
    #screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN: # when buttons are pressed, player is able to move
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveDown = True
                moveUp = False

        if event.type == KEYUP: # when no buttons are pressed, player stays stationary
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


        fish = Fish()
        sprites.add(fish)

        # if event.type == MOUSEBUTTONUP:
        #     fishes.append(pygame.rect(event.pos[0], event.pos[1], fishSize, fishSize))

    # move the player
    if moveDown and player_cat.bottom < windowHeight:
        player_cat.top += moveSpeed
    if moveUp and player_cat.top > 0:
        player_cat.top -= moveSpeed
    if moveLeft and player_cat.left > 0:
        player_cat.left -= moveSpeed
    if moveRight and player_cat.right < windowWidth:
        player_cat.right += moveSpeed

    fishCounter += 1
    if fishCounter >= newFish:
        fishCounter = 0
        fishes.append(pygame.Rect(random.randint(0,windowWidth - fishSize), random.randint(0,windowHeight - fishSize), fishSize, fishSize))

    for i in fishes:
        screen.blit(i)


    # collision detection
    for fish in fishes[:]:
        # print(f"Player rect at: {player_cat}")
        # print(f"Fish at {i}")
        if player_cat.colliderect(fish):
            fishes.remove(fish)
            score_value += 30

    # levels
    if score_value == 500 and level == 1:
        level += 1
        # add new dog
        #enemies.append(dog(0,0))
        # change how often items drop
    elif score_value == 500 and level == 2:
        level += 1

    # draw the window on the screen
    screen.blit(playerStretchedImage, player_cat)

    mainClock.tick(FPS)
    show_score(textX, textY)
    pygame.display.update()

