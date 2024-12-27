import events_config
from assets.objectsPackage.dialogBox import DialogBox
from assets.objectsPackage.objects import *
from config import *


class Tree(GenericObject):
    collider_rect: pygame.Rect = None

    dialogs = []
    dialogs.append("ciao")
    dialogs.append("come va?")
    dialogs.append("qual è il colmo per francesca?")
    dialogs.append("essere brutta!")
    dialogs.append("non è vero")
    dialogs.append("è staccarsi dal telefono")

    def __init__(self, x, y, url):
        super().__init__(x, y)
        self.height = self.width * 2
        self.image = pygame.image.load(url).convert_alpha()  # Load the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # Get the rectangle of the image
        self._layer = OBJ_LAYER
        self.collider_rect = pygame.Rect(x, y + self.height / 2, self.width, self.height / 2)
        self.dialog_index = 0

    def update(self, screen, keys, player):
        from events.collisions import obj_is_adiacet_to_player
        if pygame.K_ESCAPE in keys:
            if obj_is_adiacet_to_player(self, player):
                events_config.DIALOG_BOX_EVENT = 0
                events_config.DIALOG_INSTANCE = None
                self.dialog_index = 0
        if pygame.K_x in keys:
            if obj_is_adiacet_to_player(self, player):
                if self.dialog_index == len(self.dialogs):
                    events_config.DIALOG_BOX_EVENT = 0
                    events_config.DIALOG_INSTANCE = None
                    self.dialog_index = 0
                else:
                    DialogBox(screen, self.dialogs[self.dialog_index]).load()
                    self.dialog_index = self.dialog_index + 1
