import pygame


class GenericMap:

    def __init__(self, width, height, x, y, screen, url):
        self.wallpaper = None
        self.spawn_point = None
        self.width = width
        self.height = height
        self.screen = screen

        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.set_spawn_point(x, y)
        self.set_wallpaper(screen, url)

    def set_spawn_point(self, x, y):
        self.spawn_point = (x, y)

    def set_wallpaper(self, screen, url):
        if screen is not None and url is not None:
            self.wallpaper = pygame.image.load(url)

    def draw_wallpaper(self):
        self.screen.blit(self.wallpaper, (0, 0))

    def draw(self):
        self.draw_wallpaper()
