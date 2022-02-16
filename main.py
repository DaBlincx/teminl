import pygame
import sys
import time
import random






pygame.init()
pygame.display.set_caption('Terminal')
screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
clock = pygame.time.Clock()
game_font = pygame.font.Font("RobotoSerif.ttf",20)


mainLoop = True

while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    pygame.display.update()

pygame.quit()