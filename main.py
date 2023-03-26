# This is a sample Python script.
import math
import random

import pygame

#
# from PIL import Image
#
# imagen = Image.open('bullet2.png')
# imagen_redimensionada = imagen.resize((15, 20))
# imagen_redimensionada.save("bullet3.png")

pygame.init()
screen_X_size = 800
screen_Y_size = 600
screen = pygame.display.set_mode((screen_X_size, screen_Y_size))
pygame.display.set_caption("Space Invaders   ")
icon = pygame.image.load('sape.jpg')
pygame.display.set_icon(icon)
score = 0
playerImg = pygame.image.load('naveJugador.png')
enemyImg = pygame.image.load('naveEnemiga.png')
background = pygame.image.load('background2.jpeg')
bullet = pygame.image.load('bullet3.png')
# bullet
bullet_X = 370
bullet_Y = 550
bullet_changeY = 1.75
bullet_cangeX = 0
bullet_state = "ready"

# firstPositions
playerX = 370
playerY = 550
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
# Change position
player_changeX = 0
player_changeY = 0
enemy_changeY = 10
enemy_cangeX = 0.3



def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 7))


def player(numX, numY):
    screen.blit(playerImg, (numX, numY))


def enemy(numX, numY):
    screen.blit(enemyImg, (numX, numY))


def is_colision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
    return distance < 23


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_changeX = -0.5
            if event.key == pygame.K_RIGHT:
                player_changeX = 0.5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_X = playerX
                fire_bullet(bullet_X, bullet_Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_changeX = 0

    if bullet_state == "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_changeY
    if bullet_Y <= 0:
        bullet_Y = 550
        bullet_state = "ready"

    if playerX <= 0:
        playerX = 0
    elif playerX >= 745:
        playerX = 745
    playerX += player_changeX

    if enemyX <= 0:
        enemy_cangeX = 0.3
        enemyX = enemy_cangeX
        enemyY += enemy_changeY
    elif enemyX >= 750:
        enemy_cangeX = -0.3
        enemyX += enemy_cangeX
        enemyY += enemy_changeY
    enemyX += enemy_cangeX

    colision = is_colision(enemyX, enemyY, bullet_X, bullet_Y)
    if colision:
        bullet_Y = 550
        bullet_state = "ready"
        score += 10
        print(score)
        enemyX = random.randint(0, 800)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
