from game import *
import pygame
import time
import math
import numpy

pygame.init()
pygame.display.set_caption("hello world!")
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
max_fps = 60

game = Game()

previous_left = 0
previous_right = 0

game.player.rect.midbottom = game.start_tile.midbottom

playing = True
while playing:
    screen.fill((120, 120, 120))
    screen.blit(game.map.backgrounds[game.map.map_index], (0, 0))




    # Afficher les tiles
    game.all_tiles_rects = []
    game.all_deadly_tiles_rects = []
    for y in range(len(game.map.map)):
        for x in range(len(game.map.map[y])):
            if not game.map.map[y][x] in [0, 68, 69, 70, 71, 72, 73, 74]:
                game.all_tiles_rects.append(pygame.rect.Rect(game.map.tile_size * x, game.map.tile_size * y, game.map.tile_size, game.map.tile_size))
                screen.blit(game.map.textures[game.map.available_tiles[game.map.map[y][x]]], (game.map.tile_size * x, game.map.tile_size * y))
            elif not game.map.map[y][x] in [0, 72, 73, 74]:
                #  ALL TILES THAT KILL THE PLAYER
                screen.blit(game.map.textures[game.map.available_tiles[game.map.map[y][x]]], (game.map.tile_size * x, game.map.tile_size * y))
                game.all_deadly_tiles_rects.append(pygame.rect.Rect(game.map.tile_size * x, game.map.tile_size * y, game.map.tile_size, game.map.tile_size))


    # MOVE PLAYER AND TEST FOR COLLISIONS

    collisions = move(game.player, game.all_tiles_rects)

    if not collisions["bottom"] and game.player.y_momentum < game.player.max_y_velocity and not collisions["left"] and not collisions["right"]:
        game.player.y_momentum += game.player.y_acceleration


    # CONTROLS

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        if not collisions["right"]:
            if not game.player.x_momentum >= game.player.max_x_velocity:
                game.player.x_momentum += game.player.x_acceleration
    if collisions["right"]:
        previous_right = 0
        game.player.x_momentum = 0
        if game.player.y_momentum > game.player.sliding_speed:  # 0
            game.player.y_momentum = game.player.sliding_speed  # 0

    if keys[pygame.K_q]:
        if not collisions["left"]:
            if not game.player.x_momentum <= -game.player.max_x_velocity:
                game.player.x_momentum -= game.player.x_acceleration
    if collisions["left"]:
        previous_left = 0
        game.player.x_momentum = 0
        if game.player.y_momentum > game.player.sliding_speed:  # 0
            game.player.y_momentum = game.player.sliding_speed  # 0

    if collisions["top"]:
        game.player.y_momentum = 0

    if not (collisions["left"] or collisions["right"]) and not keys[pygame.K_q] and not keys[pygame.K_d]:
        if game.player.x_momentum < 0:
            if collisions["bottom"]:
                if game.player.x_momentum < -game.player.x_acceleration * 3:
                    game.player.x_momentum += game.player.x_acceleration * 3
                else:
                    game.player.x_momentum = 0
            else:
                if game.player.x_momentum < -game.player.x_acceleration * 2:
                    game.player.x_momentum += game.player.x_acceleration * 2
                else:
                    game.player.x_momentum = 0
        elif game.player.x_momentum > 0:
            if collisions["bottom"]:
                if game.player.x_momentum > game.player.x_acceleration * 3:
                    game.player.x_momentum -= game.player.x_acceleration * 3
                else:
                    game.player.x_momentum = 0
            else:
                if game.player.x_momentum > game.player.x_acceleration * 2:
                    game.player.x_momentum -= game.player.x_acceleration * 2
                else:
                    game.player.x_momentum = 0

    if get_death_collisions(game.player, game.all_deadly_tiles_rects):
        game.player.rect.midbottom = game.start_tile.midbottom
        game.player.y_momentum = 0
        game.player.x_momentum = 0


    if not 1080 > game.player.rect.centerx > 0 or not 720 > game.player.rect.centery > 0:
        game.player.rect.midbottom = game.start_tile.midbottom
        game.player.y_momentum = 0
        game.player.x_momentum = 0

    # print(math.dist(game.player.rect.center, game.end_tile.center))
    if math.dist(game.player.rect.center, game.end_tile.center) < 15:
        game.to_next_map()

    screen.blit(game.player.image, game.player.rect)
    pygame.draw.rect(screen, (0, 255, 0), game.player.rect, 2)

    pygame.display.flip()
    clock.tick(max_fps)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            time.sleep(0.5)
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and collisions["bottom"]:
                game.player.y_momentum = -game.player.jump_velocity

            if event.key == pygame.K_SPACE and (collisions["left"] or previous_left < 8):
                game.player.y_momentum = -game.player.jump_velocity
                game.player.x_momentum = game.player.max_x_velocity * 1

            if event.key == pygame.K_SPACE and (collisions["right"] or previous_right < 8):
                game.player.y_momentum = -game.player.jump_velocity
                game.player.x_momentum = -game.player.max_x_velocity * 1

    previous_left += 1
    previous_right += 1
