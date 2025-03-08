import pygame
from components.position import Position
from components.collider import Collider

class CollisionSystem:
    def update(self, entities):
        collisions = []
        for i, entity1 in enumerate(entities):
            if entity1.has_component(Position) and entity1.has_component(Collider):
                pos1 = entity1.get_component(Position)
                col1 = entity1.get_component(Collider)
                for j, entity2 in enumerate(entities[i+1:]):
                    if entity2.has_component(Position) and entity2.has_component(Collider):
                        pos2 = entity2.get_component(Position)
                        col2 = entity2.get_component(Collider)
                        distance = pygame.math.Vector2(pos1.x - pos2.x, pos1.y - pos2.y).length()
                        if distance < col1.radius + col2.radius:
                            collisions.append((entity1, entity2))
        return collisions