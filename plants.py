import pygame
import random

class Plant:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

        self.plant_image = pygame.image.load("aquatic-plant.png").convert_alpha()
        self.plant_image = pygame.transform.scale(self.plant_image, (self.width, self.height))

    def move(self):
        self.x -= self.vel

    def draw(self, win):
        win.blit(self.plant_image, (self.x, self.y))
