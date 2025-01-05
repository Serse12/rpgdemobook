import pygame
from pygame import Vector2

from config import *
import numpy as np
import copy


class GenericObject(pygame.sprite.Sprite):
    rect: pygame.Rect = None
    collider_rect: pygame.Rect = None
    original_image: pygame.Surface = None

    def __init__(self, x, y):
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.darkness = 0
        self.brightness = 0
        super().__init__()


class Tree(GenericObject):
    def __init__(self, x, y, url):
        super().__init__(x, y)
        self.height = self.width * 2
        self.image = pygame.image.load(url).convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=(x, y + self.height / 2))
        self._layer = OBJ_LAYER
        self.collider_rect = pygame.Rect(self.rect.bottomleft[0], self.rect.bottomleft[1] - self.height / 2, self.width,
                                         self.height / 2)


class Tile(GenericObject):

    def __init__(self, x, y, url):
        super().__init__(x, y)
        self.image = pygame.image.load(url).convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # Get the rectangle of the image
        self._layer = TILE_LAYER
