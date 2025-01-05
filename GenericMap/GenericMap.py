import pygame
from config import *
import copy
import numpy as np


class GenericMap:

    def __init__(self, x, y, screen, player, darkness):
        self.wallpaper = None
        self.spawn_point = None
        self.tiles = None
        # in pixel
        self.width = WINDOW_WIDTH
        # in pixel
        self.height = WINDOW_HEIGHT
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.mapobjects = pygame.sprite.Group()
        self.light_sources_group = pygame.sprite.Group()
        self.maptiles = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.layerupdates = pygame.sprite.LayeredUpdates()
        self.player = player
        self.darkness = darkness

        # self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.set_spawn_point(x, y)

    def set_screen(self, screen):
        self.screen = screen

    def set_spawn_point(self, x, y):
        self.spawn_point = (x, y)

    def set_wallpaper(self, url):
        self.wallpaper = pygame.image.load(url)

    def set_tiles(self, url):
        self.tiles = pygame.image.load(url)

    def draw_wallpaper(self):
        self.wallpaper = pygame.transform.scale(self.wallpaper, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.blit(self.wallpaper, (0, 0))

    def load_playable_map(self):
        return

    def load_players_and_npc(self):
        if self.player:
            self.player_group.add(self.player)
            self.all_sprites.add(self.player)
            self.layerupdates.add(self.player)
        return

    def load_all(self):
        self.load_playable_map()
        self.load_players_and_npc()

    def draw_shadows(self):
        # Create a semi-transparent surface for the shadow
        shadow_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # Define the shadow color with the desired alpha value (e.g., 128 for 50% transparency)
        shadow_color = (0, 0, 0, self.darkness)  # Black color with 50% transparency

        # Fill the shadow surface with the shadow color
        shadow_surface.fill(shadow_color)

        # Blit the shadow surface onto the main surface
        self.screen.blit(shadow_surface, (0, 0))


    def draw_lights(self):
        # Create a copy of the original image
        surface = self.screen
        light_sources = self.light_sources_group.sprites()

        # 4 perché rgba
        light_array = np.zeros((self.width, self.height, 4), dtype=np.float32)

        for light_source in light_sources:
            color = light_source.light_color
            max_brightness = light_source.light_power
            light_center_x = light_source.rect.center[0]
            light_center_y = light_source.rect.center[1]
            radius = light_source.light_radius

            xx, yy = np.meshgrid(np.arange(self.width), np.arange(self.height), indexing='ij')
            #  xx, yy = np.ogrid[:self.height, :self.width]
            dist = np.sqrt((xx - light_center_x) ** 2 + (yy - light_center_y) ** 2)

            mask = dist < radius

            # Calculate brightness contribution
            brightness = max_brightness * (1 - dist / radius)
            brightness = np.clip(brightness, 0, 255)

            # Add color contribution to the light array
            light_array[mask, 0] += color[0] * (brightness[mask] / 255)  # Red
            light_array[mask, 1] += color[1] * (brightness[mask] / 255)  # Green
            light_array[mask, 2] += color[2] * (brightness[mask] / 255)  # Blue
            light_array[mask, 3] += brightness[mask]  # Alpha (brightness)

            # Clamp the light array to valid color values
        light_array = np.clip(light_array, 0, 255).astype(np.uint8)

        # Convert NumPy array to Pygame surface
        light_surface = pygame.surfarray.make_surface(light_array[:, :, :3])
        light_surface.set_alpha(255)  # Apply maximum alpha for blending

        # Blit the light surface onto the screen
        surface.blit(light_surface, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

    def draw(self):
        self.draw_wallpaper()
        self.layerupdates.draw(self.screen)
        self.draw_shadows()
        self.draw_lights()
