import pygame
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

    def load_image(self):
        self.image = pygame.image.load(FIRST_TREE).convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (50, 50))  # Optional: Resize to 50x50
        self.rect = self.image.get_rect()  # Get the rectangle of the image
        self.rect.topleft = (x, y)  # Set initial position

    def update(self, keys):
        # Handle movement with arrow keys
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
