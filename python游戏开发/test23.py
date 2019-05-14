import pygame
import math


class Brush(object):
    def __init__(self, screen):
        self.screen = screen
        self.color = (0, 0, 0)
        self.size = 1
        self.drawing = False
        self.last_pos = None

        self.space = 1
        self.style = False
        self.brush = pygame.image.load("brush.png").convert_alpha()

        self.brush_now = self.brush.subsurface((0, 0), (1, 1))

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        for i in range(self.brush.get_width()):
            for j in range(self.brush.get_height()):
                self.brush.set_at((i, j), color + (self.brush.get_at((i, j)).a,))

    def start_draw(self, pos):
        self.drawing = True
        self.last_pos = pos

    def end_draw(self):
        self.drawing = False

    def draw(self, pos):
        if self.drawing:
            for p in self._get_points(pos):
                if not self.style:
                    pygame.draw.circle(self.screen, self.color, p, self.size)
                else:
                    self.screen.blit(self.brush_now, p)
            self.last_pos = pos

    def set_brush_style(self, style):
        print("set brush style to ", style)
        self.style = style

    def get_brush_style(self):
        return self.style

    def get_size(self):
        return self.size

    def set_size(self, size):
        if size < 0.5:
            size = 1
        elif size > 50:
            size = 50
        print("set brush size to ", size)
        self.size = size
        self.brush_now = self.brush.subsurface((0, 0), (size * 2, size * 2))

    def _get_points(self, pos):
        points = [(self.last_pos[0], self.last_pos[1])]
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length
        for _ in range(int(length)):
            points.append((points[-1][0] + step_x, points[-1][1] + step_y))
        points = map(lambda x: (int(0.5 + x[0]), int(0.5 + x[1])), points)
        return list(set(points))

    def get_current_brush(self):
        return self.brush_now


class Menu(object):
    def __init__(self, screen):
        self.screen = screen
        self.brush = None
        self.colors = [
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
            (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff),
            (0x00, 0x00, 0x00), (0x80, 0x80, 0x80),
        ]
        self.colors_rect = []
        for (i, rgb) in enumerate(self.colors):
            rect = pygame.Rect(10 + i % 2 * 32, 254 + i // 2 * 32, 32, 32)
            self.colors_rect.append(rect)

        self.pens = [
            pygame.image.load("pen1.png").convert_alpha(),
            pygame.image.load("pen2.png").convert_alpha(),
        ]
        self.pens_rect = []
        for (i, img) in enumerate(self.pens):
            rect = pygame.Rect(10, 10 + i * 64, 64, 64)
            self.pens_rect.append(rect)

        self.sizes = [
            pygame.image.load("big.png").convert_alpha(),
            pygame.image.load("small.png").convert_alpha(),
        ]
        self.size_rect = []
        for (i, img) in enumerate(self.sizes):
            rect = pygame.Rect(10 + i * 32, 138, 32, 32)
            self.size_rect.append(rect)

    def set_brush(self, brush):
        self.brush = brush

    def draw(self):
        for (i, img) in enumerate(self.pens):
            self.screen.blit(img, self.pens_rect[i].topleft)
        for (i, img) in enumerate(self.sizes):
            self.screen.blit(img, self.size_rect[i].topleft)
        self.screen.fill((255, 255, 255), (10, 180, 64, 64))
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 180, 64, 64), 1)
        size = self.brush.get_size()
        x = 10 + 32
        y = 180 + 32
        if self.brush.get_brush_style():
            x -= size
            y -= size
            self.screen.blit(self.brush.get_current_brush(), (x, y))
        else:
            pygame.draw.circle(self.screen, self.brush.get_color(), (x, y), size)

        for (i, rgb) in enumerate(self.colors):
            pygame.draw.rect(self.screen, rgb, self.colors_rect[i])

    def click_button(self, pos):
        for (i, rect) in enumerate(self.pens_rect):
            if rect.collidepoint(pos):
                self.brush.set_brush_style(bool(i))
                return True
        for (i, rect) in enumerate(self.size_rect):
            if rect.collidepoint(pos):
                if i:
                    self.brush.set_size(self.brush.get_size() - 1)
                else:
                    self.brush.set_size(self.brush.get_size() + 1)
                return True
        for (i, rect) in enumerate(self.colors_rect):
            if rect.collidepoint(pos):
                self.brush.set_color(self.colors[i])
                return True
        return False


class Painter(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("painter")
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.screen)
        self.brush = Brush(self.screen)
        self.menu.set_brush(self.brush)

    def run(self):
        self.screen.fill((255, 255, 255))
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.screen.fill((255, 255, 255))

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos)[0] <= 74 and self.menu.click_button(event.pos):
                        pass
                    else:
                        self.brush.start_draw(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.brush.end_draw()
                elif event.type == pygame.MOUSEMOTION:
                    self.brush.draw(event.pos)
            self.menu.draw()
            pygame.display.update()


if __name__ == "__main__":
    app = Painter()
    app.run()
