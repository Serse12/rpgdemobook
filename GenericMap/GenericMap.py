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
        self.all_sprites = pygame.sprite.Group()
        self.mapobjects = pygame.sprite.Group()
        self.maptiles = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.layerupdates = pygame.sprite.LayeredUpdates()

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

    def load_playable_map(self):
        return

    def load_players_and_npc(self):
        return

    def load_all(self):
        self.load_playable_map()
        self.load_players_and_npc()

    def draw(self):
        self.draw_wallpaper()
        self.layerupdates.draw(self.screen)
        #self.maptiles.draw(self.screen)


