import pygame


class GenericObject(pygame.sprite.Sprite):

    def __init__(self, x, y, url):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.obj_image = pygame.image.load(url)

    def draw_obj_image(self, screen):
        return

    def draw(self, screen):
        self.draw_obj_image(screen)
