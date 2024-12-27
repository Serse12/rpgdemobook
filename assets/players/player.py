import pygame
from config import *
from .playerconfig import *
from assets.objectsPackage.objects import GenericObject


class Player(GenericObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(FIRST_TREE).convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Optional: Resize to 50x50
        self.rect = self.image.get_rect()  # Get the rectangle of the image
        self.rect.topleft = (x, y)  # Set initial position
        self._layer = PLAYER_LAYER
        self.speed = TILE_SIZE
        self.rotation = UP
        self.collider_rect = self.rect

    def update(self, keys, obstacles):
        from events.collisions import custom_sprite_collider
        # Save original position for potential collision rollback
        original_position = self.rect.topleft

        # Handle movement and update position
        if pygame.K_LEFT in keys:
            self.rect.x -= self.speed
            self.rotation = LEFT
        if pygame.K_RIGHT in keys:
            self.rect.x += self.speed
            self.rotation = RIGHT
        if pygame.K_UP in keys:
            self.rect.y -= self.speed
            self.rotation = UP
        if pygame.K_DOWN in keys:
            self.rect.y += self.speed
            self.rotation = DOWN

        # Check for collisions and revert if necessary
        if custom_sprite_collider(self, obstacles):
            self.rect.topleft = original_position
