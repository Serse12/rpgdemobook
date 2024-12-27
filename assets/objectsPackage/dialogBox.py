import pygame
from config import *
import events_config


class DialogBox:
    def __init__(self, screen, text):
        self.rect = pygame.Rect(0, 2 * WINDOW_HEIGHT / 3, WINDOW_WIDTH, WINDOW_HEIGHT / 3)
        # self.inner_area = pygame.Rect((-28, -15, self.rect[2], self.rect[3]))
        self.font = pygame.font.Font(None, 35)
        self.font_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        self.text = text
        self.screen = screen

    def load(self):
        events_config.DIALOG_BOX_EVENT = 1
        events_config.DIALOG_INSTANCE = self

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)
