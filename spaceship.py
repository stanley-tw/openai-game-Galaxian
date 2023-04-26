# spaceship.py
import pygame
from pygame.locals import *

# Spaceship class definition
class Spaceship:
    # Initialize the spaceship object with the given screen dimensions
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 5
        self.speed_y = 5

    # Draw the spaceship on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Set the horizontal speed for moving left
    def move_left(self):
        self.speed_x = -5

    # Set the horizontal speed for moving right
    def move_right(self):
        self.speed_x = 5

    # Set the vertical speed for moving up
    def move_up(self):
        self.speed_y = -5

    # Set the vertical speed for moving down
    def move_down(self):
        self.speed_y = 5

    # Update the spaceship's position based on its current speed
    def update(self, screen):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Keep the spaceship within the horizontal screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()

        # Set the vertical limits for the spaceship's movement
        lower_limit = screen.get_height() * (1 / 2)
        upper_limit = screen.get_height() - self.rect.height

        # Keep the spaceship within the vertical screen boundaries
        if self.rect.top < lower_limit:
            self.rect.top = lower_limit
        if self.rect.bottom > upper_limit:
            self.rect.bottom = upper_limit
