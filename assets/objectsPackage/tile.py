from .objects import GenericObject
import pygame
from config import *


class Tile(GenericObject):

    def __init__(self, x, y, url):
        super().__init__(x, y)
        self.image = pygame.image.load(url).convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # Get the rectangle of the image
        # Optional: Resize to 50x50
        self._layer = TILE_LAYER
