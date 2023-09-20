import pygame
import random

class Sharks:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6

        self.shark_image = pygame.image.load("shark.png").convert_alpha()
        self.shark_image = pygame.transform.scale(self.shark_image, (self.width, self.height))

    def move(self):
        self.x -= self.vel

    def draw(self, win):
        win.blit(self.shark_image, (self.x, self.y))
