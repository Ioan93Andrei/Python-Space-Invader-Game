import pygame
import random

# initialize pygame
pygame.init()

# creates the window
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# game loop
running = True
while running:

    #RGB color         
    screen.fill((36, 36, 36))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # if key is pressed check if it's right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.1
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        

    # update the screen
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 767:
        playerX = 767

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update() 