# importing the libraries
import pygame, sys, random, math, time
from pygame.locals import *
from textwrap import fill

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


# main character
player_cat = pygame.Rect(0, 0, 60,60)
player1Img = pygame.image.load("Python/FinalGame_2270/images/amazed.png")
playerStretchedImage = pygame.transform.scale(player1Img, (60, 60))
player_cat.x = 10
player_cat.y = 700

# Creating the enemy
enemy = pygame.Rect(10, 200, 32, 32)
enemyImg = pygame.image.load('Python/FinalGame_2270/images/angry.png')
enemyStretchedImage = pygame.transform.scale(enemyImg, (60,60))
enemy.x = 400
enemy.y = 400

enemy2 = pygame.Rect(10, 200, 32, 32)
enemyImg2 = pygame.image.load('Python/FinalGame_2270/images/angry.png')
enemyStretchedImage2 = pygame.transform.scale(enemyImg2, (60,60))
enemy2.x = 100
enemy2.y = 100

enemy3 = pygame.Rect(10, 200, 32, 32)
enemyImg3 = pygame.image.load('Python/FinalGame_2270/images/angry.png')
enemyStretchedImage3 = pygame.transform.scale(enemyImg2, (60,60))
enemy3.x = 600
enemy3.y = 700

# Background
background = pygame.transform.scale(pygame.image.load('Python/FinalGame_2270/images/background.jpg').convert(), (windowHeight, windowHeight))

# Sound Setup
meow = pygame.mixer.Sound("Python/FinalGame_2270/sounds/catmeow_music.wav")
bark = pygame.mixer.Sound("Python/FinalGame_2270/sounds/dogbark_music.wav")
gameOver = pygame.mixer.Sound("Python/FinalGame_2270/sounds/gameover_music.wav")
gameOver_sound = True
levelUp = pygame.mixer.Sound("Python/FinalGame_2270/sounds/powerup_music.wav")
levelUp_sound = True
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
level = 1
delay = 0.1

def draw_level_info():
    font1 = pygame.font.SysFont('arial', 28)
    current_level = font1.render(f'Level: {level}', True, (0, 0, 0))
    screen.blit(current_level, (15, 2))
    
def show_score():
    font = pygame.font.SysFont("arial", 28)
    score = font.render(f'Score: {score_value}', True, (0, 0, 0))
    screen.blit(score, (375,2))

def draw_start_menu():
    screen.fill((173, 216, 230))

    font1 = pygame.font.SysFont('arial', 100)
    font2 = pygame.font.SysFont('arial', 50)
    font3 = pygame.font.SysFont('arial', 62)
    fontUnderline= font3
    fontUnderline.set_underline(True)
    font4 = pygame.font.SysFont('arial', 40)

    title = font1.render('Something Fishy', True, "orange")
    start_button = font2.render('Space - Start', True, "#006400")
    exit_button = font2.render('Q - Quit', True, "red")
    
    how_to_play = fontUnderline.render("How to Play", True, "white")
    movement_keys = font4.render("Use the arrow or WASD keys to:", True, "orange")
    objective = font4.render("Collect the fish & food cans", True, "#006400")
    avoid_dogs = font4.render("Don't get caught by the dogs!", True, "red")
    levels_info = font4.render("Complete all 3 levels to beat the game", True, "orange")

    fish_main_menu = pygame.image.load("Python/FinalGame_2270/images/fish.png")
    fish2_main_menu = pygame.image.load("Python/FinalGame_2270/images/fish2.png")
    fish2 = pygame.transform.flip(fish2_main_menu, True, False)
    new_fish2 = pygame.transform.scale(fish2, (100, 100))
    fish3_main_menu = pygame.image.load("Python/FinalGame_2270/images/fish3.png")
    new_fish3 = pygame.transform.scale(fish3_main_menu, (100, 100))

    
    screen.blit(title, (windowWidth/2 - title.get_width()/2, windowHeight/2 - title.get_height()/2 - 150))
    screen.blit(start_button, (windowWidth/2 - start_button.get_width()/2, windowHeight/2 - start_button.get_height()/2 - 60))
    screen.blit(exit_button, (windowWidth/2 - exit_button.get_width()/2, windowHeight/2 - exit_button.get_height()/2 - 10))

    screen.blit(how_to_play, (windowWidth/2 - how_to_play.get_width()/2, windowHeight/2 - how_to_play.get_height()/2 + 100))
    screen.blit(movement_keys, (windowWidth/2 - movement_keys.get_width()/2, windowHeight/2 - movement_keys.get_height()/2 + 170))
    screen.blit(objective, (windowWidth/2 - objective.get_width()/2, windowHeight/2 - objective.get_height()/2 + 220))
    screen.blit(avoid_dogs, (windowWidth/2 - avoid_dogs.get_width()/2, windowHeight/2 - avoid_dogs.get_height()/2 + 270))
    screen.blit(levels_info, (windowWidth/2 - levels_info.get_width()/2, windowHeight/2 - levels_info.get_height()/2 + 320))


    screen.blit(fish_main_menu, (windowWidth/2 - fish_main_menu.get_width()/2, windowHeight/2 - fish_main_menu.get_height()/2 - 250))
    screen.blit(new_fish3, (windowWidth/2 - new_fish3.get_width()/2 - 250, windowHeight/2 - new_fish3.get_height()/2 - 250))
    screen.blit(new_fish2, (windowWidth/2 - new_fish2.get_width()/2 + 250, windowHeight/2 - new_fish2.get_height()/2 - 250))

    pygame.display.update()

