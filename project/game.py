import physics as ph
import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
xsize = 800
ysize = 800
screen = pygame.display.set_mode((xsize, ysize))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
t = 0

alm = ph.ALM(np.array([400, 0]), np.array([0, 1]), 1, 1/30)

while not finished:
    clock.tick(FPS)
    alm.forces = [np.array([0, 2])]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        alm.main_stage_thrust()
    if keys[pygame.K_d]:
        alm.hover_right()
    if keys[pygame.K_a]:
        alm.hover_left()
    if keys[pygame.K_q]:
        alm.rotate_counterclockwise()
    if keys[pygame.K_e]:
        alm.rotate_clockwise()

    screen.fill((0, 0, 0))
    #circle(screen, (255, 255, 255), (int(alm.r[0]), int(alm.r[1])), 10)
    alm.update_coordinates()
    screen.blit(alm.image, alm.rect)
    print(alm.a, alm.v, alm.r, alm.angle)
    pygame.display.update()

pygame.quit()

