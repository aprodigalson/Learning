import pygame
from random import randint
import sys


class Star(object):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed


def run():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    stars = []
    for _ in range(200):
        x = float(randint(0, 639))
        y = float(randint(0, 479))
        speed = float(randint(10, 300))
        stars.append(Star(x, y, speed))

    clock = pygame.time.Clock()
    white = (255, 255, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                sys.exit()
        y = float(randint(0, 479))
        speed = float(randint(10, 300))
        star = Star(640, y, speed)
        stars.append(star)

        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000
        screen.fill((0, 0, 0))
        for star in stars:
            new_x = star.x - time_passed_seconds * star.speed
            pygame.draw.aaline(screen, white, (new_x, star.y), (star.x + 1, star.y))
            star.x = new_x

        def on_screen(star):
            return star.x > 0

        stars = list(filter(on_screen, stars))
        pygame.display.update()


run()
