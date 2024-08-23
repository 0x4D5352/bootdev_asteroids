from random import uniform
import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = uniform(20, 50)
        positive_vector = self.velocity.rotate(random_angle)
        negative_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        positive_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        negative_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        positive_asteroid.velocity = positive_vector * 1.2
        negative_asteroid.velocity = negative_vector * 1.2
