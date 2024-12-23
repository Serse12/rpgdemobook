from .objects import GenericObject
import pygame
from config import *


class Tree(GenericObject):

    def __init__(self, x, y, url):
        super().__init__(x, y, url)

    def draw_obj_image(self, screen):
        self.obj_image = pygame.transform.scale(self.obj_image, (TILE_SIZE, TILE_SIZE * 2))
        screen.blit(self.obj_image, (self.x, self.y))
