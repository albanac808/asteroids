import pygame
import math
from player import Player
from constants import *

class BearShip(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ear_radius = self.radius / 2
        self.ear_distance = self.radius
        self.color = (139, 69, 19)  # A nice saddle brown color
        # or try (165, 113, 78)  # A softer light brown
        # or (101, 67, 33)  # A darker brown
        self.rotation = -90  # Start facing upward

    def move(self, dt):
        # Override the Player's move method
        forward = pygame.Vector2(1, 0).rotate(self.rotation)  # Start facing right
        self.position += forward * PLAYER_SPEED * dt

    def draw(self, surface):
        # Main head
        pygame.draw.circle(surface, self.color, self.position, self.radius)
        
        # Calculate ear positions
        x, y = self.position
        
        # Left ear (use rotation instead of heading)
        left_ear_angle = math.radians(self.rotation) + math.pi/4
        left_x = x + self.ear_distance * math.cos(left_ear_angle)
        left_y = y + self.ear_distance * math.sin(left_ear_angle)
        
        # Right ear
        right_ear_angle = math.radians(self.rotation) - math.pi/4
        right_x = x + self.ear_distance * math.cos(right_ear_angle)
        right_y = y + self.ear_distance * math.sin(right_ear_angle)

        # Draw the ears
        pygame.draw.circle(surface, self.color, (left_x, left_y), self.ear_radius)
        pygame.draw.circle(surface, self.color, (right_x, right_y), self.ear_radius)

        # Add inner ears - slightly darker brown
        inner_ear_color = (225, 198, 153)  # Darker brown
        inner_ear_radius = self.ear_radius * 0.6  # 70% of the main ear size
        pygame.draw.circle(surface, inner_ear_color, (left_x, left_y), inner_ear_radius)
        pygame.draw.circle(surface, inner_ear_color, (right_x, right_y), inner_ear_radius)

        # First eye (left)
        eye_angle = math.radians(self.rotation - 60)
        eye_distance = self.radius * 0.45
        eye_x = x + eye_distance * math.cos(eye_angle)
        eye_y = y + eye_distance * math.sin(eye_angle) + (self.radius * 0.2)
        eye_radius = self.radius * 0.12
        pygame.draw.circle(surface, (0, 0, 0), (eye_x, eye_y), eye_radius)

        # Second eye (right) - mirror of the first
        eye_angle_2 = math.radians(self.rotation + 60)  # Notice the + instead of -
        eye_x_2 = x + eye_distance * math.cos(eye_angle_2)
        eye_y_2 = y + eye_distance * math.sin(eye_angle_2) + (self.radius * 0.2)
        pygame.draw.circle(surface, (0, 0, 0), (eye_x_2, eye_y_2), eye_radius)

        # Nose position
        nose_angle = math.radians(self.rotation)
        nose_distance = self.radius * 0.1  # Reduced from 0.8
        nose_down_offset = self.radius * 0.05    # Reduced from 0.4

        # Calculate forward and downward vectors
        forward = pygame.Vector2(nose_distance, 0).rotate(self.rotation)
        downward = pygame.Vector2(0, nose_down_offset).rotate(self.rotation)

        # Apply both vectors to position
        nose_pos = self.position + forward + downward
        nose_x, nose_y = nose_pos
        
        # Draw the nose
        nose_width = self.radius * 0.25
        nose_height = self.radius * 0.15
        nose_color = (80, 50, 20)
        
        nose_rect = pygame.Rect(
            nose_x - nose_width/2,
            nose_y - nose_height/2,
            nose_width,
            nose_height
        )
        pygame.draw.ellipse(surface, nose_color, nose_rect)