import pygame

class Particles:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()



class ParticleGroup:
    def __init__(self):
        self.all_particles = pygame.sprite.Group()


class Particle:
    def __init__(self, position, velocity, size):
        self.rect = pygame.rect.Rect(position[0], position[1], size, size)