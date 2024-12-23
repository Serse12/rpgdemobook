import sys
from maphandler import MapHandler
from config import *
from assets.players.player import *


def main():
    pygame.init()
    mapHandler = MapHandler()

    black = 0, 0, 0
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        map_to_load = mapHandler.get_current_map()
        map_to_load.set_screen(screen)

        all_sprites = map_to_load.all_sprites

        keys = pygame.key.get_pressed()
        all_sprites.update(keys)

        screen.fill(black)
        map_to_load.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
