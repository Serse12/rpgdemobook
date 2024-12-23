import pygame
from config import *


class GenericMap:

    def __init__(self, width, height, x, y, screen):
        self.wallpaper = None
        self.spawn_point = None
        self.tiles = None
        self.width = width
        self.height = height
        self.screen = screen

        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.set_spawn_point(x, y)

    def set_screen(self, screen):
        self.screen = screen

    def set_spawn_point(self, x, y):
        self.spawn_point = (x, y)

    def set_wallpaper(self, url):
        self.wallpaper = pygame.image.load(url)

    def set_tiles(self, url):
        self.tiles = pygame.image.load(url)

    def draw_wallpaper(self):
        self.wallpaper = pygame.transform.scale(self.wallpaper, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.blit(self.wallpaper, (0, 0))

    def draw_playable_map(self):
        return

    def draw_players_and_npc(self):
        return

    def draw(self):
        self.draw_wallpaper()
        self.draw_playable_map()
        self.draw_players_and_npc()


