import pygame
import random
import math
import time  # <-- Add this import


# Fish class to represent individual fish
class Fish:
    def __init__(self, image, x, y):
        self.image = pygame.transform.scale(image, (14, 14))  # Scaling 16x16 to 14x14
        self.x = x
        self.y = y

        # Initial movement speeds are set to a very slow value
        self.base_speed_x = random.uniform(0.00001, 0.0001)
        self.base_speed_y = random.uniform(0.00001, 0.0001)

        # Tiny floating amplitude and frequency
        self.float_amplitude_x = random.uniform(0.01, 0.05)
        self.float_amplitude_y = random.uniform(0.1, 0.1)
        self.float_frequency_x = random.uniform(0.0001, 0.0005)
        self.float_frequency_y = random.uniform(0.0001, 0.0005)

        # Time variables for sine-wave calculation
        self.time_x = random.uniform(0, 2 * math.pi)
        self.time_y = random.uniform(0, 2 * math.pi)

        # Time tracking for direction change
        self.last_direction_change_time = time.time()  # Time of last direction change
        self.direction_change_interval = 1  # 3 seconds interval to change direction

    def move(self, screen_width, screen_height):
        """ Update fish position based on extremely slow floating motion and periodic direction change """

        # Update floating time variables
        self.time_x += self.base_speed_x
        self.time_y += self.base_speed_y

        # Use sine-wave for floating effect
        self.x += self.float_amplitude_x * math.sin(self.time_x)
        self.y += self.float_amplitude_y * math.cos(self.time_y)

        # Check if 3 seconds have passed since the last direction change
        current_time = time.time()
        if current_time - self.last_direction_change_time >= self.direction_change_interval:
            self.last_direction_change_time = current_time  # Reset the time
            # Randomly change the direction by adjusting the base speeds
            self.base_speed_x = random.uniform(0.0001, 0.001) * random.choice([-1, 1])  # Random horizontal direction
            self.base_speed_y = random.uniform(0.0001, 0.001) * random.choice([-1, 1])  # Random vertical direction

        # Keep fish within screen boundaries
        if self.x < 0:  # Left boundary
            self.x = 0
        elif self.x > screen_width - 8:  # Right boundary
            self.x = screen_width - 8

        if self.y < 0:  # Top boundary
            self.y = 0
        elif self.y > screen_height - 8:  # Bottom boundary
            self.y = screen_height - 8

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# Function to load and split the tile sheet into individual fish
def load_fish_tiles(sheet_path, tile_size=(16, 16), rows=4, cols=4):
    # Load the tile sheet
    sheet = pygame.image.load('assets/fish.png')

    fish_list = []

    # Loop through the rows and columns to cut the sheet into individual tiles
    for row in range(rows):
        for col in range(cols):
            # Get the position of the current tile in the tile sheet
            rect = pygame.Rect(col * tile_size[0], row * tile_size[1], tile_size[0], tile_size[1])
            # Extract the tile (fish) from the sheet
            fish_image = sheet.subsurface(rect)
            fish_list.append(fish_image)

    return fish_list


# Function to spawn fish at random positions on the screen
def spawn_fish(fish_list, num_fish, screen_width, screen_height):
    fish_objects = []
    for _ in range(num_fish):
        # Randomly choose a fish
        fish_image = random.choice(fish_list)
        # Randomly spawn fish at a position within the screen bounds
        x = random.randint(0, screen_width - fish_image.get_width())
        y = random.randint(0, screen_height - fish_image.get_height())
        # Create a Fish object and add it to the list
        fish_objects.append(Fish(fish_image, x, y))
    return fish_objects
