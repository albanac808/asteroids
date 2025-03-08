from components.position import Position
from components.velocity import Velocity

class MovementSystem:
    def update(self, entities, dt):
        for entity in entities:
            if entity.has_component(Position) and entity.has_component(Velocity):
                position = entity.get_component(Position)
                velocity = entity.get_component(Velocity)
                position.x += velocity.dx * dt
                position.y += velocity.dy * dt