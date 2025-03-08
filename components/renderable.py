import pygame

class Renderable:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface