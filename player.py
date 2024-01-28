import pygame

class Player:
    def __init__(self, size):
        self.pos = [500, 200]
        self.image = pygame.transform.scale(pygame.image.load("assets/playerf1.png"), size)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.jump_velocity = 7

        self.x_momentum = 0
        self.y_momentum = 0

        self.sliding_speed = 1

        self.y_acceleration = 0.2
        self.x_acceleration = 0.5

        self.max_y_velocity = 15
        self.max_x_velocity = 7