def draw_game_over_screen():
    screen.fill((0,0,0))
    font1 = pygame.font.SysFont('arial', 100)
    font2 = pygame.font.SysFont('arial', 50)
    font3 = pygame.font.SysFont('arial', 70)
    title = font1.render('Game Over', True, "white")
    restart_button = font2.render('R - Restart', True, "#006400")
    quit_button = font2.render('Q - Quit', True, "red")
    game_over_text = font3.render('You Became Dog Food!', True, 'red')
    dog = pygame.image.load("Python/FinalGame_2270/images/angry-dog-big.png")
    screen.blit(title, (windowWidth/2 - title.get_width()/2, windowHeight/2 - title.get_height()/2))
    screen.blit(restart_button, (windowWidth/2 - restart_button.get_width()/2, windowHeight/2 - restart_button.get_height()/2 + 100))
    screen.blit(quit_button, (windowWidth/2 - quit_button.get_width()/2, windowHeight/2 - quit_button.get_height()/2 + 150))
    screen.blit(dog, (windowWidth/2 - dog.get_width()/2, windowHeight/2 - dog.get_height()/2 - 120))
    screen.blit(dog, (windowWidth/2 - dog.get_width()/2 - 250, windowHeight/2 - dog.get_height()/2 - 120))
    screen.blit(dog, (windowWidth/2 - dog.get_width()/2 + 250, windowHeight/2 - dog.get_height()/2 - 120))
    screen.blit(game_over_text, (windowWidth/2 - game_over_text.get_width()/2, windowHeight/2 - game_over_text.get_height()/2 - 260))
    pygame.display.update()

def draw_level_complete():
    screen.fill("orange")
    font1 = pygame.font.SysFont('arial', 100)
    font2 = pygame.font.SysFont('arial', 50)
    font3 = pygame.font.SysFont('arial', 62)
    title = font1.render('Level Complete', True, "white")
    continue_btn = font2.render('Space - Continue', True, "#006400")
    quit_btn = font2.render('Quit - Q', True, "red")
    level_complete_text = font3.render('Your Hunger Has Been Satisfied!', True, "#006400")
    cat2 = pygame.image.load("Python/FinalGame_2270/images/angry.png")
    screen.blit(title, (windowWidth/2 - title.get_width()/2, windowHeight/2 - title.get_height()/2))
    screen.blit(continue_btn, (windowWidth/2 - continue_btn.get_width()/2, windowHeight/2 - continue_btn.get_height()/2 + 100))
    screen.blit(quit_btn, (windowWidth/2 - quit_btn.get_width()/2, windowHeight/2 - quit_btn.get_height()/2 + 150))
    screen.blit(cat2, (windowWidth/2 - cat2.get_width()/2, windowHeight/2 - cat2.get_height()/2 - 120))
    screen.blit(cat2, (windowWidth/2 - cat2.get_width()/2 - 250, windowHeight/2 - cat2.get_height()/2 - 120))
    screen.blit(cat2, (windowWidth/2 - cat2.get_width()/2 + 250, windowHeight/2 - cat2.get_height()/2 - 120))
    screen.blit(level_complete_text, (windowWidth/2 - level_complete_text.get_width()/2, windowHeight/2 - level_complete_text.get_height()/2 - 260))
    pygame.display.update()

