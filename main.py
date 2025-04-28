import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroid_field import AsteroidField
from circleshape import *
import sys
from shot import Shot

def __main__():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    Clock = pygame.time.Clock()
    dt = 0 #Change in frames over last call 

    #Creating a display screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player  = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (updatable, drawable)

    #Infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
            for asteroid in asteroids:
                if asteroid.collision(player):
                    print("Game over!")
                    sys.exit()
        player.draw(screen)
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60)/1000
        

    






if __name__ == "__main__":
    __main__()