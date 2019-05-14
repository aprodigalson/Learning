import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640,400),0,32)

color1 = (221,99,20)
color2 = (96, 130, 51)
factor = 0

def blend_color(color1,color2,bend_factor):
    r1, g1,b1 = color1
    r2,g2,b2 = color2
    r = r1+(r2-r1)*bend_factor
    g = g1+(g2-g1)*bend_factor
    b = b1+(b2-b1)*bend_factor
    return int(r),int(g),int(b)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((255,255,255))
    tri = [(0,120), (639,100), (639,140)]
    pygame.draw.polygon(screen,(0,255,0),tri)
    pygame.draw.circle(screen,(0,0,0),(int(factor*639),120),10)

    x,y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        factor = x/639
        pygame.display.set_caption("pygame color blend test-{}".format(factor))

    color = blend_color(color1,color2,factor)
    pygame.draw.rect(screen, color, (0,240,640,240))

    pygame.display.update()