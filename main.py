# This is a sample Python script.
import pygame
from PIL import Image

pygame.init()
#imagen = Image.open('nave-espacial.png')
#imagen_redimensionada = imagen.resize((50,50))
#imagen_redimensionada.save("naveJugador.png")
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ba.jpg')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('naveJugador.png')
playerX = 100
playerY = 400


def player():
    screen.blit(playerImg, (playerX, playerY))


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
