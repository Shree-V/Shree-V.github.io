# importing the libraries
import pygame, sys, random
from pygame.locals import *
import time
from pygame import mixer

# setting up pygame
pygame.init()
pygame.mixer.init()
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


# main character
player_cat = pygame.Rect(10, 750, 125, 125)
player1Img = pygame.image.load("Python/FinalGame_2270/images/cat.png")
playerStretchedImage = pygame.transform.scale(player1Img, (125,125))

# enemy
class enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Background
background = pygame.transform.scale(pygame.image.load('Python/FinalGame_2270/images/background.jpg').convert(), (windowHeight, windowHeight))

# Sound Setup
s = 'sound'
meow = pygame.mixer.Sound("Python/FinalGame_2270/sounds/catmeow_music.wav")
bark = pygame.mixer.Sound("Python/FinalGame_2270/sounds/dogbark_music.wav")
gameOver = pygame.mixer.Sound("Python/FinalGame_2270/sounds/gameover_music.wav")
levelUp = pygame.mixer.Sound("Python/FinalGame_2270/sounds/powerup_music.wav")
music = pygame.mixer.music.load("Python/FinalGame_2270/sounds/background_music.wav")
pygame.mixer.music.play(-1)

# player movement variables
moveDown = False
moveUp = False
moveRight = False
moveLeft = False

moveSpeed = 6


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

# Load in images, create an array with the images, create a function the randomly chooses images from this array
fish1 = pygame.image.load("Python/FinalGame_2270/images/Fishie1.png")
fish2 = pygame.image.load("Python/FinalGame_2270/images/Fishie2.png")
fish3 = pygame.image.load("Python/FinalGame_2270/images/Fishie3.png")
fish_choices = [fish1, fish2, fish3]
def chooseImage1():  
    return random.choice(fish_choices)


foodCan = pygame.image.load("Python/FinalGame_2270/images/foodCan.png")
can_choices = [foodCan]
def chooseImage2():
    return random.choice(can_choices)


BadItem1 = pygame.image.load("Python/FinalGame_2270/images/CatClips.png")
BadItem2 = pygame.image.load("Python/FinalGame_2270/images/spraybottle.png")
BadItem_choices = [BadItem1, BadItem2]
def chooseImage3():
    return random.choice(BadItem_choices)

# create classes for each set of items
# Set random locations and images, format images to rectangle, set up functions for use in game loop
class Fish:
    def __init__(self):
        self.x = random.randint(0, windowWidth - 50)
        self.y = random.randint(0, windowHeight - 50)
        fish_image = chooseImage1()
        self.fishStretchedImage = pygame.transform.scale(fish_image, (50,50))
        self.fish_rect = pygame.Rect(self.fishStretchedImage.get_rect())
        self.fish_rect.x = self.x
        self.fish_rect.y = self.y
    def getImage(self):
        return self.fishStretchedImage
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getRect(self):
        return self.fish_rect
    

# set up time function to make images appear and disapper in game loop
last_time1 = None
fishes = []
def addFishes():
    last_time1 = time.time()
    fish = Fish()
    fishes.append(fish)



class FoodCan:
    def __init__(self):
        self.x = random.randint(0, windowWidth - 40)
        self.y = random.randint(0, windowHeight - 40)
        can_image = chooseImage2()
        self.canStretchedImage = pygame.transform.scale(can_image, (40,40))
        self.can_rect = pygame.Rect(self.canStretchedImage.get_rect())
        self.can_rect.x = self.x
        self.can_rect.y = self.y
    def getImage(self):
        return self.canStretchedImage
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getRect1(self):
        return self.can_rect

last_time2 = None
foodCans = []
def addFoodCans():
    last_time2 = time.time()
    cans = FoodCan()
    foodCans.append(cans)


class Bad_Items:
    def __init__(self):
        self.x = random.randint(0, windowWidth - 50)
        self.y = random.randint(0, windowHeight - 50)
        baditem_image = chooseImage3()
        self.badStretchedImage = pygame.transform.scale(baditem_image, (50,50))
        self.bad_rect = pygame.Rect(self.badStretchedImage.get_rect())
        self.bad_rect.x = self.x
        self.bad_rect.y = self.y
    def getImage(self):
        return self.badStretchedImage
    def getX(self):
        return self.x
    def getY(self):
        return self.y  
    def getRect2(self):
        return self.bad_rect 

last_time3 = None
badItems = []
def addBadItems():
    last_time3 = time.time()
    bad_items = Bad_Items()
    badItems.append(bad_items)     


# Game Loop
running = True
delete_time1 = time.time()
delete_time2 = time.time()
delete_time3 = time.time()
while running:
    screen.fill((173, 216, 230))
    
    # Background Image
    #screen.blit(background, (0, 0))

    # set up how quickly items appear and disappear for each set of items
    now1 = time.time()
    if (last_time1 != None):
        now1 = time.time()
        if (now1 - last_time1 >= 2 and now1 - last_time1 < 5):
            addFishes()
            last_time1 = now1
        if (now1 - delete_time1 >= 5):
            fishes.pop(0)
            delete_time1 = now1

    now2 = time.time()
    if (last_time2 != None):
        now2 = time.time()
        if (now2 - last_time2 >= 5 and now2 - last_time2 < 10):
            addFoodCans()
            last_time2 = now2
        if (now2 - delete_time2 >= 5):
            foodCans.pop(0)
            delete_time2 = now2

    now3 = time.time()
    if (last_time3 != None):
        now3 = time.time()
        if (now3 - last_time3 >= 2 and now3 - last_time3 < 5):
            addBadItems()
            last_time3 = now3
        if (now3 - delete_time3 >= 5):
            badItems.pop(0)
            delete_time3 = now3
            

    # continue adding items as well
    else:
        addFishes() 
        last_time1 = now1
        addFoodCans()
        last_time2 = now2
        addBadItems()
        last_time3 = now3
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

                
    # move the player
    if moveDown and player_cat.bottom < windowHeight:
        player_cat.top += moveSpeed
    if moveUp and player_cat.top > 0:
        player_cat.top -= moveSpeed
    if moveLeft and player_cat.left > 0:
        player_cat.left -= moveSpeed
    if moveRight and player_cat.right < windowWidth:
        player_cat.right += moveSpeed


    for fish in fishes[:]:
    # print(f"Player rect at: {player_cat}")
    # print(f"Fish at {i}")
        if player_cat.colliderect(fish.getRect()):
            #print("Caught fish")
            fishes.remove(fish)
            score_value += 30

    for food in foodCans[:]:
        if player_cat.colliderect(food.getRect1()):
            foodCans.remove(food)
            score_value += 50    

    for bad in badItems[:]:
        if player_cat.colliderect(bad.getRect2()):
            badItems.remove(bad)
            score_value -= 30 

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
    for fish in fishes:
        screen.blit(fish.getImage(), (fish.getX(), fish.getY()))
    for cans in foodCans:
        screen.blit(cans.getImage(), (cans.getX(), cans.getY()))
    for bad_items in badItems:
        screen.blit(bad_items.getImage(), (bad_items.getX(), bad_items.getY()))

    mainClock.tick(FPS)
    show_score(textX, textY)
    pygame.display.update()
