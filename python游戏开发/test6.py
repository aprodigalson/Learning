import pygame,sys
import pygame.freetype



pygame.init()
screen = pygame.display.set_mode((600,400))
GOLD = 255,250,0
RED = pygame.Color("red")

rect1 = pygame.draw.rect(screen,GOLD,(100,100,200,100),0)
rect2 = pygame.draw.rect(screen,RED,(200,300,400,100),0)
fontpath = "C://Windows//Fonts//simsun.ttc"
font = pygame.freetype.Font(fontpath,36)
frect = font.render_to(screen,(100,100),"爱我中国",fgcolor=RED)
fsur, frect = font.render("sdfs",fgcolor=RED)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(fsur,(0,0))
    pygame.display.update()