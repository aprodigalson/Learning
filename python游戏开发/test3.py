import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 400), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
