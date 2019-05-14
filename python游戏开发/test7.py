import pygame
import sys
import pygame.freetype

# pygame 是一种游戏开发引擎

'''
基本框架：

1引入pygame 和sys 
2初始化init()及设置
3死循环：获取事件并响应事件
4       刷新


'''

file_ball = "PYG02-ball.gif"
file_flower = "PYG03-flower.png"

pygame.init()
width = 600
height = 400
speed = [1, 1]
BLACK = 0, 0, 0
GOLD = 255, 250, 0
pos = [100, 100]
fontpath = "C://Windows//Fonts//simsun.ttc"

vInfo = pygame.display.Info()
width = vInfo.current_w // 2
height = vInfo.current_h // 2
size = (width, height)
# flags = pygame.NOFRAME RESIZE
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
flower = pygame.image.load(file_flower)
pygame.display.set_caption("python")
pygame.display.set_icon(flower)

font = pygame.freetype.Font(fontpath, 36)
frect = font.render_to(screen, pos, "狗", fgcolor=GOLD, size=50)

fps = 100
fclock = pygame.time.Clock()  # Clock对象

while True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif even.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif even.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif even.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[0] == 0 else (abs(speed[1] - 1)) * int(speed[1] / abs(speed[1]))
            elif even.key == pygame.K_ESCAPE:
                sys.exit()
        elif even.type == pygame.VIDEORESIZE:
            # also can be even.size[0]
            width = even.w
            height = even.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    # print(speed)
    if pos[0] < 0 or pos[0] + frect.width > width:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1] + frect.height > height:
        speed[1] = -speed[1]

    pos[0] += speed[0]
    pos[1] += speed[1]
    screen.fill(BLACK)
    frect = font.render_to(screen, pos, "狗", fgcolor=GOLD, size=50)

    pygame.display.update()
    fclock.tick(fps)
