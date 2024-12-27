import pygame
from pygame import Vector2

from config import *


class GenericObject(pygame.sprite.Sprite):
    rect: pygame.Rect = None
    collider_rect: pygame.Rect = None

    def __init__(self, x, y):
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        super().__init__()
