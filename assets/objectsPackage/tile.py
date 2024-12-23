from .objects import GenericObject
import pygame
from config import *


class Tile(GenericObject):

    def __init__(self, x, y, url):
        super().__init__(x, y, url)

    def draw_obj_image(self, screen):
        self.obj_image = pygame.transform.scale(self.obj_image, (TILE_SIZE, TILE_SIZE))
        screen.blit(self.obj_image, (self.x, self.y))
        self.layer = 1
