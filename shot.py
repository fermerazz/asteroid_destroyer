from circleshape import CircleShape
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.color = (255, 255, 255)  # White for the color shot
        self.lifetime = 1.0  # Lifetime in seconds
        self.time_alive = 0.0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
            
    def update(self, dt):
        self.position += self.velocity * dt
        self.time_alive += dt
        if self.time_alive >= self.lifetime:
            self.kill()
       
     