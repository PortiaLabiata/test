import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 0, 0), (150, 135), 25)
circle(screen, (255, 0, 0), (250, 135), 20)
circle(screen, (0, 0, 0), (150, 135), 10)
circle(screen, (0, 0, 0), (250, 135), 10)
line(screen, (0, 0, 0), [160, 110], [110, 90], 9)
line(screen, (0, 0, 0), [240, 110], [310, 90], 9)
line(screen, (0, 0, 0), [165, 210], [235, 210], 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
