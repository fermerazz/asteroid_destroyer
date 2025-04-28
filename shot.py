from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.color = (255, 255, 0)  # Yellow color for the shot
        self.lifetime = 1.0  # Lifetime in seconds
        self.time_alive = 0.0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
            