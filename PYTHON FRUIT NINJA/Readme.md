# FRUIT NINJA

Fruit ninja game, also known as fruit-slicing game which is easy to play. Fruit ninja game is popular among children.

The objective of this project is to build a fruit ninja game with python. This game is built with the help of pygame module and basic concept of python.

In this game, the user has to cut the fruits by touching the mouse on fruits. There are also bombs with fruits. If the mouse touches more than three bombs then the game will be over.

# PREREQUISITES
In this python project, we require pygame, random, sys, and os module of python. Please install pygame and random:
pip install pygame
Pip install random

# Importing required modules
import pygame, sys
import os
import random
# Creating display window
player_lives = 3
score = 0
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']
WIDTH = 800
HEIGHT = 500
FPS = 12
pygame.init()
pygame.display.set_caption(‘FRUIT NINJA--DataFlair’)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
gameDisplay.fill((BLACK))
background = pygame.image.load('back.jpg')
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 32)
score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
lives_icon = pygame.image.load('images/white_lives.png')
# ABOUT :
player_lives will keep track of remaining lives
score will keeps track of score
fruits are the entities in the game
pygame.init() initialize pygame
pygame.display.set_caption will set the caption of game window
FPS controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th second
WIDTH and HEIGHT are setting game display size by using pygame.display.set_mode
game background set by pygame.image.load which is used to set image
Lives-icon stores images that show remaining lives

# Generalized structure of the fruit Dictionary
def generate_random_fruits(fruit):
    fruit_path = "images/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x' : random.randint(100,500),               
        'y' : 800,
        'speed_x': random.randint(-10,10),    
        'speed_y': random.randint(-80, -60),    
        'throw': False,                       
        't': 0,                               
        'hit': False,
    }
    if random.random() >= 0.75:     
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False
data = {}
for fruit in fruits:
    generate_random_fruits(fruit)
# ABOUT :
This function generates random fruits and generalized structure
‘x’ and ‘y’ store the value where the fruit should be positioned on x-coordinate and y – coordinate
Speed_x and speed_y are key that store the value of how fast the fruit should move in the x and y-direction. It also controls the diagonal movement of fruits
throws key used to determine that the generated coordinate of the fruits is outside the gameplay or not. If outside, then it will be discarded.
Return the next random floating-point number in the range (0.0, 1.0)  to keep the fruits inside the gameDisplay
Data Dictionary used to hold the data of the random fruit generation


#  Method to draw fonts
font_name = pygame.font.match_font('comic.ttf')
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)
    
# ABOUT :
Draw_text function helps to draw text on the screen.
get_rect() return the Rect object.
X and y is the dimension of x-direction and y-direction
blit() draws image or writes text on the screen at a specified position


#  Draw players lives
def draw_lives(display, x, y, lives, image) :
    for i in range(lives) :
        img = pygame.image.load(image)
        img_rect = img.get_rect()      
        img_rect.x = int(x + 35 * i)   
        img_rect.y = y                 
        display.blit(img, img_rect)
def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("images/red_lives.png"), (x, y))
# ABOUT :
img_rect gets the (x,y) coordinates of the cross icons (lives on the top rightmost side)
img_rect .x sets the next cross icon 35 pixels from the previous one
img_rect.y takes care of how many pixels the cross icon should be positioned from the top of the screen
# Show game over display & front display
def show_gameover_screen():
    gameDisplay.blit(background, (0,0))
    draw_text(gameDisplay, "FRUIT NINJA!", 64, WIDTH / 2, HEIGHT / 4)
    if not game_over :
        draw_text(gameDisplay,"Score : " + str(score), 40, WIDTH / 2, 250)
    draw_text(gameDisplay, "Press a key to begin!", 24, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
show_gameover_screen() function shows the initial game screen and game over screen
pygame.display.flip() will update only a part of screen but if no args will pass then it will update the entire screen
pygame.event.get() will return all the event stored in the pygame event queue
If event type is equal to quit then the pygame will quit
event.KEYUP event that occurs when the key is pressed and released


# Game Loop
first_round = True
game_over = True        
game_running = True    
while game_running :
    if game_over :
        if first_round :
            show_gameover_screen()
            first_round = False
        game_over = False
        player_lives = 3
        draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')
        score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(score_text, (0, 0))
    draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')
    for key, value in data.items():
        if value['throw']:
            value['x'] += value['speed_x']
            value['y'] += value['speed_y']
            value['speed_y'] += (1 * value['t'])
            value['t'] += 1
            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'], value['y']))
            else:
                generate_random_fruits(key)
            current_position = pygame.mouse.get_pos()
            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 \
                    and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                if key == 'bomb':
                    player_lives -= 1
                    if player_lives == 0:
                        hide_cross_lives(690, 15)
                    elif player_lives == 1 :
                        hide_cross_lives(725, 15)
                    elif player_lives == 2 :
                        hide_cross_lives(760, 15)
                    if player_lives < 0 :
                        show_gameover_screen()
                        game_over = True
                    half_fruit_path = "images/explosion.png"
                else:
                    half_fruit_path = "images/" + "half_" + key + ".png"
                value['img'] = pygame.image.load(half_fruit_path)
                value['speed_x'] += 10
                if key != 'bomb' :
                    score += 1
                score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
                value['hit'] = True
        else:
            generate_random_fruits(key)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

# ABOUT :
This is the mainloop of the game
game_over terminates the game while loop if more than 3-Bombs are cut
game_running used to manage the game loop
If the event type is quit then the game window will be closed
In this game loop we displaying the fruits inside the screen dynamically
If a fruit is not cut then nothing will happen to it. if fruit cut, then a half-cut-fruit image should appear in place of that fruit
if the user clicks bombs for three-time, a GAME OVER message should be displayed and the window should be reset
clock.tick() will keep the loop running at the right speed (manages the frame/second). The loop should update after every 1/12th of the sec
