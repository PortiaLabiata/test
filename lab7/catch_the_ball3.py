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
    rect = pygame.Rect(x-r, y-r, x+r, y+r)
    def __init__(self, x_init, y_init, r, color, speed, angle):
        self.x = x_init
        self.y = y_init
        self.r = r
        self.color = color
        self.speed = speed
        self.angle = angle
        self.rect = pygame.Rect(x_init-r, y_init-r, x_init+r, y_init+r)

    def move(self, velocity, angle):
        self.x += int(velocity*sin(angle))
        self.y += int(velocity*cos(angle))

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
border_top = pygame.Rect(0, 0, xsize, 1)
border_left = pygame.Rect(0, 0, 1, ysize)
border_bottom = pygame.Rect(0, ysize, xsize, ysize-1)
border_right = pygame.Rect(xsize, 0, xsize-1, ysize-1)

while not started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            started = True
            finished = True
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
                    points_surface = points_font.render("Score: "+str(points), False, WHITE)
                else:
                    print("Missed this one(")
                    points -= 1
                    ball = Ball(randint(20, xsize), randint(20, ysize), randint(10, 50), COLORS[randint(0, 5)], randint(5, 15), randint(0, 180))
                    points_surface = points_font.render("Score: "+str(points), False, WHITE)


    if ball.rect.colliderect(border_top) or ball.rect.colliderect(border_bottom) or ball.rect.colliderect(border_left) or ball.rect.colliderect(border_right):
        ball.angle = 180 - ball.angle
    ball.move(ball.speed, ball.angle)
    screen.fill(BLACK)
    screen.blit(points_surface, (10, 10))
    ball.draw()
    pygame.display.update()


pygame.quit()
