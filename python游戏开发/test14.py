import pygame, sys

background_image_filename = "sushiplate.jpg"
sprite_image_filename = "fugu.png"

pygame.init()
screen = pygame.display.set_mode((600, 400))
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

x, y = 100, 100
clock = pygame.time.Clock()
speed_x, speed_y = 170, 130

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))
    time_passe = clock.tick()
    time_passed_seconds = time_passe / 1000
    x += time_passed_seconds * speed_x
    y += time_passed_seconds * speed_y
    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0
    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()
