from config import *
import events_config
import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("ciao")
clock = pygame.time.Clock()


from maphandler import MapHandler
from FirstMap.FirstMap import FirstMap
from LoadingScreen.loadingscreen import LoadingScreen
from assets.players.player import Player

def main():
    # mapHandler = MapHandler()
    # map_to_load = mapHandler.get_current_map()

    loadingscreen = LoadingScreen(screen)
    loadingscreen.draw()
    pygame.display.flip()

    player = Player(2 * TILE_SIZE, 2 * TILE_SIZE)  # Replace with your image file

    firstMap = FirstMap(screen, player)
    firstMap.load_all()

    temp_stop_input = False

    running = True
    while running:
        keys = set()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if events_config.DIALOG_BOX_EVENT and event.type == pygame.KEYDOWN:
                keys.add(event.key)

        if events_config.DIALOG_BOX_EVENT:
            events_config.DIALOG_INSTANCE.update(keys)
            if not events_config.DIALOG_BOX_EVENT:
                temp_stop_input = True

        else:
            if temp_stop_input:
                pressed_keys = pygame.key.get_pressed()
                if not pressed_keys[pygame.K_x]:
                    temp_stop_input = False
            else:
                pressed_keys = pygame.key.get_pressed()
                player.update(pressed_keys, firstMap.mapobjects)
                firstMap.mapobjects.update(screen, pressed_keys, player)

        screen.fill('black')
        firstMap.draw()


        if events_config.DIALOG_BOX_EVENT:
            events_config.DIALOG_INSTANCE.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
