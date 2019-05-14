import pygame, sys
from MyVector import Vector

background_image_filename = "sushiplate.jpg"
sprite_image_filename = "fugu.png"

pygame.init()
screen = pygame.display.set_mode((600, 400))
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()

position = Vector(100, 100)
heading = Vector()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    screen.blit(sprite, position.get_tuple())
    time_passe = clock.tick()
    time_passed_seconds = time_passe / 1000
    destination = Vector(*pygame.mouse.get_pos()) - Vector(*sprite.get_size()) / 2

    vector_to_mouse = Vector.from_points(position, destination)

    vector_to_mouse.normalize()

    heading = heading + (vector_to_mouse * 0.6)
    position += heading * time_passed_seconds

    pygame.display.update()
