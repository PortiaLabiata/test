import pygame
from pygame.draw import *
import pygame.font
from itertools import count as iter_count

def draw_multi_lines(screen, text, x, y):
    font = pygame.font.SysFont(None, 23)
    for number, line in enumerate(text):
        surface = font.render(line, False, (255, 255, 255))
        rect = surface.get_rect()
        rect.center = (x, y+15*number)
        screen.blit(surface, rect)


def generate_control_panel(screen, alm, terrain, tperc):
    inter_list = list(zip(*terrain))[1]
    sea_level = sum(inter_list)/len(inter_list)
    font = pygame.font.SysFont(None, 23)
    panel_string = []
    panel_string.append("V vert.: "+str(round(alm.v[1], 2)))
    panel_string.append("V hor.: "+str(round(alm.v[0], 2)))
    panel_string.append("Main fuel: "+str(round(alm.main_fuel, 2)))
    panel_string.append("RCS fuel: "+str(round(alm.rcs_fuel, 2)))
    panel_string.append("Alt: "+str(round(sea_level-alm.r[1], 2)))
    panel_string.append("Angle: "+str(round(alm.angle, 2)))
    panel_string.append("Ang vel.: "+str(round(alm.current_ang_vel, 3)))
    panel_string.append("Thrust: "+str(tperc))
    draw_multi_lines(screen, panel_string, 70, 15)

def draw_big_text(screen, text):
    font = pygame.font.SysFont(None, 40)
    surface = font.render(text, False, (255, 255, 255))
    rect = surface.get_rect()
    rect.center = (683, 384)
    screen.blit(surface, rect)
