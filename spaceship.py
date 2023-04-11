# spaceship.py
import pygame
from pygame.locals import *

class Spaceship:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height - 10
        self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.speed = -5

    def move_right(self):
        self.speed = 5

    def stop_moving(self):
        self.speed = 0

    def update(self, screen):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