def draw_game_complete():
    screen.fill((173, 216, 230))
    font1 = pygame.font.SysFont('arial', 100)
    font2 = pygame.font.SysFont('arial', 50)
    font3 = pygame.font.SysFont('arial', 62)
    title = font1.render('Game Completed!', True, "white")
    restart_btn = font2.render('R - Restart', True, "#006400")
    quit_btn = font2.render('Quit - Q', True, "red")
    level_complete_text = font3.render('You Really Fooled Those Dogs!', True, "#006400")
    cat2 = pygame.image.load("Python/FinalGame_2270/images/falling-in-love.png")
    screen.blit(title, (windowWidth/2 - title.get_width()/2, windowHeight/2 - title.get_height()/2))
    screen.blit(restart_btn, (windowWidth/2 - restart_btn.get_width()/2, windowHeight/2 - restart_btn.get_height()/2 + 100))
    screen.blit(quit_btn, (windowWidth/2 - quit_btn.get_width()/2, windowHeight/2 - quit_btn.get_height()/2 + 150))
    screen.blit(cat2, (windowWidth/2 - cat2.get_width()/2, windowHeight/2 - cat2.get_height()/2 - 120))
    screen.blit(cat2, (windowWidth/2 - cat2.get_width()/2 - 250, windowHeight/2 - cat2.get_height()/2 - 120))
    screen.blit(cat2, (windowWidth/2 - cat2.get_width()/2 + 250, windowHeight/2 - cat2.get_height()/2 - 120))
    screen.blit(level_complete_text, (windowWidth/2 - level_complete_text.get_width()/2, windowHeight/2 - level_complete_text.get_height()/2 - 260))
    pygame.display.update()

# Load in images, create an array with the images, create a function the randomly chooses images from this array
fish1 = pygame.image.load("Python/FinalGame_2270/images/fish.png")
fish2 = pygame.image.load("Python/FinalGame_2270/images/fish2.png")
fish3 = pygame.image.load("Python/FinalGame_2270/images/fish3.png")
fish_choices = [fish1, fish2, fish3]
def chooseImage1():
    return random.choice(fish_choices)

foodCan = pygame.image.load("Python/FinalGame_2270/images/canned-food.png")
can_choices = [foodCan]
def chooseImage2():
    return random.choice(can_choices)


BadItem1 = pygame.image.load("Python/FinalGame_2270/images/nailclips.png")
BadItem2 = pygame.image.load("Python/FinalGame_2270/images/spray.png")
BadItem_choices = [BadItem1, BadItem2]
def chooseImage3():
    return random.choice(BadItem_choices)

# create classes for each set of items
# Set random locations and images, format images to rectangle, set up functions for use in game loop
class Fish:
    def __init__(self):
        self.x = random.randint(0, windowWidth - 50)
        self.y = random.randint(50, windowHeight - 50)
        self.width = 50
        self.height = 50
        fish_image = chooseImage1()
        self.fishStretchedImage = pygame.transform.scale(fish_image, (55,55))
        self.fish_rect = pygame.Rect(self.fishStretchedImage.get_rect())
        self.fish_rect.x = self.x
        self.fish_rect.y = self.y
        self.fish_rect.width = self.width
        self.fish_rect.height = self.height
    def getImage(self):
        return self.fishStretchedImage
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getRect(self):
        #print(self.fish_rect)
        return self.fish_rect

