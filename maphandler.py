from FirstMap.FirstMap import FirstMap


class MapHandler:
    maps_mapping = {0: FirstMap}

    def __init__(self):
        self.currentMapID = 0

    def set_mapid(self, mapid):
        self.currentMapID = mapid

    def get_current_map(self):
        map_class = self.maps_mapping[self.currentMapID]
        if map_class is None:
            raise ValueError(f"No map found for ID {self.currentMapID}")

        return map_class(None)
