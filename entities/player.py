from entities.entity import Entity
from components.position import Position
from components.velocity import Velocity
from components.renderable import Renderable
from components.collider import Collider

class Player(Entity):
    def __init__(self, x, y, surface):
        super().__init__()
        self.add_component(Position(x, y))
        self.add_component(Velocity(0, 0))
        self.add_component(Renderable(surface))
        self.add_component(Collider(surface.get_width() / 2))