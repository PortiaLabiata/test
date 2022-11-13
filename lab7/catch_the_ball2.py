import pygame
from pygame.draw import *
import pygame.font
from random import randint
from math import sqrt, sin, cos
pygame.init()
pygame.font.init()

FPS = 30
xsize = 400
ysize = 400
screen = pygame.display.set_mode((xsize, ysize))
pts = pygame.font.SysFont(None, 24)
st = pygame.font.SysFont(None, 50)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x, y, r, starting_direction, speed, direction, color = 0, 0, 0, 0, 0, 0, 0
def throw_ball():
    """ Метает шарик """
    global x, y, r, starting_direction, speed, color
    x = randint(0, xsize)
    y = randint(0, ysize)
    r = randint(10, 40)
    starting_direction = randint(0, 359)
    speed = 3
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def move_ball():
    global x, y, r, direction, speed, color
    """
    if x<=r or y<=r or xsize-x<=r or ysize-x<=r:
        direction = 180 - direction
    """
    x += int(speed*sin(direction))
    y += int(speed*cos(direction))
    circle(screen, color, (x, y), r)


throw_ball()
direction = starting_direction
clock = pygame.time.Clock()
finished = False
points = 0
started = False
start_surface = st.render("Click to start", False, (255, 255, 255))
pts_surface = pts.render('Score: '+str(points), False, (255, 255, 255))
st_text_rect = start_surface.get_rect()
st_text_rect.center = (xsize // 2, ysize // 2)
screen.blit(start_surface, st_text_rect)
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("LMB")
                print(x, y, r)
                if sqrt((event.pos[0]-x)**2+(event.pos[1]-y)**2)<=r:
                    print("Gotcha!")
                    points += 50//r
                    pts_surface = pts.render('Score: '+str(points), False, (255, 255, 255))
                    throw_ball()
                else:
                    points -= 50//r
                    print("Missed this one!")
                    pts_surface = pts.render('Score: '+str(points), False, (255, 255, 255))
                    throw_ball()
                started = True

    if started:
        screen.fill(BLACK)
        screen.blit(pts_surface, (10, 10))
        move_ball()
    pygame.display.update()
pygame.quit()
