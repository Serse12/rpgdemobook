import pygame.color

from GenericMap.GenericMap import GenericMap

from config import *
from events.collisions import *
from assets.objectsPackage.tile import Tile


class FirstMap(GenericMap):
    objs_in_map = []
    objs_in_map.append(Tree(0 * TILE_SIZE, 0 * TILE_SIZE, FIRST_TREE))
    objs_in_map.append(Tree(0 * TILE_SIZE, 1 * TILE_SIZE, FIRST_TREE))
    objs_in_map.append(Tree(0 * TILE_SIZE, 2 * TILE_SIZE, FIRST_TREE))
    objs_in_map.append(Tree(5 * TILE_SIZE, 5 * TILE_SIZE, FIRST_TREE))

    player = Player(2*TILE_SIZE, 2*TILE_SIZE)  # Replace with your image file

    def __init__(self, screen):
        super().__init__(8, 8, 0, 0, screen)
        self.set_wallpaper("./FirstMap/img/wallpaper1.png")
        self.set_tiles("./FirstMap/img/housetile.png")

    def load_playable_map(self):
        self.all_sprites.add(self.objs_in_map)
        self.layerupdates.add(self.objs_in_map)
        self.mapobjects.add(self.objs_in_map)

        # for i in range(0, self.width):
        #    for j in range(0, self.height):
        #        rec = pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        #        pygame.draw.rect(self.screen, pygame.color.Color(0, 0, 0),
        #                         rec, 1)

        for i in range(0, self.width):
            for j in range(0, self.height):
                self.maptiles.add(Tile(i * TILE_SIZE, j * TILE_SIZE, HOUSE_TILE))
                self.layerupdates.add(Tile(i * TILE_SIZE, j * TILE_SIZE, HOUSE_TILE))

    def load_players_and_npc(self):
        self.player_group.add(self.player)
        self.all_sprites.add(self.player)
        self.layerupdates.add(self.player)


