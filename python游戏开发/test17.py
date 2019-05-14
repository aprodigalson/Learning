import pygame, sys
from MyVector import Vector
import math

background_image_filename = "sushiplate.jpg"
sprite_image_filename = "fugu.png"
pygame.init()
screen = pygame.display.set_mode((600, 400), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()

sprite_pos = Vector(200, 150)
sprite_speed = 300
sprite_rotation = 0
sprite_rotation_speed = 360

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0
    movement_direction = 0

    if pressed_keys[pygame.K_LEFT]:
        rotation_direction = 1
    elif pressed_keys[pygame.K_RIGHT]:
        rotation_direction = -1
    if pressed_keys[pygame.K_UP]:
        movement_direction = 1
    elif pressed_keys[pygame.K_DOWN]:
        movement_direction = -1

    screen.blit(background, (0, 0))

    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vector(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    screen.blit(rotated_sprite, sprite_draw_pos.get_tuple())

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
    heading_x = math.sin(sprite_rotation * math.pi / 180)
    heading_y = math.cos(sprite_rotation * math.pi / 180)

    heading = Vector(heading_x, heading_y)
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()
