# from particles import Particles
from player import Player
from map import Map
import pygame


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(obj, tls):
    collisions = {"top": False, "bottom": False, "left": False, "right": False}
    obj.rect.x += obj.x_momentum
    hit_list = collision_test(obj.rect, tls)
    for tiles in hit_list:
        if obj.x_momentum > 0:
            obj.rect.right = tiles.left
            collisions["right"] = True
        elif obj.x_momentum < 0:
            obj.rect.left = tiles.right
            collisions["left"] = True
    obj.rect.y += obj.y_momentum
    hit_list = collision_test(obj.rect, tls)
    for tiles in hit_list:
        if obj.y_momentum > 0:
            obj.rect.bottom = tiles.top
            # obj.y_momentum = obj.y_acceleration
            collisions["bottom"] = True
        elif obj.y_momentum < 0:
            obj.rect.top = tiles.bottom
            collisions["top"] = True
    return collisions


def get_death_collisions(obj, tls):
    # obj.rect.x += obj.x_momentum
    hit_list = collision_test(obj.rect, tls)
    for tiles in hit_list:
        return True
    # obj.rect.y += obj.y_momentum
    hit_list = collision_test(obj.rect, tls)
    for tiles in hit_list:
        return True


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player((0.75*self.map.tile_size, 1.5*self.map.tile_size))
        self.all_tiles_rects = []
        self.all_deadly_tiles_rects = []


        self.start_tile = None
        self.end_tile = None
        self.interact_tile = None

        self.get_map_points()

    def to_next_map(self):
        self.map.next_map()
        self.get_map_points()
        self.player.rect.midbottom = self.start_tile.midbottom
        # self.all_deadly_tiles_rects = []


    def get_map_points(self):
        for y in range(len(self.map.map)):
            for x in range(len(self.map.map[y])):
                if self.map.map[y][x] == 72:
                    self.start_tile = pygame.rect.Rect(self.map.tile_size * x, self.map.tile_size * y, self.map.tile_size, self.map.tile_size)
                if self.map.map[y][x] == 73:
                    self.end_tile = pygame.rect.Rect(self.map.tile_size * x, self.map.tile_size * y, self.map.tile_size, self.map.tile_size)
                if self.map.map[y][x] == 74:
                    self.interact_tile = pygame.rect.Rect(self.map.tile_size * x, self.map.tile_size * y, self.map.tile_size, self.map.tile_size)

