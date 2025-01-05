import pygame
from config import *
from .playerconfig import *
from assets.objectsPackage.objects import GenericObject
import math
from assets.objectsPackage.dialogBox import DialogBox
import copy

class Bob(GenericObject):
    images_prefix = "./assets/tiles/pipoyaEdits_blackByrd/bob/"

    dialogs = [[AVATAR_DIR + "protagonista.png", "ciao"],
               [AVATAR_DIR + "bob.png", "sono Bob!"],
               [AVATAR_DIR + "protagonista.png", "caca pupu"]]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(self.images_prefix + "avanti2.png").convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Optional: Resize to 50x50
        self.rect = self.image.get_rect(topleft=(x, y))  # Get the rectangle of the image
        self.original_image = copy.deepcopy(self.image)
        self._layer = PLAYER_LAYER
        self.collider_rect = self.rect

    def update(self, screen, keys, player):
        from events.collisions import obj_is_adiacet_to_player
        if keys[pygame.K_x]:
            if obj_is_adiacet_to_player(self, player):
                DialogBox(screen, self.dialogs).load()
