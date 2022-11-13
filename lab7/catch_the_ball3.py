import pygame
from pygame.draw import *
import pygame.font
from random import randint
from math import sqrt, sin, cos

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball(object):
    x = 0
    y = 0
    r = 42
    color = BLACK
    def __init__(self, x_init, y_init, r, color, speed, angle):
        self.x = x_init
        self.y = y_init
        self.r = r
        self.color = color
        self.speed = speed
        self.angle = angle

    def move(self, velocity, angle):
        self.x = int(velocity*sin(angle))
        self.y = int(velocity*cos(angle))

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

pygame.init()
pygame.font.init()

FPS = 30
xsize = 600
ysize = 600
screen = pygame.display.set_mode((xsize, ysize))
points_font = pygame.font.SysFont(None, 24)
start_font = pygame.font.SysFont(None, 50)
points = 0

pygame.display.update()
clock = pygame.time.Clock()
finished = False
ball = Ball(randint(20, xsize), randint(20, ysize), randint(10, 50), COLORS[randint(0, 5)], randint(5, 15), randint(0, 180))
start_surface = start_font.render("Click to start", False, WHITE)
points_surface = points_font.render("Score: "+str(points), False, WHITE)
start_rect = start_surface.get_rect()
start_rect.center = (xsize // 2, ysize // 2)
screen.blit(start_surface, start_rect)
pygame.display.update()
started = False

while not started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            started = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                started = True

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("LMB pressed")
                print(ball.x, ball.y, ball.r)
                if sqrt((event.pos[0]-ball.x)**2+(event.pos[1]-ball.y)**2)<=ball.r:
                    print("Gotcha!")
                    points += 1
                    ball = Ball(randint(20, xsize), randint(20, ysize), randint(10, 50), COLORS[randint(0, 5)], randint(5, 15), randint(0, 180))
                else:
                    print("Missed this one(")
                    points -= 1
                    ball = Ball(randint(20, xsize), randint(20, ysize), randint(10, 50), COLORS[randint(0, 5)], randint(5, 15), randint(0, 180))

    ball.move(ball.speed, ball.angle)
    screen.fill(BLACK)
    ball.draw()
    pygame.display.update()


pygame.quit()
