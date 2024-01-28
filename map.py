import pygame
import pickle

class Map:
    def __init__(self) -> None:
        # self.tile_size = 40
        self.maps = self.load_map()  # Load the matrice for the map
        self.map_index = 0
        bar = pygame.image.load("assets/BG-Bar.png")
        forest = pygame.image.load("assets/BG_Forest.png")
        desert = pygame.image.load("assets/BG-Desert.png")
        candy = pygame.image.load("assets/BG-Candy.png")

        self.backgrounds = [bar, bar, bar, bar, forest, forest, forest, forest, desert, desert, desert, desert, candy, candy, candy, candy]
        self.map = self.maps[self.map_index]
        # self.textures = {
        #     1: pygame.transform.scale(pygame.image.load("assets/obstacle.png"), (self.tile_size, self.tile_size))
        # }

        self.textures = {}
        self.tile_size = 40
        ts = int(self.tile_size/2)
        self.tileset = pygame.image.load("assets/Tileset_v7.png")

        tile_width = self.tileset.get_width() // ts
        tile_height = self.tileset.get_height() // ts

        self.tiles = []

        self.tiles_is_empty = {}

        for y in range(tile_height):
            for x in range(tile_width):
                tile = self.tileset.subsurface(pygame.Rect(x * ts, y * ts, ts, ts))
                self.tiles.append(tile)

        self.available_tiles = []
        for tile in range(len(self.tiles)):
            for x in range(ts):
                for y in range(ts):
                    if self.tiles[tile].get_at((x, y)) != (255, 255, 255):
                        break
                else:
                    continue
                self.tiles_is_empty[tile] = True
                self.textures[tile] = pygame.transform.scale(self.tiles[tile], (self.tile_size, self.tile_size))
                self.available_tiles.append(tile)
                break
            else:
                self.tiles_is_empty[tile] = False
                self.textures[tile] = pygame.transform.scale(self.tiles[tile], (self.tile_size, self.tile_size))

    def load_map(self):
        return pickle.load(open("map.txt", "rb"))

    def next_map(self):
        self.map_index += 1
        self.map = self.maps[self.map_index]