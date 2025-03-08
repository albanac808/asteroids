import pygame
from components.position import Position
from components.renderable import Renderable

class RenderSystem:
    def __init__(self, screen):
        self.screen = screen

    def update(self, entities):
        for entity in entities:
            if entity.has_component(Position) and entity.has_component(Renderable):
                position = entity.get_component(Position)
                renderable = entity.get_component(Renderable)
                self.screen.blit(renderable.surface, (position.x, position.y))