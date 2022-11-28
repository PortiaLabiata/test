import physics as ph
import interface as it
import pygame
import numpy as np
import terrain_generator as tg
from math import sqrt
from pygame.draw import *

pygame.init()

FPS = 30
xsize = 1366
ysize = 768
screen = pygame.display.set_mode((xsize, ysize))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

alm = ph.ALM(np.array([400, 0]), np.array([0, 1]), 1, 1/30)
terrain = tg.raise_mountains(screen, 0.2)
stage_thrust = 0

while not finished:
    clock.tick(FPS)
    alm.forces = [np.array([0, 1.07])]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    keys = pygame.key.get_pressed()
    if alm.main_fuel >= 0:
        if keys[pygame.K_w]:
            if stage_thrust < 100:
                stage_thrust += 1
            else:
                stage_thrust = 100
        if keys[pygame.K_s]:
            if stage_thrust > 0:
                stage_thrust -= 1
            else:
                stage_thrust = 0
    if alm.rcs_fuel >= 0:
        if keys[pygame.K_d]:
            alm.hover_right()
        if keys[pygame.K_a]:
            alm.hover_left()
        if keys[pygame.K_q]:
            alm.rotate_counterclockwise()
        if keys[pygame.K_e]:
            alm.rotate_clockwise()

    screen.fill((0, 0, 0))
    alm.main_stage_thrust(stage_thrust)
    alm.update_coordinates()

    x, y = alm.rect.center[0], alm.rect.center[1]
    for pixel in terrain:
        screen.set_at(pixel, (255, 255, 255))
        lat, h = pixel[0], pixel[1]
        if sqrt((lat-x)**2+(h-y)**2)<=35:
            if sqrt(alm.v[0]**2+alm.v[1]**2)>=10:
                print("Mission failed! ALM crashed")
                finished = True
            else:
                print("Mission complete! ALM successfully landed")
                finished = True

    #panel_surf, panel_rect = it.generate_control_panel(alm)
    #screen.blit(panel_surf, panel_rect)
    #it.generate_control_panel(alm)
    screen.blit(alm.image, alm.rect)
    print(alm.a, alm.v, alm.r, alm.angle, x, y)
    pygame.display.update()

pygame.quit()

