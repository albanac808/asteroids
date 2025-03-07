class Entity:
    def __init__(self):
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component

    def get_component(self, component_type):
        return self.components.get(component_type)

class PositionComponent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class MovementSystem:
    def update(self, entities):
        for entity in entities:
            position = entity.get_component(PositionComponent)
            if position:
                # Update position
                pass