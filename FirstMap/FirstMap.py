import pygame.color

from GenericMap.GenericMap import GenericMap

from config import *
from events.collisions import *
from assets.objectsPackage.objects import Tile
from assets.players.alice import Alice
from assets.players.bob import Bob
from assets.objectsPackage.lights import Torch, LightSource


class FirstMap(GenericMap):
    items_in_a_tile = list()
    items_in_a_tile.append("")
    items_in_a_tile.append([Tile])
    items_in_a_tile.append([Tree, Tile])
    items_in_a_tile.append([Tile, Alice])
    items_in_a_tile.append([Tile, Bob])
    items_in_a_tile.append([Tile, Torch])

    map_to_render = ["2222222222222222",
                     "2111111111115342",
                     "2111111111111112",
                     "2111115111111112",
                     "2115111151111512",
                     "2111111111111112",
                     "2111111111111112",
                     "2222222222222222", ]

    def __init__(self, screen, player):
        super().__init__(0, 0, screen, player, darkness=100)
        self.set_wallpaper("./FirstMap/img/wallpaper1.png")
        self.set_tiles("./FirstMap/img/housetile.png")

    def load_playable_map(self):
        i = 0
        j = 0
        for row in self.map_to_render:
            for index in row:
                for element in self.items_in_a_tile[int(index)]:
                    obj = None
                    if element is Tree:
                        obj = Tree(j * TILE_SIZE, i * TILE_SIZE, SECOND_TREE)
                    if element is Tile:
                        obj = Tile(j * TILE_SIZE, i * TILE_SIZE, HOUSE_TILE)
                    if element is Alice:
                        obj = Alice(j * TILE_SIZE, i * TILE_SIZE)
                    if element is Bob:
                        obj = Bob(j * TILE_SIZE, i * TILE_SIZE)
                    if element is Torch:
                        obj = Torch(j * TILE_SIZE, i * TILE_SIZE)

                    if isinstance(obj, Tile):
                        self.all_sprites.add(obj)
                        self.layerupdates.add(obj)
                        self.maptiles.add(obj)

                    else:
                        if isinstance(obj, GenericObject):
                            self.all_sprites.add(obj)
                            self.layerupdates.add(obj)
                            self.mapobjects.add(obj)

                        if isinstance(obj, LightSource):
                            self.light_sources_group.add(obj)

                j += 1
            i += 1
            j = 0
