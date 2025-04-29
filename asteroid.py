from circleshape import CircleShape
import pygame
from main import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ang = random.uniform(20, 50) #random angle
            #Rotated vector
            vec_1 = self.velocity.rotate(ang)
            vec_2 = self.velocity.rotate(-ang)
            new_radius = self.radius - ASTEROID_MIN_RADIUS 
            
            #New asteroids
            ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            #Velocities
            ast_1.velocity = vec_1 * 1.2
            ast_2.velocity = vec_2 * 1.2

