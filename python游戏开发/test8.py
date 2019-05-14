import pygame

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()

event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))

    event_text = event_text[-screen_size[1] // font_height:]
    if event.type == pygame.QUIT:
        exit()
    screen.fill((255, 255, 255))
    y = screen_size[1] - font_height
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
        y -= font_height
    pygame.display.update()
