import pygame
from constants import *
from bearship import BearShip
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
# Player.containers = (updatable, drawable)
BearShip.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
#    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    player = BearShip(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        # Limits framerate to 60 FPS
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()