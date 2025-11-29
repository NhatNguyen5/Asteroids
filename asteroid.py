from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        for _ in range(2):
            if _ == 1: 
                random_angle = -random_angle
            new_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid.velocity = self.velocity.rotate(random_angle)
            new_asteroid.velocity *= 1.2
