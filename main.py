import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))
image = pygame.image.load('image/mario.png')

game_runing = True

while game_runing:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(image, (0,0))
    pygame.display.update()
    