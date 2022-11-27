import pygame
from pygame.draw import *
from random import random, randint

def raise_mountains(screen, sw_pr):
    h0 = randint(0, 100)
    direction = randint(1, 3)
    h = h0
    heights = []
    for latitude in range(1, 1367):
        if h <= 40:
            direction = 3
        if direction == 1:
            h -= 1
        elif direction == 2:
            pass
        elif direction == 3:
            h += 1

        #screen.set_at((latitude, 768-h), (255, 255, 255))
        heights.append((latitude, 768-h))
        if random() > (1 - sw_pr):
            direction = randint(1, 3)
    return heights
"""
pygame.init()

FPS = 30
xsize = 1366
ysize = 768
screen = pygame.display.set_mode((xsize, ysize))

terrain = raise_mountains(screen, 0.3)
for pixel in terrain:
    screen.set_at(pixel, (255, 255, 255))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pygame.display.update()

pygame.quit()
"""
