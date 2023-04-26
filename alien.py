# alien.py
import pygame
from pygame.locals import *
import random

# Alien class definition
class Alien:
    # Initialize the alien object with the given screen width and y position
    def __init__(self, screen_width, y):
        self.image = pygame.image.load("alien.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = y
        self.speed = 2
        self.direction_change_counter = 0

    # Draw the alien on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Update the alien's position and movement behavior
    def update(self, screen):
        self.move_randomly()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Keep the alien within the horizontal screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()

        # Set the vertical limits for the alien's movement
        upper_limit = screen.get_height() * (1 / 2)
        lower_limit = 0

        # Keep the alien within the vertical screen boundaries
        if self.rect.top < lower_limit:
            self.rect.top = lower_limit
        if self.rect.bottom > upper_limit:
            self.rect.bottom = upper_limit

    # Move the alien randomly within the allowed boundaries
    def move_randomly(self):
        if self.direction_change_counter == 0:  # Only change direction when the counter is 0
            random_direction = random.choice([-1, 0, 1])
            self.speed_x = random_direction * self.speed
            random_direction = random.choice([-1, 0, 1])
            self.speed_y = random_direction * self.speed
            # Reset the counter to a random value between 10 and 50
            self.direction_change_counter = random.randint(10, 50)
        else:
            # Decrease the counter by 1 to keep track of direction change intervals
            self.direction_change_counter -= 1
