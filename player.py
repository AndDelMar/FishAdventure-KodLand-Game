import pygame

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 35

        self.player_image = pygame.image.load("transparent-fish.png").convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (self.width, self.height))

    def draw(self, win):
        win.blit(self.player_image, (self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def check_collision(self, obstacle):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
            pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
        )
