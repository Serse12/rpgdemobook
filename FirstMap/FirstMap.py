import pygame.color

from GenericMap.GenericMap import GenericMap

from assets.objectsPackage.objects import *
from assets.objectsPackage.tree import *
from assets.objectsPackage.tile import *
from assets.players.player import *


class FirstMap(GenericMap):
    objs_in_map = []
    objs_in_map.append(Tree(0 * TILE_SIZE, 0 * TILE_SIZE, FIRST_TREE))
    objs_in_map.append(Tree(0 * TILE_SIZE, 1 * TILE_SIZE, FIRST_TREE))
    objs_in_map.append(Tree(0 * TILE_SIZE, 2 * TILE_SIZE, FIRST_TREE))

    player = Player(0, 0)  # Replace with your image file
    all_sprites = pygame.sprite.Group(player)

    def __init__(self, screen):
        super().__init__(8, 8, 0, 0, screen)
        self.set_wallpaper("./FirstMap/img/wallpaper1.png")
        self.set_tiles("./FirstMap/img/housetile.png")

    def load_assets(self):
        self.player.load_image("path/to/player_image.png")  # Replace with the actual path

    def draw_playable_map(self):
        for x in self.objs_in_map:
            x.draw_obj_image(self.screen)

        # for i in range(0, self.width):
        #    for j in range(0, self.height):
        #        rec = pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        #        pygame.draw.rect(self.screen, pygame.color.Color(0, 0, 0),
        #                         rec, 1)

        for i in range(0, self.width):
            for j in range(0, self.height):
                tile = Tile(i * TILE_SIZE, j * TILE_SIZE, HOUSE_TILE)
                tile.draw_obj_image(self.screen)

    def draw_players_and_npc(self):
        self.all_sprites.draw(self.screen)


