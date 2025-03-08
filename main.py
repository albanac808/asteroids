import pygame
from ecs_manager import ECSManager
from systems.movement import MovementSystem
from systems.render import RenderSystem
from systems.collision import CollisionSystem
from entities.player import Player
from entities.asteroid import Asteroid
import constants

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

ecs_manager = ECSManager()

# Add systems
ecs_manager.add_system(MovementSystem())
ecs_manager.add_system(RenderSystem(screen))
ecs_manager.add_system(CollisionSystem())

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