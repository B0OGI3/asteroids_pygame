from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event 
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        new_ast_one = self.velocity.rotate(rand_angle)
        new_ast_two = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_one = Asteroid(self.position.x, self.position.y, new_radius)
        ast_two = Asteroid(self.position.x, self.position.y, new_radius)

        ast_one.velocity = new_ast_one * 1.2
        ast_two.velocity = new_ast_two * 1.2