# main.py
import pygame
from pygame.locals import *
from spaceship import Spaceship
from alien import Alien

pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galaxian")

# Game objects
spaceship = Spaceship(screen_width, screen_height)
aliens = [Alien(screen_width, y * 50) for y in range(2)]

# Clock
clock = pygame.time.Clock()

def draw_objects():
    screen.fill((0, 0, 0))
    spaceship.draw(screen)
    for alien in aliens:
        alien.draw(screen)
    pygame.display.flip()

def game_loop():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    spaceship.move_left()
                if event.key == K_RIGHT:
                    spaceship.move_right()
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    spaceship.stop_moving()

        spaceship.update(screen)
        for alien in aliens:
            alien.update(screen)
        draw_objects()

if __name__ == "__main__":
    game_loop()
    pygame.quit()
