import pygame
from ecs_manager import ECSManager
from systems.movement import MovementSystem
from systems.render import RenderSystem
from systems.collision import CollisionSystem
from entities.player import Player
from entities.asteroid import Asteroid
import constants
import os

os.environ['SDL_AUDIODRIVER'] = 'dummy'

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

ecs_manager = ECSManager()

# Add systems
ecs_manager.add_system(MovementSystem())
ecs_manager.add_system(RenderSystem(screen))
ecs_manager.add_system(CollisionSystem())

# Create a surface for the player
# Method 1: Create a simple colored surface
player_surface = pygame.Surface((50, 50))  # Create a 50x50 surface
player_surface.fill((255, 0, 0))  # Fill with red color

# Method 2: Load an image (use this if you have a player image file)
# player_surface = pygame.image.load('player.png').convert_alpha()

# Create and add entities
player = Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2, player_surface)
ecs_manager.add_entity(player)

for _ in range(constants.ASTEROID_COUNT):
    asteroid = Asteroid(random_x, random_y, asteroid_surface)
    ecs_manager.add_entity(asteroid)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    ecs_manager.update(dt)

    pygame.display.flip()

pygame.quit()