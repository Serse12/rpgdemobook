import pygame
from config import *
from .playerconfig import *
from assets.objectsPackage.objects import GenericObject
import math
import copy


class Player(GenericObject):
    animation_frame = [list() for x in range(4)]

    images_prefix = "./assets/tiles/pipoyaEdits_blackByrd/protagonist/"

    animation_frame[LEFT] = [images_prefix + "sinistra1.png", images_prefix + "sinistra2.png",
                             images_prefix + "sinistra3.png"]
    animation_frame[RIGHT] = [images_prefix + "destra1.png", images_prefix + "destra2.png",
                              images_prefix + "destra3.png"]
    animation_frame[UP] = [images_prefix + "dietro1.png", images_prefix + "dietro2.png",
                           images_prefix + "dietro3.png"]
    animation_frame[DOWN] = [images_prefix + "avanti1.png", images_prefix + "avanti2.png",
                             images_prefix + "avanti3.png"]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(self.images_prefix + "avanti2.png").convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Optional: Resize to 50x50
        self.rect = self.image.get_rect(topleft=(x, y))  # Get the rectangle of the image
        self.original_image = copy.deepcopy(self.image)
        self._layer = PLAYER_LAYER
        self.speed = 2
        self.rotation = UP
        self.collider_rect = self.rect
        self.animation_frame_count = 0

    def update_sprite(self, keys):
        resto = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            resto = self.rect.x % TILE_SIZE
        elif keys[pygame.K_DOWN] or keys[pygame.K_UP]:
            resto = self.rect.y % TILE_SIZE

        if resto < TILE_SIZE / 2:
            self.animation_frame_count = 0
        else:
            self.animation_frame_count = 2

        self.image = pygame.image.load(self.animation_frame[self.rotation][self.animation_frame_count]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.original_image = copy.deepcopy(self.image)

    def update(self, keys, obstacles):
        from events.collisions import custom_sprite_collider

        if keys[pygame.K_LSHIFT]:
            self.speed = 2
        else:
            self.speed = 1

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.rotation = LEFT
            if custom_sprite_collider(self, obstacles):
                self.rect.x += self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.rotation = RIGHT
            if custom_sprite_collider(self, obstacles):
                self.rect.x -= self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.rotation = UP
            if custom_sprite_collider(self, obstacles):
                self.rect.y += self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.rotation = DOWN
            if custom_sprite_collider(self, obstacles):
                self.rect.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_UP] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            self.update_sprite(keys)

        else:
            self.animation_frame_count = 1
            self.image = pygame.image.load(
                self.animation_frame[self.rotation][self.animation_frame_count]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.original_image = copy.deepcopy(self.image)
