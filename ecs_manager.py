class ECSManager:
    def __init__(self):
        self.entities = []
        self.systems = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def add_system(self, system):
        self.systems.append(system)

    def update(self, dt):
        for system in self.systems:
            if hasattr(system, 'update'):
                system.update(self.entities, dt)