import pygame
import random
from fish import load_fish_tiles, spawn_fish  # Import functions from fish.py

# Initialize Pygame and the mixer for music
pygame.init()

# Set up display (using the halved screen size)
screen_width, screen_height = 1008, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# Load and split the fish tiles
fish_list = load_fish_tiles("assets/fish_tiles.png")  # Path to your 16x16 tile sheet

# Spawn fish
fish_objects = spawn_fish(fish_list, 10, screen_width, screen_height)

# Load and scale the map
map_image = pygame.image.load("assets/seamap.png")
map_image = pygame.transform.scale(map_image, (screen_width, screen_height))

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill((255, 255, 255))

    # Draw the scaled map
    screen.blit(map_image, (0, 0))

    # Update fish movement
    for fish in fish_objects:
        fish.move(screen_width, screen_height)  # Move each fish
        fish.draw(screen)  # Draw each fish

    # Update display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # 60 FPS

pygame.quit()
