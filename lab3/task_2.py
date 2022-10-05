import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

def draw_cluster_of_circles(scr, R, nx, ny, x, y, r, g, b, shift):
    for i in range(0, ny):
        for j in range(0, nx):
            circle(scr, (r, g, b), (x+shift*j, y+shift*i), R)

rect(screen, (0, 0, 255), (0, 0, 400, 200))
rect(screen, (0, 255, 0), (0, 200, 400, 400))
draw_cluster_of_circles(screen, 20, 6, 2, 250, 50, 255, 255, 255, 15)
rect(screen, (147, 107, 14), (70, 180, 120, 100))
polygon(screen, (255, 0, 0), ((70, 180), (130, 130), (190, 180)))
rect(screen, (14, 147, 145), (90, 205, 80, 50))
line(screen, (0, 0, 0), [320, 300], [320, 170], 15)
draw_cluster_of_circles(screen, 30, 2, 4, 315, 150, 15, 83, 14, 10)
circle(screen, (249, 194, 194), (100, 50), 40)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
