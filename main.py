# main.py
import pygame
from pygame.locals import *
from spaceship import Spaceship
from alien import Alien
from missile import Missile
import sys

pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galaxian")

num_aliens = 2

# Initialize game objects
spaceship = Spaceship(screen_width, screen_height)  # Create the player's spaceship
aliens = [Alien(screen_width, y * 50) for y in range(num_aliens)]  # Create aliens
missiles = []  # List to store all active missiles

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Display a congratulations message in the center of the screen
def display_congratulations_message(screen):
    font = pygame.font.Font(None, 42)
    text = font.render("Congratulations!", True, (255, 215, 0))
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text, text_rect)

    # Add the following lines to display "Press SPACE to continue" below the main message
    font_small = pygame.font.Font(None, 24)
    text_small = font_small.render("Press SPACE to continue", True, (255, 255, 255))
    text_small_rect = text_small.get_rect()
    text_small_rect.center = (screen_width // 2, screen_height // 2 + 50)
    screen.blit(text_small, text_small_rect)

    pygame.display.flip()

# Draw game objects on the screen
def draw_objects():
    screen.fill((0, 0, 0))  # Clear the screen with a black background
    spaceship.draw(screen)  # Draw the player's spaceship
    for alien in aliens:  # Draw each alien
        alien.draw(screen)
    for missile in missiles[:]:  # Update and draw each missile
        missile.update()
        if missile.rect.bottom < 0:  # Remove missile when it goes off the screen
            missiles.remove(missile)
        else:
            for alien in aliens[:]:  # Check for collisions between missile and aliens
                if missile.rect.colliderect(alien.rect):
                    missiles.remove(missile)  # Remove the missile
                    aliens.remove(alien)  # Remove the alien
                    break  # Break out of the inner loop to avoid using a removed missile
        missile.draw(screen)  # Draw the missile
    pygame.display.flip()  # Update the display

def display_countdown(screen):
    screen.fill((0, 0, 0))  # Clear the screen for the next number
    for count in range(3, 0, -1):
        font = pygame.font.Font(None, 100 - (count * 20))
        text = font.render(str(count), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (screen_width // 2, screen_height // 2)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)  # Wait for 1 second
        screen.fill((0, 0, 0))  # Clear the screen for the next number


# Main game loop
def game_loop():
    global aliens
    global num_aliens
 
    pygame.key.stop_text_input()
    display_countdown(screen)
    running = True
    while running:
        clock.tick(60)  # Limit the frame rate to 60 FPS
        if not aliens:  # Check if all aliens are eliminated
            display_congratulations_message(screen)  # Display the victory message
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    num_aliens += 1
                    aliens = [Alien(screen_width, y * 50) for y in range(num_aliens)]  # Reset aliens
                    display_countdown(screen)
            continue

        # Process keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship.move_left()  # Move the spaceship left
        if keys[pygame.K_RIGHT]:
            spaceship.move_right()  # Move the spaceship right
        if keys[pygame.K_UP]:
            spaceship.move_up()  # Move the spaceship up
        if keys[pygame.K_DOWN]:
            spaceship.move_down()  # Move the spaceship down

        # Process events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    missile = Missile(spaceship.rect.centerx, spaceship.rect.top)  # Create a missile
                    missiles.append(missile)  # Add the missile to the list of active missiles

        # Update game objects
        spaceship.update(screen)
        for alien in aliens:
            alien.update(screen)

        # Draw game objects
        draw_objects()

if __name__ == "__main__":
    game_loop()  # Start the game loop
    pygame.quit()  # Quit the game when the loop ends
