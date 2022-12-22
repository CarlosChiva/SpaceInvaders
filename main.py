# This is a sample Python script.
import pygame

# from PIL import Image
# imagen = Image.open('nave-espacial.png')
# imagen_redimensionada = imagen.resize((50,50))
# imagen_redimensionada.save("naveJugador.png")

pygame.init()
screen_X_size = 800
screen_Y_size = 600
screen = pygame.display.set_mode((screen_X_size, screen_Y_size))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('sape.jpg')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('naveJugador.png')
enemyImg = pygame.image.load('naveEnemiga.png')
# firstPositions
playerX = 370
playerY = 550
enemyX = 370
enemyY = 30
# Change position
player_changeX = 0
player_changeY = 0
enemy_changeY = 0
enemy_cangeX = 0


def player(numX, numY):
    screen.blit(playerImg, (numX, numY))


def enemy(numX, numY):
    screen.blit(enemyImg, (numX,numY))


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_changeX = -0.1
            if event.key == pygame.K_RIGHT:
                player_changeX = 0.1
        if event.type == pygame.KEYUP:
            player_changeX = 0
    if playerX <= 0:
        playerX = 0
    elif playerX >= 745:
        playerX = 745

    playerX += player_changeX

    player(playerX + 0.5, playerY + 0.5)
    enemy(enemyX,enemyY)
    pygame.display.update()