# set up time function to make images appear and disapper in game loop
last_time1 = None
fishes = []
def addFishes():
    print("Adding fish")
    last_time1 = time.time()
    fish = Fish()
    fishes.append(fish)

class FoodCan:
    def __init__(self):
        self.x = random.randint(0, windowWidth - 50)
        self.y = random.randint(50, windowHeight - 50)
        self.width = 50
        self.height = 50
        can_image = chooseImage2()
        self.canStretchedImage = pygame.transform.scale(can_image, (40,40))
        self.can_rect = pygame.Rect(can_image.get_rect())
        self.can_rect.x = self.x
        self.can_rect.y = self.y
    def getImage(self):
        can_image = chooseImage2()
        return can_image
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
        self.y = random.randint(50, windowHeight - 50)
        self.width = 50
        self.height = 50
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

def game_over():
    draw_game_over_screen()

def level_complete():
    draw_level_complete()
    
def game_completed():
    draw_game_complete()

def dog_chasing_cat():
    # dog chasing the cat
    distance_x = player_cat.x - enemy.x
    distance_y = player_cat.y - enemy.y
    distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
    enemySpeed = 2

    if distance < 350:
        enemy.x += enemySpeed * distance_x / distance
        enemy.y += enemySpeed * distance_y / distance

def dog2_chasing_cat():
    distance_x = player_cat.x - enemy2.x
    distance_y = player_cat.y - enemy2.y
    distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
    enemySpeed = 3

    if distance < 350:
        enemy2.x += enemySpeed * distance_x / distance
        enemy2.y += enemySpeed * distance_y / distance

def dog3_chasing_cat():
    distance_x = player_cat.x - enemy3.x
    distance_y = player_cat.y - enemy3.y
    distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

    enemySpeed = 2

    if distance < 350:
        enemy3.x += enemySpeed * distance_x / distance
        enemy3.y += enemySpeed * distance_y / distance
    

# Game Loop
running = True
playing = False
game_state = "start_menu"
game_over = False
level_complete = False
game_completed = False
playing = False
delete_time1 = time.time()
delete_time2 = time.time()
delete_time3 = time.time()

