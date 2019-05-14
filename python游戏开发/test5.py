import pygame
import sys

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

vInfo = pygame.display.Info()
width = vInfo.current_w // 2
height = vInfo.current_h // 2
size = (width, height)
# flags = pygame.NOFRAME RESIZE
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.event.EventType
flower = pygame.image.load(file_flower)
pygame.display.set_caption("python")
pygame.display.set_icon(flower)
print(pygame.display.Info())

ball = pygame.image.load(file_ball)  # Surface 对象

ballrect = ball.get_rect()  # Rect 对象 ，有width,height,top,bottom,left,right

fps = 300
fclock = pygame.time.Clock()  # Clock对象

bgColor = pygame.Color("black")


def RGBChannel(a):
    return 0 if a < 0 else (255 if a > 255 else int(a))


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
    if pygame.display.get_active():
        ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    bgColor.r = RGBChannel(ballrect.left * 255 / width)
    bgColor.g = RGBChannel(ballrect.top * 255 / height)
    bgColor.b = RGBChannel(min(speed[0], speed[1]) * 255 / max(speed[0], speed[1], 1))

    screen.fill(bgColor)
    screen.blit(ball, ballrect)

    pygame.display.update()
    fclock.tick(fps)
