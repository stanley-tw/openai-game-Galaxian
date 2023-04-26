# missile.py
import pygame

# Missile class definition
class Missile:
    # Initialize the missile object with the given x and y positions and an optional speed argument
    def __init__(self, x, y, speed=5):
        # Create a surface for the missile and fill it with a color (red in this case)
        self.image = pygame.Surface((4, 8))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        
        # Set the initial position of the missile
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed

    # Update the missile's position by moving it vertically upwards
    def update(self):
        self.rect.y -= self.speed

    # Draw the missile on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
