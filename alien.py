# alien.py
import pygame
from pygame.locals import *

class Alien:
    def __init__(self, screen_width, y):
        self.image = pygame.image.load("alien.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = y
        self.speed = 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen):
        self.rect.x += self.speed
        if self.rect.right >= screen.get_width() or self.rect.left <= 0:
            self.speed = -self.speed