while running:
    screen.fill((173, 216, 230))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

    print(f"[debug] Num food items: {len(fishes) + len(foodCans)}")

    if game_state == "start_menu":
        gameOver_sound = True
        levelUp_sound = True

        fishes = []
        last_time1 = time.time()
        badItems = []
        last_time2 = time.time()
        foodCans = []
        last_time3 = time.time()

        pygame.mixer.music.pause()
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "game_level1"
            
            game_over = False
        if keys[pygame.K_q]:
            running = False
            pygame.quit()
            sys.exit()

    if game_state == "completed_level1":
        
        fishes = []
        last_time1 = time.time()
        badItems = []
        last_time2 = time.time()
        foodCans = []
        last_time3 = time.time()
        
        pygame.mixer.music.pause()
        if levelUp_sound:
            levelUp.play()
            levelUp_sound = False
        draw_level_complete()
        level = 2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "game_level2"
            game_over = False
            player_cat.x = 10
            player_cat.y = 700
            enemy.x = 400
            enemy.y = 400
            score_value = 0

            enemy2.x = 100
            enemy2.y = 100

    if game_state == "completed_level2":

        fishes = []
        last_time1 = time.time()
        badItems = []
        last_time2 = time.time()
        foodCans = []
        last_time3 = time.time()
        
        pygame.mixer.music.pause()
        if levelUp_sound:
            levelUp.play()
            levelUp_sound = False
        draw_level_complete()
        level = 3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "game_level3"
            game_over = False
            player_cat.x = 10
            player_cat.y = 700
            enemy.x = 400
            enemy.y = 400
            score_value = 0

            enemy2.x = 100
            enemy2.y = 100

            enemy3.x = 700
            enemy3.y = 600
    
            
        if keys[pygame.K_q]:
            running = False
            pygame.quit()
            sys.exit()

    if game_state == "game_complete":
        
        pygame.mixer.music.pause()
        if levelUp_sound:
            levelUp.play()
            levelUp_sound = False
        draw_game_complete()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
            game_over = False
            game_completed = False
            

        if keys[pygame.K_q]:
            running = False
            pygame.quit()
            sys.exit()
        
    if game_state == "game_over":
        pygame.mixer.music.pause()
        # gameOver_sound = True
        if gameOver_sound:
            gameOver.play()
            gameOver_sound = False
        draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
            game_over = False
            player_cat.x = 10
            player_cat.y = 700
            enemy.x = 400
            enemy.y = 400
            score_value = 0

        if keys[pygame.K_q]:
            running = False
            pygame.quit()
            sys.exit()

    if game_state == "game_level1":
        pygame.mixer.music.unpause()
        keys = pygame.key.get_pressed()
        # set up how quickly items appear and disappear for each set of items
        now1 = time.time()
        if (last_time1 != None):
            now1 = time.time()
            if (now1 - last_time1 >= 2 and now1 - last_time1 < 5):
                for numFish in range(2):
                    addFishes()
                last_time1 = now1
            if (now1 - delete_time1 >= 5):
                addFishes()
                fishes.pop()
                delete_time1 = now1

        now2 = time.time()
        if (last_time2 != None):
            now2 = time.time()
            if (now2 - last_time2 >= 5 and now2 - last_time2 < 10):
                addFoodCans()
                last_time2 = now2
            if (now2 - delete_time2 >= 5):
                addFoodCans()
                foodCans.pop()
                delete_time2 = now2

        now3 = time.time()
        if (last_time3 != None):
            now3 = time.time()
            if (now3 - last_time3 >= 2 and now3 - last_time3 < 5):
                addBadItems()
                last_time3 = now3
            if (now3 - delete_time3 >= 5):
                addBadItems()
                badItems.pop()
                delete_time3 = now3

        # continue adding items as well
        else:
            addFishes()
            last_time1 = now1
            addFoodCans()
            last_time2 = now2
            addBadItems()
            last_time3 = now3

        dog_chasing_cat()
    
        # draw the window on the screen
        banner_rect = pygame.draw.rect(screen, "orange", pygame.Rect(0, 0, 800, 40))
        screen.blit(playerStretchedImage, player_cat)
        screen.blit(enemyStretchedImage, enemy)

        if player_cat.colliderect(enemy):
            game_over = True
            game_state = "game_over"

        for fish in fishes:
            screen.blit(fish.getImage(), (fish.getX(), fish.getY()))
        for cans in foodCans:
            screen.blit(cans.getImage(), (cans.getX(), cans.getY()))
        for bad_items in badItems:
            screen.blit(bad_items.getImage(), (bad_items.getX(), bad_items.getY()))

        show_score()
        draw_level_info()

    if game_state == "game_level2":
        levelUp_sound = True
        pygame.mixer.music.unpause()
        keys = pygame.key.get_pressed()
        # set up how quickly items appear and disappear for each set of items
        now1 = time.time()
        if (last_time1 != None):
            now1 = time.time()
            if (now1 - last_time1 >= 2 and now1 - last_time1 < 5):
                for numFish in range(2):
                    addFishes()
                last_time1 = now1
            if (now1 - delete_time1 >= 5):
                addFishes()
                fishes.pop()
                delete_time1 = now1

        now2 = time.time()
        if (last_time2 != None):
            now2 = time.time()
            if (now2 - last_time2 >= 5 and now2 - last_time2 < 10):
                addFoodCans()
                last_time2 = now2
            if (now2 - delete_time2 >= 5):
                addFoodCans()
                foodCans.pop()
                delete_time2 = now2

        now3 = time.time()
        if (last_time3 != None):
            now3 = time.time()
            if (now3 - last_time3 >= 2 and now3 - last_time3 < 5):
                addBadItems()
                last_time3 = now3
            if (now3 - delete_time3 >= 5):
                addBadItems()
                badItems.pop()
                delete_time3 = now3

        # continue adding items as well
        else:
            addFishes()
            last_time1 = now1
            addFoodCans()
            last_time2 = now2
            addBadItems()
            last_time3 = now3

        dog_chasing_cat()
        dog2_chasing_cat()
    
        # draw the window on the screen
        banner_rect = pygame.draw.rect(screen, "orange", pygame.Rect(0, 0, 800, 40))
        screen.blit(playerStretchedImage, player_cat)
        screen.blit(enemyStretchedImage, enemy)
        screen.blit(enemyStretchedImage2, enemy2)

        if player_cat.colliderect(enemy) or player_cat.colliderect(enemy2):
            game_over = True
            game_state = "game_over"

        for fish in fishes:
            screen.blit(fish.getImage(), (fish.getX(), fish.getY()))
        for cans in foodCans:
            screen.blit(cans.getImage(), (cans.getX(), cans.getY()))
        for bad_items in badItems:
            screen.blit(bad_items.getImage(), (bad_items.getX(), bad_items.getY()))

        show_score()
        draw_level_info()

    if game_state == "game_level3":
        levelUp_sound = True
        pygame.mixer.music.unpause()
        keys = pygame.key.get_pressed()
        # set up how quickly items appear and disappear for each set of items
        now1 = time.time()
        if (last_time1 != None):
            now1 = time.time()
            if (now1 - last_time1 >= 2 and now1 - last_time1 < 5):
                for numFish in range(2):
                    addFishes()
                last_time1 = now1
            if (now1 - delete_time1 >= 5):
                addFishes()
                fishes.pop()
                delete_time1 = now1

        now2 = time.time()
        if (last_time2 != None):
            now2 = time.time()
            if (now2 - last_time2 >= 5 and now2 - last_time2 < 10):
                addFoodCans()
                last_time2 = now2
            if (now2 - delete_time2 >= 5):
                addFoodCans()
                foodCans.pop()
                delete_time2 = now2

        now3 = time.time()
        if (last_time3 != None):
            now3 = time.time()
            if (now3 - last_time3 >= 2 and now3 - last_time3 < 5):
                addBadItems()
                last_time3 = now3
            if (now3 - delete_time3 >= 5):
                addBadItems()
                badItems.pop()
                delete_time3 = now3

        # continue adding items as well
        else:
            addFishes()
            last_time1 = now1
            addFoodCans()
            last_time2 = now2
            addBadItems()
            last_time3 = now3

        dog_chasing_cat()
        dog2_chasing_cat()
        dog3_chasing_cat()
    
        # draw the window on the screen
        banner_rect = pygame.draw.rect(screen, "orange", pygame.Rect(0, 0, 800, 40))
        screen.blit(playerStretchedImage, player_cat)
        screen.blit(enemyStretchedImage, enemy)
        screen.blit(enemyStretchedImage2, enemy2)
        screen.blit(enemyStretchedImage3, enemy3)

        if player_cat.colliderect(enemy) or player_cat.colliderect(enemy2) or player_cat.colliderect(enemy3):
            game_over = True
            game_state = "game_over"
            pygame.mixer.Sound.play(gameOver)

        for fish in fishes:
            screen.blit(fish.getImage(), (fish.getX(), fish.getY()))
        for cans in foodCans:
            screen.blit(cans.getImage(), (cans.getX(), cans.getY()))
        for bad_items in badItems:
            screen.blit(bad_items.getImage(), (bad_items.getX(), bad_items.getY()))

        show_score()
        draw_level_info()

    # move the player
    if moveDown and player_cat.bottom < (windowHeight):
        player_cat.top += moveSpeed
    if moveUp and player_cat.top > 0:
        player_cat.top -= moveSpeed
    if moveLeft and player_cat.left > 0:
        player_cat.left -= moveSpeed
    if moveRight and player_cat.right < (windowWidth):
        player_cat.right += moveSpeed

    for fish in fishes[:]:
        if player_cat.colliderect(fish.getRect()):
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
            
    # completing levels
    if score_value >= 200 and game_state == "game_level1":
        level_complete = True
        game_state = "completed_level1"

    if score_value >= 200 and game_state == "game_level2":
        level_complete = True
        game_state = "completed_level2"

    if score_value >= 200 and game_state == "game_level3":
        level_complete = True
        game_state = "game_complete"
    
    mainClock.tick(FPS)
    pygame.display.update()