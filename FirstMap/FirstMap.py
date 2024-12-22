from GenericMap.GenericMap import GenericMap


class FirstMap(GenericMap):
    def __init__(self, screen):
        super().__init__(5, 5, 0, 0, screen, "./FirstMap/img/wallpaper1.png")
