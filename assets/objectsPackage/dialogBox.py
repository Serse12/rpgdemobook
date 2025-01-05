import pygame
from config import *
import events_config


class DialogBox:
    def __init__(self, screen, texts):
        self.image_rect = None
        self.image = None
        self.dialog_box_width = WINDOW_WIDTH
        self.dialog_box_height = WINDOW_HEIGHT / 3
        self.rect = pygame.Rect(0, 2 * WINDOW_HEIGHT / 3, self.dialog_box_width, self.dialog_box_height)
        self.font = pygame.font.Font(None, 35)
        self.font_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        self.texts = texts
        self.screen = screen
        self.dialog_index = 0

    def load(self):
        events_config.DIALOG_BOX_EVENT = 1
        events_config.DIALOG_INSTANCE = self

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.rect)
        self.image = pygame.image.load(self.texts[self.dialog_index][0])
        self.image = pygame.transform.scale(self.image, (self.dialog_box_height, self.dialog_box_height))
        self.image_rect = self.image.get_rect(topleft=self.rect.topleft)
        pygame.draw.rect(self.screen, self.bg_color, self.image_rect)
        text_surface = self.font.render(self.texts[self.dialog_index][1], True, self.font_color)
        text_rect = text_surface.get_rect(topleft=self.image_rect.topright)
        self.screen.blit(self.image, self.image_rect)
        self.screen.blit(text_surface, text_rect)

    def update(self, keys):
        from events.collisions import obj_is_adiacet_to_player
        if pygame.K_ESCAPE in keys:
            self.exit_dialog()
        if pygame.K_x in keys:
            self.dialog_index = self.dialog_index + 1
            if self.dialog_index >= len(self.texts):
                self.exit_dialog()

    def exit_dialog(self):
        events_config.DIALOG_BOX_EVENT = 0
        events_config.DIALOG_INSTANCE = None
        self.dialog_index = 0
