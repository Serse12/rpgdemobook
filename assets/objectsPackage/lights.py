from .objects import GenericObject
import pygame
import copy
from config import *

images_prefix = "./assets/tiles/"


class LightSource(GenericObject):

    def __init__(self, x, y, light_radius, light_power):
        super().__init__(x, y)
        self.light_radius = light_radius
        self.light_power = light_power
        self.light_color = pygame.Color('yellow')


class Torch(LightSource):

    def __init__(self, x, y):
        super().__init__(x, y, light_radius=TILE_SIZE*2, light_power=100)
        self.image = pygame.image.load(images_prefix + "torch.png").convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Optional: Resize to 50x50
        self.rect = self.image.get_rect(topleft=(x, y))  # Get the rectangle of the image
        self.original_image = copy.deepcopy(self.image)
        self._layer = OBJ_LAYER
        self.collider_rect = self.rect
