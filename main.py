import sys

from config import *
import events_config
import pygame

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

from maphandler import MapHandler
from FirstMap.FirstMap import FirstMap


def main():
    black = 0, 0, 0

    mapHandler = MapHandler()
    # map_to_load = mapHandler.get_current_map()
    firstMap = FirstMap(screen)
    firstMap.load_all()

    while True:
        keys = set()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys.add(event.key)

        # map_to_load = mapHandler.get_current_map()
        # keys = pygame.key.get_pressed()
        if events_config.DIALOG_BOX_EVENT:
            firstMap.mapobjects.update(screen, keys, firstMap.player)

        else:
            firstMap.player.update(keys, firstMap.mapobjects)
            firstMap.mapobjects.update(screen, keys, firstMap.player)

        screen.fill(black)
        firstMap.draw()

        if events_config.DIALOG_BOX_EVENT:
            events_config.DIALOG_INSTANCE.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
