import pygame
from GenericMap.GenericMap import *
from config import *


class LoadingScreen(GenericMap):

    def __init__(self, screen):
        super().__init__(x=0, y=0, screen=screen, player=None, darkness=0)

        self.font = pygame.font.Font(None, 35)
        self.font_color = (255, 255, 255)
        self.bg_color = (255, 0, 0)

        self.set_wallpaper("./FirstMap/img/wallpaper1.png")
        self.wallpaper = pygame.transform.scale(self.wallpaper, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.wallpaper_rect = self.wallpaper.get_rect(topleft=(0, 0))
        self.text_surface = self.font.render("LOADING...", True, self.font_color)
        self.text_rect = self.text_surface.get_rect(center=self.wallpaper_rect.center)

    def draw_wallpaper(self):
        self.screen.blit(self.wallpaper, self.wallpaper_rect)
        self.screen.blit(self.text_surface, self.text_rect)
